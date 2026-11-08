# Publication and deployment policy

## Review before sealing

1. Edit presentation copies under `portfolio/public/` and their metadata.
2. Review text, images, media and links for personal records, credentials, device
   identifiers, private infrastructure and restricted material. Scanners cannot
   establish publication rights or detect every possible secret.
3. Source links must be listed in `portfolio/source-links.json`, use a full
   immutable Git commit, and refer to a reviewed file. Validation checks the
   repository, URL structure and file existence in Git; other blob/tree links fail.
4. Preserve originals. Document corrections in separate explanations.
5. Only after review, run `python tools/review_manifest.py` and commit the changed
   allowlist with the reviewed files. The workflow never regenerates hashes.
6. Build and run publication, preservation and browser checks.

The build copies only allowlisted files whose SHA-256 matches. Unknown existing
output files fail rather than being deleted. Review such files manually.
Coursework and archive directories are never deployment inputs. Validation
rejects prohibited formats, disguised binaries, reparse points, hard links,
escaping paths, broken links/fragments, metadata drift, personal contact links,
unapproved source URLs and detected credential patterns.

HTML CSP disables API calls, form submission, frames and objects. Inline scripts
and styles remain permitted for compatibility with academic demos; this is not
strict script isolation. Demo forms use fictional input and do not submit.
GitHub Pages does not apply Azure staticwebapp.config.json headers.

## Deployment after review

No merge, deployment, billing change or repository setting change is performed
by development of this PR.

After reviewing and merging:

1. Select GitHub Actions in repository Settings → Pages.
2. Review the `github-pages` environment: restrict to `main` and add required
   reviewers where available. The workflow does not configure these protections.
3. Manually run “Portfolio validation and approved Pages deployment” on `main`,
   selecting `deploy`. Leaving it clear runs validation only.
4. Approve the environment if required. All validation must pass before the
   sealed `site/` artifact can deploy.
5. Check the resulting Pages URL and nested 404 recovery.

PRs and pushes cannot enter the deployment job. Only that job receives Pages
write and OIDC permissions. Actions use pinned commit references and checkout
credentials are not persisted. Dependencies are test-only and locked. There are
no alternative hosts, paid services or subscriptions in this implementation.

Reference: [GitHub custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
