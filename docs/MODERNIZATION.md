# Modernization review — 2026-11-08

## Baseline and preservation

Fetched remote main matched `207fb6f366422ed0cc2bc8c0dde2a59c7c54cf6f`.
The workspace contained an extensive uncommitted reorganization, a reviewed
publication layer and Azure-specific assumptions. Development used a separate
worktree inside the authorized directory. Original files, reorganization and
local audit reports remain intact.

All 704 hashes in the earlier preservation ledger matched. A fresh snapshot of
713 files under the existing coursework/ and archive/ directories matched after
implementation. All 535 baseline tracked files outside explicit presentation,
documentation and tooling scope are unchanged. Private inventories stay local.

The PR adds portfolio/, tools/, documentation and a workflow. It does not stage
coursework moves or private archives. No history was rewritten and no original
academic project was executed or edited.

## Presentation and evidence

- Four case studies: housing analysis, Flask services, systems design/capstone,
  and responsive interfaces. Images are retained diagrams/screenshots or labeled
  architecture illustrations derived from inspected source.
- Search combines keywords with course filters, announces counts and handles
  empty results. Course/project/demo counts match the metadata.
- Accessible mobile menu, Escape handling, skip links, reduced motion and theme
  persistence; desktop and mobile layout checks.
- Corrected root-relative demo URLs and nested 404 recovery for GitHub Pages.
- Seven source links use verified files at the immutable baseline.
- Engineering descriptions checked against public READMEs for secure-crt-scripts,
  link-neighbor and cisco-ascii-banner-generator. These are documented capabilities,
  not claims of new runtime testing. Private home-lab evidence is omitted.

## Corrections and publication findings

INFO400 prints sqrt(mean_squared_error(...)) under an MAE label; it is RMSE.
Its held-out rows use observed lag values, not a recursive twelve-month forecast.
The historical write-up is retained with a separate visible correction and case
study. Reported scores were not reproduced or presented as verified results.

The Flask sources enable debugging and omit explicit HTTP timeouts. The case
study identifies these prototype limitations without editing the assignments.

Certificate files, personal credential records, unverified credential-status
claims and private infrastructure details are excluded from new publication.
Existing demonstration media and vendor libraries are retained. Azure config
is excluded from the new publication layer; existing local Azure files are intact.
The former blanket GitHub-link prohibition is replaced with a pinned-link allowlist.

The security boundary is the reviewed artifact, not the entire Git repository.
Previously committed coursework remains in Git/history. This is not a historical
exposure-removal exercise. Pattern checks supplement manual review; they cannot
guarantee detection of every secret or publication-rights issue.

## Local validation

- 123 allowlisted files built and fetched successfully over HTTP.
- 13 boundary tests passed: prohibited formats, disguised PDFs, private paths,
  changed/unreviewed files, contact links, unapproved sources, incorrect project
  roots and missing files/fragments.
- 14 automated WCAG A/AA scans passed for desktop/mobile main pages, case studies
  and dark catalog, after correcting contrast issues.
- Search, combined filters, empty state, menu/Escape, theme persistence, and
  nested 404 navigation passed at 1440 and 390 pixels.
- All HTML pages loaded without JavaScript exceptions. Six demo entry points
  loaded at both sizes; accordion interaction and local-only form handling passed.
- Seven immutable source paths verified in Git; change-scope audit passed.
- Preservation checks passed as detailed above.

Local tools: Python 3.15.2, Node 26.13.0, installed Chrome, Playwright 1.65.0 and
axe integration 4.14.0. CI targets Python 3.13 and Node 24. Python build tooling
uses only the standard library and declares Python 3.10+ compatibility.

## Limits and follow-up

No production deployment or merge. GitHub-hosted execution and live post-deployment
behavior require independent confirmation. The owner must select Pages Actions
and review environment protections before a manual deployment dispatch.

Automated accessibility checks are not a full assistive-technology audit.
Academic demos were smoke-tested; exhaustive accessibility redesign of every
assignment is outside this presentation change. Only Chrome was tested locally.
Original Flask services and housing analysis were not executed. External historic
reference sites were not exhaustively revalidated. No paid services are introduced.
