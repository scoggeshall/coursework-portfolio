"""Explicit maintainer action AFTER reviewing every public change. Never run in CI."""
import json
from validate_site import ROOT, validate, digest
if __name__=='__main__':
    public=ROOT/'portfolio/public'
    validate(public,sealed=False)
    manifest={p.relative_to(public).as_posix():digest(p) for p in sorted(public.rglob('*')) if p.is_file()}
    (ROOT/'portfolio/public-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(f'Sealed {len(manifest)} reviewed public files.')
