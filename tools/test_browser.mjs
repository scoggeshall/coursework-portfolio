// Local-only browser verification. No server binds to a public interface.
import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import { createServer } from 'node:http';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
const root = path.resolve(import.meta.dirname, '..');
const local = path.join(root, '.local');
await mkdir(local, {recursive:true});
process.env.TEMP = local; process.env.TMP = local; process.env.TMPDIR = local;
const site = path.join(root, 'site');
const prefix = '/coursework-portfolio/';
const mime = {'.html':'text/html','.css':'text/css','.js':'application/javascript','.json':'application/json','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.gif':'image/gif','.webp':'image/webp'};
const server = createServer(async (req,res) => {
  let file;
  try {
    const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    if (!pathname.startsWith(prefix)) throw Error('Outside public base');
    file = path.resolve(site, pathname.slice(prefix.length) || 'index.html');
    if (!file.startsWith(site+path.sep)) throw Error('Outside artifact');
    const data = await readFile(file);
    res.writeHead(200, {'Content-Type':mime[path.extname(file)] || 'application/octet-stream'}); res.end(data);
  } catch { res.writeHead(404, {'Content-Type':'text/html'}); res.end(await readFile(path.join(site,'404.html'))); }
});
await new Promise(resolve => server.listen(0,'127.0.0.1',resolve));
const base = `http://127.0.0.1:${server.address().port}${prefix.slice(0,-1)}`;
const browser = await chromium.launchPersistentContext(path.join(local,'browser-profile'), {
  headless:true, ...(process.platform === 'win32' ? {channel:'chrome'} : {}),
  downloadsPath:local, viewport:{width:1440,height:1000}, reducedMotion:'reduce'
});
const page = browser.pages()[0];
const errors=[], report={pages:[], demos:[], interactions:[]};
page.on('pageerror', e => errors.push(e.message));
page.on('response', r => { if(r.status()>=400 && !r.url().includes('missing-')) errors.push(`${r.status()} ${r.url()}`); });
try {
  const manifest = JSON.parse(await readFile(path.join(root,'portfolio/public-manifest.json'),'utf8'));
  for (const name of Object.keys(manifest)) {
    const response = await fetch(`${base}/${name}`);
    assert.equal(response.status,200,name);
  }
  const projects = JSON.parse(await readFile(path.join(root,'portfolio/projects.json'),'utf8'));
  for (const width of [1440,390]) {
    await page.setViewportSize({width,height:1000});
    for (const route of ['index.html','coursework.html',...projects.map(p=>`projects/${p.id}.html`)]) {
      await page.goto(`${base}/${route}`);
      assert.equal(await page.locator('h1').count(),1,route);
      assert(await page.evaluate(()=>document.documentElement.scrollWidth <= innerWidth),`Horizontal overflow: ${route} ${width}`);
      const result = await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
      report.pages.push({route,width,violations:result.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>n.target)}))});
    }
    await page.goto(`${base}/index.html`);
    await page.locator('img').evaluateAll(async images => {
      for (const img of images) img.loading='eager';
      await Promise.all(images.map(img=>img.decode()));
    });
    await page.screenshot({path:path.join(local,`homepage-${width}.png`),fullPage:true});
    assert.equal(await page.locator('[data-stat="courses"]').textContent(),'29');
    assert.equal(await page.locator('[data-stat="projects"]').textContent(),String(projects.length));
    if(width===390) {
      const menu=page.getByRole('button',{name:'Menu',exact:true});
      assert.equal(await page.locator('#primary-nav').isVisible(),false);
      await menu.click(); assert.equal(await menu.getAttribute('aria-expanded'),'true');
      await page.keyboard.press('Escape'); assert.equal(await menu.getAttribute('aria-expanded'),'false');
      await menu.click(); await page.locator('#primary-nav').getByRole('link',{name:'Coursework',exact:true}).click();
      assert(page.url().endsWith('/coursework.html'));
    }
    await page.goto(`${base}/coursework.html`);
    await page.locator('#course-search').fill('Flask');
    assert(await page.locator('.course:visible').count()>0);
    await page.getByRole('button',{name:'Data & Analysis',exact:true}).click();
    assert.equal(await page.locator('.course:visible').count(),0);
    assert(await page.locator('[data-empty]').isVisible());
    await page.getByRole('button',{name:'All',exact:true}).click();
    await page.locator('#course-search').fill('INFO400');
    assert.equal(await page.locator('.course:visible').count(),1);
    await page.locator('#course-search').fill('');
    assert.equal(await page.locator('.course:visible').count(),29);
    await page.locator('[data-theme-toggle]').click();
    assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
    const dark=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
    report.pages.push({route:'coursework.html (dark)',width,violations:dark.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))});
    await page.reload(); assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
    await page.locator('[data-theme-toggle]').click();
    report.interactions.push({width,search:true,combinedFilter:true,emptyState:true,themePersistence:true,mobileMenu:width===390});
  }
  const demos=JSON.parse(await readFile(path.join(root,'portfolio/demos.json'),'utf8'));
  for(const demo of demos) {
    for (const width of [1440,390]) {
      await page.setViewportSize({width,height:1000});
      await page.goto(`${base}/${demo.url}`);
      assert(await page.locator('body').innerText());
    }
    report.demos.push(demo.url);
  }
  for(const route of Object.keys(manifest).filter(name=>name.endsWith('.html') && name!=='404.html')) {
    await page.goto(`${base}/${route}`);
    assert(await page.locator('body').innerText(),route);
  }
  await page.goto(`${base}/demos/webd343-jquery/index.html`);
  await page.locator('#accordion h2').nth(1).click();
  await page.waitForTimeout(500);
  assert(await page.locator('#accordion p').nth(1).isVisible());
  await page.goto(`${base}/demos/webd221-evolution-of-video-games/game-form.html`);
  const form=page.locator('form');
  await form.evaluate(node=>node.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true})));
  assert(await page.getByText('Demonstration only. Nothing was sent or saved.').isVisible());
  report.interactions.push({accordion:true,formSubmissionPrevented:true,allHtmlPagesLoaded:true});
  const missing=await page.goto(`${base}/missing-folder/missing-page`);
  assert.equal(missing.status(),404);
  await page.getByRole('link',{name:'Portfolio home'}).click();
  assert.equal(await page.locator('[data-stat="projects"]').textContent(),String(projects.length));
  await page.goto(`${base}/index.html#%E0%A4%A`);
  assert.equal(errors.length,0,errors.join('\n'));
  report.runtimeErrors=errors;
  await writeFile(path.join(local,'browser-results.json'),JSON.stringify(report,null,2));
  assert.equal(report.pages.reduce((n,p)=>n+p.violations.length,0),0,'Accessibility failures: see .local/browser-results.json');
  console.log(`PASS: ${report.pages.length} accessibility scans; desktop/mobile search, filters, themes, navigation; ${report.demos.length} demo entry points; ${Object.keys(manifest).length} HTTP files; nested 404.`);
} finally { await browser.close(); await new Promise(resolve=>server.close(resolve)); }
