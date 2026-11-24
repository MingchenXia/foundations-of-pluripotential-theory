# Terminology, the subharmonic convention and the Introduction, 24 November 2026

The author made three requests on the current main branch (`cf848be`):
- remove the word "collar" throughout the book;
- point out that the convention allowing a subharmonic function to be identically $-\infty$ differs from the convention of [SGPT];
- stop emphasizing, in the Introduction, the ceiling identity and the example taken from [SGPT], and improve the Introduction of the whole book.

## Changes

- **"Collar."** Every occurrence in Chapters 9, 15, 17 and Appendix B (55, counting three label names) was removed. "A collar of $\partial B$" became "an open neighborhood of $\partial B$" where openness is used (for example, where a compact complement is needed) and "a neighborhood of $\partial B$" otherwise. A potential "with a quadratic collar" is now "quadratic near $\partial B$". The two terms of a split integral formerly called the "collar term" are now named by their domain of integration. The definition sentence and its index entry "collar of a sphere" were removed. The labels `eq:bt-collar-modification`, `lem:bt-common-collar` and `eq:quadratic-collar-energy-approximation` were renamed `eq:bt-boundary-modification`, `lem:bt-common-boundary-values` and `eq:quadratic-boundary-energy-approximation`, also in `plan/tasks.json`. No statement changed.
- **Convention.** After `def:subharmonic` (Chapter 3), a short paragraph says that [SGPT, Definition 1.1.1] requires a subharmonic function on a domain not to be identically $-\infty$, and notes two consequences of the convention used here (decreasing limits, `thm:subharmonic-decreasing`; restrictions of psh functions to lines). The list of conventions records the same difference and notes that plurisubharmonic functions on a domain exclude $-\infty$ in both books. The locator was checked against the published SGPT PDF (Definition 1.1.1, Section 1.1.1) and its retained source (`def:subhar1`, `def:psh`).
- **Introduction.** The paragraph on the diffuse polar example and the sentence on the ceiling identity were removed. The Introduction now states the readership and the three principles of the book (self-containedness up to resolution and principalization; pointwise versus almost-everywhere statements; explicit treatment of degenerate cases), keeps the overview of the two parts, replaces the example by a sentence comparing the holomorphic and the nonlinear measurement of singularities, and ends with a reading guide. The chapter groups in the guide were checked against the actual cross-references between chapters, and the closing paragraph points to the convention difference. The Part II introduction is unchanged.

## Validation

- `make check`: integrity OK (62 active TeX files). `make audit`: 0 errors, 81 warnings.
- Forced build: no unresolved references or citations, no overfull boxes; 949 physical pages. Log: `research/reviews/logs/2026-11-24-collar-convention-introduction-build.log`.
- Inspected the Introduction (physical pages 3–6), the Conventions (page 15), the new paragraph in Chapter 3 (page 80) and the rephrased opening of Section 9.2 (page 253).

These are reviews by the authoring agent; builds and audits do not verify mathematics.
