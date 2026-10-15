# Round 4: proofreading for readability and presentation (13 October 2026)

## Request and scope

After round 3 (`research/reviews/2026-10-07-complete-proofs-round3.md`) and the notation changes that followed it (commit `8549555`, 934 physical pages), the author asked for a new round of proofreading focused on readability and presentation.

Round 3 had added many lemmas and long arguments under correctness pressure, so this round concentrated on how the text reads:
- the structure of long proofs: one-sentence plans, genuine steps with stated goals, notation declared before use, no letter with two meanings in one proof, paragraphs split at their logical joints, and arguments derived twice stated once;
- the placement and motivation of auxiliary results, and chapter and section openings that describe the text as it now is;
- sentences: length, clear antecedents, reasons placed next to claims, no meta remarks;
- formulas: long inline formulas displayed, displays punctuated, notation consistent across chapters;
- proofreading: typos, item and step references, spelling and capitalization.

Mathematical content was to stay unchanged, except for genuine errors, each of which had to be reported.

Scope: the 61 active TeX files (front matter, Chapters 1–18, Appendix A, Appendix B). Baseline: `8549555`.

## Method

1. **Proofreading**, one agent per unit, 30 units. Large files were split by region: Chapter 14 at §14.5, Appendix A at §A.4, and the Chapter 9 and Chapter 16 inputs in two groups each. Each agent read its unit completely and in order, together with the neighboring chapter ends and openings, and reported every change of mathematical content.
2. **Independent check**, a different agent per unit (the Chern-smoothing input of Chapter 16 had its own checker). The checker examined every hunk of `git diff 8549555`, verified each reported correction, reread the unit, checked that every label, citation with its locator and index entry was preserved, and compiled the unit. Checkers fixed drift with minimal local edits.
3. **Coordinator**: routing of cross-unit observations to the agents concerned, small local edits where a report left a doubt, a book-wide layout fix (a paragraph break after the 29 proofs that were followed directly by text), front-matter review and full builds.

## What changed

- **Long proofs.** Plans were added to the long proofs of round 3 and earlier, and step headings were renumbered where steps were missing or empty. For example, `lem:compact-elliptic-foundations` now has six steps; the 14-page proof of `lem:chern-joint-smoothing` has a plan and seven titled steps, with every auxiliary quantity defined at its first use; and `lem:penalized-local-regularity`, `lem:projective-simplex-fibre-formula` and `lem:penalized-real-hessian` have numbered steps with goals. Every "Step N" reference was rechecked.
- **Letters with two meanings in one proof** were renamed throughout (a few hundred renames), for example the Green operator $\mathcal G$ in Chapter 14, the eigenvalues $\lambda_i$ and difference steps $s$ in the penalized equations, and the Cauchy constants $C(r)$ next to the lattice $M$ in Chapter 18.
- **Stated once.** Facts derived two or three times are now stated once and cited, among them `eq:bt-collar-modification` (Chapter 9, now also cited in Chapter 15), `eq:blocki-capacity-bound`, `eq:trace-measure-form-comparison`, `eq:weighted-geometric-arithmetic-mean`, `eq:wedge-product-telescoping`, `eq:convex-cube-lipschitz`, `eq:penalized-distributional-trace-bound`, `eq:potential-reciprocity`, `eq:complex-line-polar-coordinates` and `lem:extrapolation-obstacle-contact`.
- **Placement.** A few auxiliary lemmas moved, within their sections, to just before their first use (`lem:difference-quotients`, `lem:sobolev-multiplication`, `lem:analytic-complement-cutoffs`). §A.1 was reordered so that analytic subsets and removable singularities follow the algebraic material they depend on. §7.1 is now titled "Complex manifolds and differential forms" (label unchanged).
- **Openings, sentences and formulas.** Chapter and section openings were updated where round 3 added material. Several hundred long paragraphs and sentences were split, and long inline formulas were displayed. Meta remarks were removed.
- **Notes.** Appendix B was tightened in the same way; plain preprint citations now say which arXiv version was used; three factual statements about the book were corrected.

## Mathematical corrections and gaps closed

