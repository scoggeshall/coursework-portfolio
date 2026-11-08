# Technical coursework portfolio

A static portfolio with four case studies, a searchable catalog of 29 courses,
six browser demonstrations, and links to public engineering tools.

Website: https://scoggeshall.github.io/coursework-portfolio/

## Source and publication boundaries

| Location | Purpose |
| --- | --- |
| `portfolio/public/` | Reviewed presentation copies; authoritative public source |
| `portfolio/*.json` | Metadata, pinned source links, and SHA-256 publication allowlist |
| `site/` | Ignored generated output; the only Pages artifact |
| `tools/` | Python build/validation and Node browser tests |
| `docs/` | Publication policy and modernization evidence |
| Existing course folders | Preserved original tracked coursework; never deployment inputs |

The pre-existing local reorganization into `coursework/` and `archive/` remains
intact. This PR does not stage those moves or publish the private collection.
Legacy tracked course paths remain unchanged. The complete course catalog links
to reviewed write-ups and demos; restricted originals are not public downloads.

## Build and test

Python 3.10+ builds without third-party packages. Browser checks use Node 22+
and locked development dependencies. The website requires no backend.

```powershell
python tools/build_site.py
python -m unittest discover -s tools -p test_validation.py -v
python tools/audit_workspace.py
npm ci --ignore-scripts --no-audit --no-fund
node tools/test_browser.mjs
```

Windows tests use installed Chrome and a repository-local profile. On Linux,
install the test browser with `npx playwright install --with-deps chromium`.
Screenshots and reports go to ignored `.local/`. Tests serve only `site/`, on
loopback, with the GitHub Pages project prefix and real HTTP 404 handling.

Review public changes before running `python tools/review_manifest.py`.
Never regenerate the allowlist automatically in CI. Unknown files, changed
hashes, unsafe links, prohibited formats, and detected secrets fail validation.

## GitHub Pages

The workflow validates PRs and pushes to `main`. Deployment requires an explicit
manual dispatch on `main` with `deploy` selected, after all checks pass. It uploads
only `site/`. A push or merge does not automatically deploy. No Azure, paid hosting,
subscription, or billing changes are introduced.

See [publication policy](docs/PUBLICATION.md) for approval and deployment steps,
and [the review report](docs/MODERNIZATION.md) for preservation and test evidence.
