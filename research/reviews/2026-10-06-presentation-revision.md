# Whole-book presentation revision (6 October 2026)

## Request and scope

The author asked for one revision of the whole book focused on presentation: the book should read like a normal textbook, without stiff language and without undeclared non-standard notation, and its results must be correct. The scope was every active input of `book.tex` (61 TeX files): the Introduction, Conventions and both part introductions, Chapters 1–18, Appendix A and the historical notes (Appendix B). Baseline: commit `746ef09` (512 pages). Final: 736 pages, `make verify` passes with no unresolved references, no overfull or underfull boxes, 0 house-audit errors (90 advisory warnings, down from 98: arXiv-only entries, label prefixes, standard theorem titles, the retained BibTeX setup).

## Method

- **Front matter** (coordinator): Introduction and part introductions rewritten as continuous prose with the same claims and cross-references; a book-wide Notation list added to the Conventions (indicator functions, relative compactness, closure/interior/boundary, supports, $C^k_c$, $L^p_{\loc}$, real and imaginary parts); the historical notes made a consistently numbered Appendix B.
- **First pass** (one agent per unit, 26 units): every chapter and input read completely and rewritten for textbook presentation under a common brief (voice and transitions, chapter and section openings, self-contained statements, explicit proof steps, removal of review-log language and ad hoc coinages, declaration of notation at first use in reading order, book-wide spellings, one definition of $\mathrm d^{\mathrm c}$ in Chapter 7). Every statement and proof was checked; each mathematical change was reported.
- **Second read** (an independent agent per unit): complete read of the revised unit, comparison of every changed hunk with `746ef09` for mathematical drift, verification of every reported correction, presentation fixes, a uniform pointer to the notes section at the end of each chapter opening.
- **Third read** for the one proof rewritten during the second read (`thm:analytic-bounded-growth-coherence`).
- **Coordinator**: cross-chapter consistency (terminology of currents, $\preceq$/$\sim$, Bergman spaces $\mathcal H_\varphi$, $\beta$, regular loci, `\qsup`), item references between chapters, removal of 190 page-break commands tuned for the old pagination, final build, automated short-page scan of all 736 pages and direct inspection of sampled pages (front matter, contents, chapter openings, dense proof pages, appendices).

No independent external review is claimed. The checks are reads by the authoring agents, as recorded here; builds and audits do not certify mathematics.

## Errors in the earlier text found and corrected

These were present in `746ef09` (or arose in this round and were caught by the second read, as noted):

- Ch. 1: the converse in `prop:bounded-hessian-taylor` was imprecise and lacked a gluing step.
- Ch. 2: a linearity step in `thm:perron-resolutivity` used $U_0=V_0=0$ before proving it; the exhaustion argument for Green functions; the dimension-one Green kernel.
- Ch. 3: the gluing of local representatives in `thm:subharmonic-distribution`.
- Ch. 4: the product construction in `thm:choquet-capacitability`; the capacity of balls relied on an unproved derivative-jump argument; strong subadditivity on open sets; subharmonicity of the Cantor potential was argued from ball means.
- Ch. 5: equality of a reduction with its regularization outside a polar set cited a theorem giving only a.e. equality; two comparison steps on non-relatively-compact sets.
- Ch. 6: the radii in the high-value energy estimate; convergence of truncated heat-kernel integrals; unitary invariance of normalized measures.
- Ch. 7: the spanning proof for positivity cones polarized as if forms were Hermitian.
- Ch. 8: a mean-value disc that touched the boundary circle; a Lipschitz covering radius; a strict inequality at common poles (introduced in this round, fixed in the second read).
- Ch. 9: two wrong citations; the order of the Chern–Levine–Nirenberg induction; a sign in an automorphism bound (introduced in this round, fixed in the second read); the capacity step of the bounded-density Dirichlet problem.
- Ch. 10: exceptional sets pluripolar only in balls were concluded pluripolar in $X$; a non-Borel pluripolar set in a measure statement.
- Ch. 12: a monotone convergence claimed off the unit disc; the divisorial order of a germ was ambiguous (statements of the valuative criteria adjusted); several local arguments.
- Ch. 13: a missing $\log J$ term; a point bound applied on disconnected domains; $|f|$ versus $|f|^2$; the bounded-growth coherence proof used unproved facts about uniform limits on singular spaces (rewritten and independently checked); gentle analytic singularities are now required on every log resolution, which later proofs need (a priori stronger than the source definition; a remark and a historical note record this).
- Ch. 14: local potentials claimed on every coordinate ball; Lelong numbers of a non-positive current; the elliptic lemma did not cover $D_g-\beta$ (now stated and cited); a vacuous uniqueness statement in Siu's decomposition; a residue identification left as a sketch; a covering mesh too coarse; a decreasing limit not shown to stay in $\PSH(X,\omega)$.
- Ch. 15: a definition with two possibly different values; an impossible normalization in a weighted CLN lemma; a missing null-vector argument; the direction of a potential bound and an upper bound misstated as a bound (both introduced in this round, fixed in the second read).
- Ch. 16: `lem:divisorial-envelope-closure` needed a Kähler model; `prop:global-local-capacity-equivalence` claimed more than its proof gives (now stated as proved; callers use only what remains); the Chern kernel square identity in `lem:chern-joint-smoothing` was false as printed (conjugation and a missing integration-by-parts term; symbolic check in `scripts/2026-10-06-chern-kernel-identity/`); an $L^p$ duality step not proved in the book replaced; a missing approximation step for the $W^{2,p}$ regularity of Newtonian potentials; an undefined constant.
- Ch. 17: the order of shifts in the Monge–Ampère difference identity; an induction step; the endpoint constant in the geodesic energy theorem.
- Ch. 18: very ampleness used a definition different from Chapter 14's; a subgradient step; improper Legendre transforms; a sentence relying on toric varieties of fans, which the book does not define.
- Appendix A: a local equation of order one for codimension-one branches; the hypothesis on blowup centres for disconnected submanifolds; a field-norm step in curve selection; density of the regular locus was used but not stated.
- Appendix B: about a dozen notes that misdescribed proofs or overstated sources; the Guedj–Zeriahi capacity normalization is now cited exactly. Every citation and locator of the earlier notes is preserved.

## Points left for the author

- Definition of gentle analytic singularities strengthened to every log resolution (Ch. 13); compare with the source definition (noted in Appendix B).
- `prop:global-local-capacity-equivalence` (Ch. 16) now omits the identification of zero-capacity Borel sets with pluripolar sets and of the convergence notions; a capacitability theorem for the Monge–Ampère capacity would restore it.
- The new remark in Ch. 18 cites \cite[Section 3.1]{CLS11}; the locator agrees with the source book's CLS citations but was not checked against CLS itself.
- Harmless unused hypotheses noted by readers: regularity of $D$ in `ex:balayage-harmonic-measure`, $\psi\geq0$ in Kiselman's principle, strict plurisubharmonicity in `thm:hormander-smooth-weight`, compact support in `thm:complex-projection-l2`.
- `ex:pluripolar-hyperplane-not-discrete` (Ch. 10) overlaps `prop:classical-plurifine-distinction` (Ch. 5); `thm:compact-complex-global-josefson` (Ch. 14) is not used later.
- The book grew from 512 to 736 pages, mainly because compressed proofs are now written out.