No statement changed. The following gaps in proofs were closed, most of them already present before this round:
- **Chapter 1:** `lem:mollifier-density`(2) applied Jensen's inequality to a complex-valued function; it is now applied to $|v(x-h)-v(x)|$. The reason why half-open boxes generate the Borel σ-algebra is given.
- **Chapter 7:** reality of a positive current of order zero was proved only for test forms supported in one chart; a partition of unity now extends it.
- **Chapter 9:** in `thm:bt-decreasing-continuity` a bound was claimed outside $B$, where it can fail; an undefined index $j_0$ and an undeclared constant $N$ were fixed; "the compact set where $w\ne u$" became "a compact set outside which $w=u$"; the cutoff in the ball Dirichlet problem is now smooth, as the $C^2$ claim needs.
- **Chapter 12:** three local gaps (a lower bound on a compact disc, the range of a radius, a null set), a dropped step in `prop:lelong-logarithmic-growth`, and the independence of the representative in `def:divisorial-order-discrepancy`.
- **Chapter 14:** the margin induction in `lem:smooth-divisor-discrepancy-margin` did not cover a center of codimension one outside the boundary; a dropped frame argument in `lem:line-bundle-ball-frame`; a weighted norm made explicit in `lem:local-critical-gain-extension`.
- **Chapter 16:** "below $u$" is now "below $u$ quasi-everywhere, hence everywhere"; a plan sentence of the domination principle overstated what the limit gives; the Hermitian part $U$ of the matrix $U'$ in `lem:chern-joint-smoothing` is now named correctly.
- **Chapter 17:** dropping a special case had made the background-independence argument circular; the order of the argument was restored.
- **Appendix A:** $\gamma(0)\in C$ by properness; $Y$ is analytic only in $X\cap\pi^{-1}(U)$; Remmert's Step 2 needs a neighborhood of the closure; the base case of an induction in relative principalization; divisions by $W$ on the chosen polydisc in local parametrization.
- **Other dropped reasons restored by checkers** in Chapters 3, 4, 6, 15 and 18 (for example the realness of a density in Chapter 6 and "since $K$ is compact" in Chapter 18).

## Validation

- `make check`: integrity OK (27 chapter units, 61 active TeX files).
- `make audit`: 0 errors, 82 advisory warnings (label prefixes, standard theorem titles, arXiv-only entries).
- Forced build (`latexmk -g`): no unresolved references or citations, no fatal errors, no overfull or underfull boxes. Log: `research/reviews/logs/2026-10-13-proofread-round4-final-build.log`.
- Length: 952 physical pages (last printed page 938), against 934 (920) at the baseline. The growth of about 2% comes from the proof plans, the step goals and the paragraph splits; the source grew by about 1%.
- Short-page scan: pages more than a few lines short occur only before chapter and part openings and at the end of the references. Revised pages in Chapters 3, 14, 16 and 17 were inspected visually.
- Preservation against `8549555`: no label lost (1316 → 1333, the additions are new displays and lemmas), the multiset of citations with their locators is identical (218), no index entry lost (1113 → 1130), and the page-break commands are unchanged. `thm:analytic-resolution-input` and `thm:marked-order-one-input` are byte-identical, and `plan/external-inputs.json` is unchanged.

## Author decisions after the round

The author asked to keep the current order of the homepage list and to carry out the three merges proposed at the end of the round as preferred. `AGENTS.md` now says that the homepage entry keeps the position the author chose.
- **Chapter 17.** `thm:bounded-density-relative-exponential-equation` was a special case of `thm:nonpluripolar-relative-exponential-equation`, with a nearly identical coercivity argument, and was cited only in the notes. It is removed; a remark after the general theorem records that $\nu=g\,\mathrm dV$ with bounded $g\geq0$, $\int_Xg\,\mathrm dV>0$, is admissible, and the notes cite the general theorem. Its index entry moved to the general theorem, and its label was dropped from the result list of task Q11-01 in `plan/tasks.json`.
- **Chapter 4.** The exhaustion of a Borel set by increasing compact sets, which did not involve the subharmonic function, moved from `thm:subharmonic-quasicontinuity` to the end of `thm:choquet-capacitability`, with its proof. No other statement cited it.
- **Chapters 12 and 13.** `thm:multiplier-ideal-coherence` now treats a bounded pseudoconvex open set in a chart (a bounded polydisc being a special case), uses only local upper bounds of the weight, and allows a measure $\varrho\,\mathrm dV$ with $c_\varrho\leq\varrho\leq C_\varrho$. It states the evaluation bound, the Hilbert-space properties with Parseval's identity, and the generation of $\mathcal I(\varphi)$ as items (1)–(3). `lem:bounded-hilbert-ideal-generation` was generalized in the same way, and the dimension-zero cases are now covered explicitly. The proof of `lem:pseudoconvex-weighted-bergman-space` in Chapter 13 is now a citation of these results; every other citer is a special case. An independent check confirmed the generalized proofs and made three one-sentence fixes (the empty set in dimension zero, the place where the upper bound of $\varrho$ is used, and holomorphy of coefficients in dimension zero).

After the merges: `make check` and `make audit` pass (0 errors), and the forced build gives 950 physical pages (last printed page 936) with no unresolved references and no overfull or underfull boxes (log: `research/reviews/logs/2026-10-13-proofread-round4-merges-build.log`). Compared with `8549555`, the only label removed is the merged theorem's; citations with locators are unchanged and no index entry was lost.

## Caveat

These are reviews by authoring agents, not an independent certification. Builds and audits do not verify mathematics.
