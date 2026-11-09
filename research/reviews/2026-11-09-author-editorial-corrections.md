# Author's editorial corrections — 9 November 2026

Scope: the six requested corrections to references, proof endings, the Radon definition, the title page and standard-material citations. This is a local editorial review, not a fresh mathematical certification of the chapters or the whole book.

## Changes

- SGPT is linked at `https://mingchenxia.github.io/Lectures/SGPT_final.pdf` in the bibliography. VX reads "to appear".
- Removed source-provenance, version and retention commentary from printed references and the historical appendix. Exact source links and previously checked research records retain the source identities and locator evidence. No new source theorem or publication data were inferred.
- Removed all citations of Tao's expository notes from Appendix B, along with comparisons whose only purpose was to assign sources to standard results. Research-result attribution, including PSHD and the accepted resolution/principalization interfaces, remains.
- Added a footnote at Definition 1.1.1 explaining the usual open-set inner-regularity convention and its equivalence here by Proposition 1.1.2. Read the definition and the complete adjacent regularity proposition/proof; no hypotheses or definition were changed.
- Added "To Charles Favre" on the title page, using the existing subtitle facility.
- Added mathematical closing prose to ten proofs ending in displays: P01 vague set inequalities; P02 fundamental solution; P03 distributional representative; P06 Gaussian transform; Q02 local Lp integrability; Q08 increasing continuity and truncation mass/capacity; Q10 rooftop algebra, extrapolation contact and strict minorant. A one-line page enlargement keeps the truncation estimate, closing sentence and QED together on printed page 299.
- Updated the project citation/proof policy and repository-local book skill memory. No external installed skill was modified; the repository-local skills are the applicable cloud copies. The edited skill front matter and relative resource links were validated.

## Review and verification

Read the changed passages twice in context, including their adjacent statements and final implications; compared the bibliography edits and historical-note changes against the previous text. This is not a complete new read of the ten long proofs or their source papers. Displayed mathematics in every edited chapter input is unchanged. The P01 dossier and reference guide were consulted; no GZ mathematical assertion or erratum was newly adopted.

- `make check`: passed; 61 active TeX inputs and all immutable source files intact.
- `make audit`: 0 errors; existing advisory warnings reviewed at the edited scope.
- `make progress`: regenerated, with all mathematical statuses unchanged. Editorial-review links are added to the affected chapter/task records without replacing their original proof-review evidence.
- `make build`: passed with no unresolved citations/references or fatal errors. The environment initially lacked fonts; installed official CTAN runtime packages `newtx`, `kastrup`, `tex-gyre` and `doublestroke` in `/workspace/texmf`, with font maps in workspace-owned configuration/variable directories. The build used `TEXMFHOME=/workspace/texmf TEXMFVAR=/workspace/texmf-var TEXMFCONFIG=/workspace/texmf-config`. Four small overfull boxes (2.05–3.63 pt) occur on unchanged source lines; no underfull boxes remain after setting the bibliography ragged right. The four affected physical pages (25, 373, 676 and 829) were checked in a contact sheet; nothing is clipped. No warnings were suppressed.
- All 597 active proof environments were scanned: none ends in a display. The PDF contains 602 square glyphs, accounting for 597 proof end marks and the five explicit mathematical `\square` occurrences.
- Direct full-page inspection: physical pages 1, 20, 39, 62, 85, 147, 235, 279, 313–314, 620, 698, 700 and 947–949. All ten changed proof end marks are visible. The first render placed the dedication on page 2; this was corrected and the final title page inspected. The initial isolated closing sentence on page 314 was corrected; final pages 313–314 were inspected again.
- Layout inspection of the historical appendix: all physical pages 907–934 in labelled contact sheets. Other inspected proof-page rasters were byte-identical after the final page-enlargement change, carrying their direct visual inspection forward. This is not direct visual inspection of all 949 pages.
- SGPT destination responded HTTP 200. Final PDF: 949 physical pages, last printed page 935. SHA-256: `0059c9b8e4d86b44962f167ffc7d5e6b2cde4f3e85fc3140ce4d1404f602181a`.

The standing publication destination is `MingchenXia/mingchenxia.github.io`, `Papers/FPT_vibe.pdf`; the homepage entry retains its position and existing dedication description, with the physical page count and update date revised together with the PDF. Publication outcome is recorded in the session handoff.

Publication verification: homepage commit `c1dafbc4253fc9a056f2d76328631c7b331c50af` is on remote main. Downloading its immutable public `raw.githubusercontent.com` PDF returned exactly the compiled SHA-256 above. The source edits were pushed as `0145d3f3ee0109ce9c5f73e630ebabafc345e70b`. At the final hosting check, GitHub Pages run `42547326658` had completed the build and was still deploying; the main site still served the previous PDF. The immutable uploaded PDF is available while hosting finishes.
