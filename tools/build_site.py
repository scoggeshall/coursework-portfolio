"""Copy only explicitly reviewed public files; archive/coursework are never inputs."""
from pathlib import Path
import json, shutil
from validate_site import ROOT, digest, validate

def main():
    src=ROOT/'portfolio/public'; dst=ROOT/'site'
    manifest=json.loads((ROOT/'portfolio/public-manifest.json').read_text())
    validate(src)
    # Fail on unexpected output rather than silently deleting possible user work.
    if dst.exists():
        for p in dst.rglob('*'):
            if p.is_symlink() or (hasattr(p,'is_junction') and p.is_junction()): raise ValueError('Unsafe output link')
            if p.is_file() and p.relative_to(dst).as_posix() not in manifest: raise ValueError('Unexpected output file: '+str(p))
    for rel,sha in manifest.items():
        a=(src/rel).resolve(); b=(dst/rel).resolve()
        if not a.is_relative_to(src) or not b.is_relative_to(dst): raise ValueError('Manifest path escapes publication boundary')
        if not a.is_file() or digest(a)!=sha: raise ValueError('Unreviewed input: '+rel)
        if b.exists() and b.stat().st_nlink > 1: raise ValueError('Hard-linked output: '+rel)
        b.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(a,b)
    result=validate(dst)
    (ROOT/'docs/validation-result.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(f"PASS: {result['files']} public files, {result['courses']} official courses, {result['demos']} demos")
if __name__=='__main__': main()
