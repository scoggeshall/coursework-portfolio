"""Fail if this modernization changes academic files or introduces unrelated paths.

The immutable pre-modernization baseline keeps this check independent of main.
No files are written by this audit.
"""
from pathlib import Path
import subprocess
from validate_site import ROOT, validate
BASE='207fb6f366422ed0cc2bc8c0dde2a59c7c54cf6f'
ALLOWED_FILES={'.gitattributes','.gitignore','README.md','package.json','package-lock.json'}
ALLOWED_PREFIXES=('portfolio/','tools/','docs/','.github/workflows/')
def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True)
def main():
    changed=git('diff','--name-only',BASE,'--').splitlines()
    added=git('ls-files','--others','--exclude-standard').splitlines()
    unexpected=[name for name in changed+added if name not in ALLOWED_FILES and not name.startswith(ALLOWED_PREFIXES)]
    if unexpected: raise ValueError('Changes outside portfolio scope: '+', '.join(unexpected))
    baseline=git('ls-tree','-r','--name-only',BASE).splitlines()
    protected=[name for name in baseline if name not in ALLOWED_FILES and not name.startswith(ALLOWED_PREFIXES)]
    # git diff compares bytes/objects to the baseline and also catches deletions.
    if any(name in changed for name in protected): raise ValueError('Original tracked content changed')
    result=validate(ROOT/'site')
    print(f"PASS: {len(protected)} baseline files unchanged; {result['files']} allowlisted public files; change scope restricted")
if __name__=='__main__': main()
