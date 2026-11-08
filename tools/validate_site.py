"""Fail-closed final-artifact validation. Python 3.10+ standard library only."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import hashlib, html, json, re, sys, subprocess
ROOT=Path(__file__).resolve().parents[1]
ALLOWED={'.html','.css','.js','.json','.png','.jpg','.jpeg','.gif','.webp','.svg','.ico'}
PROHIBITED=re.compile(r'archive/|transcript|student[-_ ]?id|\bAssociates\b|\bBachelors\b|coursework/|dev\.azure\.com|visualstudio\.com|\b(?:date of birth|home address|social security number|FERPA)\b|\b\d{3}-\d{2}-\d{4}\b',re.I)
SECRET=re.compile(r'-----BEGIN .*PRIVATE KEY-----|(?:api[_-]?key|password|deployment[_-]?token)\s*[:=]\s*["\'][^"\'\s]{8,}["\']',re.I)
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.refs=[]; self.ids=set(); self.text=[]; self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        for key in ['href','src','poster','action']:
            if a.get(key): self.refs.append((a[key],tag,key))
        if a.get('srcset'):
            self.refs.extend((x.strip().split()[0],tag,'src') for x in a['srcset'].split(','))
    def handle_data(self,data): self.text.append(data)
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(site, sealed=True):
    site=Path(site).resolve()
    if not site.is_relative_to(ROOT): raise ValueError('Validation target must be inside workspace')
    files={p.relative_to(site).as_posix():p for p in site.rglob('*') if p.is_file()}
    errors=[]; external=set(); pages={}
    source_links=set(json.loads((ROOT/'portfolio/source-links.json').read_text(encoding='utf-8')))
    for link in source_links:
        match=re.fullmatch(r'https://github\.com/scoggeshall/coursework-portfolio/blob/([0-9a-f]{40})/(.+)',link)
        if not match or match[2].startswith('/') or '..' in match[2].split('/'):
            errors.append('Invalid approved GitHub source link'); continue
        exists=subprocess.run(['git','cat-file','-e',match[1]+':'+match[2]],cwd=ROOT,capture_output=True)
        if exists.returncode: errors.append('Approved source missing from pinned Git revision: '+match[2])
    if not files: errors.append('Empty public output')
    for p in site.rglob('*'):
        if p.is_symlink() or (hasattr(p,'is_junction') and p.is_junction()): errors.append('Link/reparse point: '+str(p))
    for rel,p in files.items():
        if p.stat().st_nlink > 1: errors.append('Hard-linked public file: '+rel)
        if p.suffix.lower() not in ALLOWED or PROHIBITED.search(unquote(rel)) or any(x.startswith('.') for x in p.relative_to(site).parts): errors.append('Prohibited file/path: '+rel)
        data=p.read_bytes()
        if data.startswith((b'PK\x03\x04',b'%PDF',b'SQLite format',b'MZ')): errors.append('Prohibited binary signature: '+rel)
        if p.suffix.lower() in {'.html','.css','.js','.json','.svg'}:
            try: s=data.decode('utf-8')
            except UnicodeDecodeError: errors.append('Non-UTF8 text: '+rel); continue
            if PROHIBITED.search(html.unescape(s)): errors.append('Prohibited content: '+rel)
            if SECRET.search(s): errors.append('Possible embedded credential: '+rel)
            if p.suffix=='.html': pages[rel]=Page(s)
    def check(ref,rel,tag='a',attr='href'):
        ref=html.unescape(ref).strip(); u=urlsplit(ref)
        if u.scheme or u.netloc:
            if u.scheme not in ['https','mailto','tel']: errors.append('Unsafe URL: '+rel+' -> '+ref)
            if u.scheme in ['mailto','tel']: errors.append('Personal contact link: '+rel)
            if u.hostname == 'github.com' and ('/blob/' in u.path or '/tree/' in u.path) and ref not in source_links: errors.append('Unreviewed source link: '+rel)
            external.add(ref)
            if tag not in ['a'] and attr in ['src','href']: errors.append('Remote runtime dependency: '+rel+' -> '+ref)
            return
        path=unquote(u.path)
        if path.startswith('/coursework-portfolio/'):
            path=path[len('/coursework-portfolio/'):]
            path='/' + path
        elif path.startswith('/'):
            errors.append('Root URL bypasses GitHub Pages project base: '+rel+' -> '+ref)
        if '\\' in path: errors.append('Backslash URL: '+rel+' -> '+ref); return
        target=(site/path.lstrip('/') if path.startswith('/') else (site/rel).parent/path).resolve() if path else site/rel
        if not target.is_relative_to(site): errors.append('Public boundary escape: '+rel+' -> '+ref); return
        if target.is_dir(): target=target/'index.html'
        key=target.relative_to(site).as_posix()
        if key not in files: errors.append('Missing target: '+rel+' -> '+ref)
        elif u.fragment and target.suffix=='.html' and unquote(u.fragment) not in pages[key].ids:
            errors.append('Missing fragment: '+rel+' -> '+ref)
    for rel,page in pages.items():
        for ref,tag,attr in page.refs: check(ref,rel,tag,attr)
    for rel,p in files.items():
        if p.suffix=='.css':
            for ref in re.findall(r'url\(\s*["\']?([^\)"\']+)',p.read_text(encoding='utf-8')): check(ref,rel,'style','src')
    official=json.loads((ROOT/'portfolio/official-courses.json').read_text(encoding='utf-8'))
    courses=json.loads((ROOT/'portfolio/courses.json').read_text(encoding='utf-8'))
    demos=json.loads((ROOT/'portfolio/demos.json').read_text(encoding='utf-8'))
    if len(courses)!=len(official) or {c['code'] for c in courses}!=set(official): errors.append('Course coverage must match unique official courses')
    projects=json.loads((ROOT/'portfolio/projects.json').read_text(encoding='utf-8'))
    network=json.loads((ROOT/'portfolio/network-projects.json').read_text(encoding='utf-8'))
    approved_network_repositories={
        'https://github.com/scoggeshall/link-neighbor',
        'https://github.com/scoggeshall/secure-crt-scripts',
        'https://github.com/scoggeshall/cisco-ascii-banner-generator',
    }
    if len({p['id'] for p in network})!=len(network): errors.append('Duplicate network project ID')
    check('network-engineering.html','index.html')
    for project in network:
        if project['repository'] not in approved_network_repositories: errors.append('Unapproved network repository')
        if not re.fullmatch(r'[0-9a-f]{40}',project['revision']): errors.append('Network evidence must pin a full revision')
        route='network/'+project['id']+'.html'
        check(route,'index.html'); check(project['image'],'index.html','img','src')
        if route in files:
            content=files[route].read_text(encoding='utf-8')
            if project['revision'] not in content or project['repository'] not in content: errors.append('Network evidence metadata drift: '+route)
    for route in ['network-engineering.html',*(r for r in pages if r.startswith('network/'))]:
        if route not in files: continue
        content=files[route].read_text(encoding='utf-8')
        if re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[0-9a-f]{2}:){5}[0-9a-f]{2}\b',content,re.I): errors.append('Operational identifier in networking presentation: '+route)
        for ref,tag,attr in pages[route].refs:
            if urlsplit(ref).hostname=='github.com' and ref not in approved_network_repositories: errors.append('Unapproved network repository link: '+route)
    if len({p['id'] for p in projects})!=len(projects): errors.append('Duplicate project ID')
    for project in projects:
        check('projects/'+project['id']+'.html','index.html')
        check(project['image'],'index.html','img','src')
        if not project['codes'] or any(code not in official for code in project['codes']): errors.append('Unknown project course')
    js=(site/'script.js').read_text(encoding='utf-8')
    published=json.loads(re.search(r'const COURSES = (.*);',js).group(1))
    if published!=courses: errors.append('Public course data differs from reviewed course metadata')
    published_demos=json.loads(re.search(r'const DEMOS = (.*);',js).group(1))
    if published_demos!=demos: errors.append('Public demo data differs from reviewed demo metadata')
    published_projects=json.loads(re.search(r'const PROJECTS = (.*);',js).group(1))
    if published_projects!=projects: errors.append('Public project data differs from reviewed project metadata')
    home=files['index.html'].read_text(encoding='utf-8')
    for kind,value in [('courses',len(courses)),('projects',len(projects)),('demos',len(demos))]:
        if f'data-stat="{kind}">{value}<' not in home: errors.append('Homepage count differs from metadata: '+kind)
    for c in courses:
        if c['title']!=official.get(c['code']): errors.append('Course pair mismatch: '+c['code'])
        if c.get('demo'): check(c['demo'],'index.html')
        if c.get('writeups'): check('writeups/index.html#'+c['writeups']['slug'],'index.html')
    for d in demos:
        if d['course']!=d['code']+' — '+official[d['code']]: errors.append('Demo course mismatch')
        check(d['url'],'index.html')
        for rel,page in pages.items():
            if rel.startswith(str(Path(d['url']).parent).replace('\\','/')+'/') and d['course'] not in ''.join(page.text): errors.append('Missing complete demo course label: '+rel)
    for rel,page in pages.items():
        text=' '.join(page.text)
        markup=files[rel].read_text(encoding='utf-8')
        for course_label in re.findall(r'<span class="code-chip">(.*?)</span>',markup):
            if html.unescape(course_label) not in [code+' — '+title for code,title in official.items()]: errors.append('Incomplete featured course label: '+rel)
        if rel.startswith('writeups/') and rel!='writeups/index.html':
            prefix=Path(rel).name.split('-')[0]
            code={'fundamentals':'ENTD200','entd320':'ENTD320','info400':'INFO400','stem380':'STEM380','hrmt101':'HRMT101'}.get(prefix)
            for tag in [r'<title>(.*?)</title>',r'<p class="eyebrow">(.*?)</p>']:
                match=re.search(tag,markup,re.S)
                if not code or not match or code+' — '+official[code] not in html.unescape(match[1]): errors.append('Incomplete write-up course label: '+rel)
        if re.search(r'\.submit\s*\(',markup): errors.append('Form bypasses local-only demonstration handling: '+rel)
        for code in set(re.findall(r'\b[A-Z]{4}\d{3}\b',text)):
            if code not in official: errors.append('Unverified course: '+rel+' '+code)
    if sum(p.stat().st_size for p in files.values())>250*1024*1024: errors.append('Public artifact exceeds the project size budget')
    if sealed:
        approved=json.loads((ROOT/'portfolio/public-manifest.json').read_text())
        actual={rel:digest(p) for rel,p in files.items()}
        if actual!=approved: errors.append('Final manifest differs from reviewed publication allowlist (added, missing or changed file)')
    if errors: raise ValueError('\n'.join(sorted(set(errors))))
    return {'files':len(files),'bytes':sum(p.stat().st_size for p in files.values()),'courses':len(courses),'projects':len(projects),'demos':len(demos),'html_pages':len(pages),'external_links':sorted(external),'status':'PASS'}
if __name__=='__main__':
    try:
        result=validate(ROOT/(sys.argv[1] if len(sys.argv)>1 else 'site'), '--unsealed' not in sys.argv)
        print(json.dumps(result,indent=2))
    except (ValueError,AssertionError) as e: print(str(e),file=sys.stderr); sys.exit(1)
