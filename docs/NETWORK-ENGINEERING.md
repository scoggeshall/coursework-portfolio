# Network Engineering expansion — 2026-11-08

## Scope and evidence

Branch starts at merged main `92b459b5fee611050eeec0cba97fc8e8aebed8c3`.
The prior modernization branch and the root workspace's uncommitted reorganization
remain untouched. Development is in a separate worktree inside the authorized
directory. Original coursework and separate networking repositories are unchanged.

The homepage now prioritizes Network Engineering & Automation before academic
projects. The dedicated page covers six skill areas and six educational scenarios.
Three project case studies describe purpose, implementation, engineering challenges,
features, limitations, inspected revision and source filenames. Four original SVG
diagrams illustrate workflows without operational identifiers. All existing
public paths and the homepage `#engineering` anchor are retained.

Evidence categories are explicit:

- **Repository-backed:** source and README inspection supports the stated tool
  behavior. The tools were not executed against equipment during this update.
- **Author-described experience:** the user supplied the routing, wireless,
  monitoring, security and automation areas. Production scope, employers, years,
  achievements and measured results are not independently asserted.
- **Laboratory scope:** Cisco switching, Ubuntu, Windows ICS and discovery are
  labeled as home-lab topics, not production deployments or a completed lab report.
- **Illustrative:** WAN/OSPF, campus VLANs, WLAN diagnosis, infrastructure visibility,
  SNMPv3 and scripting scenarios are newly written educational examples. They are
  not sanitized transcripts of real incidents or actual configurations.
- **Proposed:** platform-aware diagnostic completion checks and fixture tests are
  identified as possible future improvements, not implemented repository features.

## Inspected public sources

| Repository | Immutable revision | Files inspected |
| --- | --- | --- |
| [Link Neighbor](https://github.com/scoggeshall/link-neighbor) | `bc1383329aeed2dee544eae02cc5c2100baf0033` | README.md; Find-LinkNeighbor.ps1 |
| [SecureCRT Scripts](https://github.com/scoggeshall/secure-crt-scripts) | `9d70fc6162cfe5207c4ee97c34815c1f76b09ce1` | README.md; oui-lookup/oui-lookup.py; cable-test/cable-test.py |
| [Cisco ASCII Banner Generator](https://github.com/scoggeshall/cisco-ascii-banner-generator) | `1252b61b896d64c112aae36b37475497030a792d` | README.md; cisco_banner.py |

README blob hashes were respectively `b68f41da6a4c17760d35affaadfeb7929448444d`,
`173a1a517f436d39e30ffa5f7808bb24085b43b8`, and
`4999c04812e1c769f5d5748eaa699778c3509f9f`.

Link Neighbor implementation confirms interface correlation, protocol-specific
fields, bounded capture, and first-packet behavior. SecureCRT confirms preservation
of displayed MAC formatting, longest supported OUI-prefix matching, and a confirmed
TDR action with a fixed ten-second delay. That delay does not prove completion.
The banner source confirms ASCII checks, font/layout handling, safe filename logic
and delimiter selection; the documented runtime requirement is not a new test result.

Technical scenario references are linked on the page: RFC 2328 for OSPFv2,
RFC 3414 for SNMPv3 USM, Cisco's VLAN trunking and wireless DHCP references,
and the Wireshark User's Guide. No platform-specific configuration commands were
invented, and Cisco syntax is not presented as interchangeable with Extreme syntax.

## Publication controls

The SHA-256 manifest remains the artifact boundary. Existing sensitive-format,
credential-pattern, path/link, metadata and immutable academic-source checks remain.
New checks validate networking metadata/revision syntax, metadata-to-page agreement,
the three approved repository URLs, and absence of IPv4/MAC identifiers in networking
HTML. New negative tests reject identifiers and unapproved repository links.
These checks supplement review; they are not exhaustive personal-data detection.

No operational screenshot, packet capture, device address, hostname, secret,
certificate, workplace configuration or restricted source material was copied.
The public diagrams are newly authored and explicitly illustrative. The only new
command example is the repository's documented local function invocation without
device identifiers. No network equipment was accessed or changed.

GitHub Pages and the existing GitHub Actions workflow are retained unchanged.
Deployment still requires an explicit manual dispatch from main. No alternative
hosting, paid service, dependency addition, automatic merge or deployment is introduced.

## Local validation

- 131 manifest-approved public files build and return HTTP 200 under the Pages prefix.
- 15 publication boundary tests pass, including both new networking rejection tests.
- 24 automated WCAG A/AA scans pass at 1440 and 390 pixels, including all networking
  pages and the networking landing page in dark mode.
- Networking homepage CTA, all three case-study round trips, mobile menu navigation,
  academic search/filter behavior, theme persistence and nested 404 recovery pass.
- Existing demos and all public HTML load without JavaScript exceptions; existing
  accordion and local-only form behavior pass.
- Git preservation audit confirms 535 protected baseline tracked files unchanged.
- All 713 local coursework/archive files match the fresh pre-task SHA-256 snapshot.

Browser execution used installed Chrome with the existing locked Playwright/axe
dependencies; Python tooling ran locally. Automated accessibility checks do not
replace a manual assistive-technology audit. Other browser engines, real network
device execution, GitHub-hosted checks and post-deployment behavior are not claimed
as verified by these local results.
