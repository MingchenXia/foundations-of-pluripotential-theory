# Whole-book presentation revision, round 2 (6 October 2026)

## Request and scope

After the first round (`research/reviews/2026-10-06-presentation-revision.md`, ending at commit `be87a88`), the author asked for a second round. Round 2 read the book as one connected text rather than chapter by chapter. Its scope was the same 61 active TeX files: front matter, Chapters 1–18, Appendix A and the historical notes (Appendix B). Baseline: `be87a88` (736 physical pages). Final: 742 physical pages (last printed page 728); `make verify` passes with no unresolved references, no overfull or underfull boxes, and 0 house-audit errors (90 advisory warnings, unchanged in kind: arXiv-only entries, label prefixes, standard theorem titles).

## Method

- **Revision** (one agent per unit, 26 units, common brief): each unit was read completely in reading order, together with the end of the previous chapter, the opening of the next one and the front-matter passages describing it. The brief asked for five things:
  - cross-chapter consistency: a repeated definition becomes a reminder with an exact reference, and a term with a different meaning says so where the new meaning is introduced;
  - tightening;
  - a fresh referee check of every statement and proof;
  - a textbook finish;
  - index entries for defined notions and named results.
- **Independent check** (a different agent per unit): every changed hunk was compared with `be87a88` for mathematical drift, every reported correction was verified, and every replaced definition was checked against the earlier one.
- **Third read**: the checker of Chapter 14 replaced a construction in `lem:gentle-weighted-normal-residue`. That construction and the new shrinking step were then verified by a third agent, which made no change.
- **Coordinator**: relayed cross-unit findings between running agents and made the cross-chapter edits listed below. It aligned the front matter with the chapters, ran `make check`, `make audit` and a forced full build, scanned all 742 pages for short pages, and inspected sampled changed pages directly (5, 17, 146, 282, 399, 705).

No independent external review is claimed. Builds and audits do not certify mathematics.

## Cross-chapter consistency

- **Repeated definitions replaced by exact reminders:**
  - $B(x,r)$ and its closure, written $\overline{B(x,r)}$ throughout;
  - mollifiers, recalled from §1.4;
  - support;
  - Green energy;
  - affine complex lines;
  - upper regularization;
  - Hermitian and Kähler forms, which Chapter 7 now defines;
  - globally pluripolar sets;
  - generic Lelong numbers;
  - more singular, $\preceq$ (first in Chapter 13);
  - quasi-everywhere and quasi-continuity on $X$;
  - global convergence in capacity;
  - $\mathcal E(X,\theta)$ and $M(q)$;
  - imaginary-translation invariance;
  - Sobolev spaces.
- **Different meanings now stated where they arise:**
  - *quasi-everywhere* (polar in Part I, `def:quasi-everywhere`; pluripolar in Part II);
  - *harmonic* functions versus harmonic forms;
  - the local Monge–Ampère capacity $\operatorname{Cap}_D$ versus the global $c_\omega$;
  - the Cegrell class $\mathcal E_0(B)$ versus $\mathcal E(X,\theta)$;
  - *weight* (Chapter 11) versus plurisubharmonic weight (Chapter 12);
  - the various *competitors*;
  - *admissible* functions (Chapters 4–5) versus $S$-majorants (Chapter 17).
- **Book-wide spellings:**
  - "closed positive current";
  - "fiber" (labels unchanged);
  - "Hermitian quadratic form" for the linear-algebra sense;
  - "analytic singularities", since the definition already requires rational coefficients;
  - the Laplace–Beltrami operator $L$ with the renamed tensor Laplacians $D_g$, $\overline D_g$;
  - log resolutions as composites of blowups along closed submanifolds, in Appendix A and in Chapter 13 onwards.
- **Local letter clashes renamed:** for example $V$ for neighborhoods, $\sigma$ versus $\tau$, $M$ as a constant versus the mass $M(u)$, $\Omega=2\pi\omega\to\widehat\omega$, the lattice $M$, $\eta$ as a one-form, and $\omega$ in Part I.
- **Front matter corrected:**
  - reductions are in Chapter 5, not Chapter 4;
  - balayage preserves potentials quasi-everywhere on a compact set;
  - the role of the incidence estimate;
  - quasi-continuity is proved in Chapter 9, not Chapter 10;
  - the non-Kähler Josefson section of Chapter 14;
  - metric-Laplacian regularity of envelopes;
  - truncation levels;
  - the toric chapter's projective toric manifold and Guillemin metric.

## Errors and gaps found and corrected

Unless marked "round 2", these were present in `be87a88`.

- **Ch. 3:**
  - `prop:fundamental-potential`: the claimed finite upper bound was $-\infty$ for $\nu=0$.
  - `thm:subharmonic-distribution` is split into three items, and a proof is added that the almost-everywhere class determines a subharmonic function without any integrability assumption.
- **Ch. 4:**
  - Facts proved only inside proofs, but cited by later results, are now part of the statements (`lem:ball-green-symmetry`, `prop:compact-extremal`).
  - The graph step of `thm:choquet-capacitability` is rewritten.
  - The choice of sets in `thm:outer-capacity` is justified.
  - A hypothesis dropped from the chapter opening (round 2) was restored by the check.
- **Ch. 6:**
  - The range of $c$ in `lem:positive-circle-selection` is now stated.
  - The Fourier transform of measures is defined only where it is used.
- **Ch. 7:** "strongly positive" is restored where a step needs it (round 2, check).
- **Ch. 8:**
  - Locality of plurisubharmonicity did not cover the condition "not identically $-\infty$".
  - Only one direction of the smooth criterion was justified.
  - Plurisubharmonicity of $-\ell(\Real w)$ in `cor:kiselman-product-tube` was not shown.
  - A "logarithmic potential" in two input sections contradicted Chapter 4's definition.
- **Ch. 9:**
  - The polydisc estimate in `prop:canonical-grid-energy-control` did not cover cubes of measure zero or the unbounded limit, both of which are used (new display `eq:canonical-grid-polydisc-average`).
  - Positive definiteness was inferred from a positive determinant alone (`thm:homogeneous-ball-dirichlet`).
  - The comparison principle was applied on the wrong domain.
  - The constants in the outer-capacity part of `prop:bt-capacity-basic`.
  - The chapter opening falsely said all potentials are locally bounded.
  - Decreasing mollification was claimed for arbitrary radial kernels.
  - Undeclared symbols, and the scope of $\eta$.
- **Ch. 10:**
  - `prop:finite-locus-truncation` is now stated with outer measure.
  - A new paragraph proves that pluripolar sets are polar.
  - `ex:real-polar-not-pluripolar` is extended to all $n\ge2$ (round 2, check).
- **Ch. 11:**
  - A functional representation used later was proved only inside a proof.
  - Finiteness is now made explicit in the twist lemma.
  - A quantifier order in two limit arguments is corrected.
- **Ch. 12:**
  - `prop:generic-lelong-uniform-growth` needs a closed submanifold.
  - `prop:generic-divisorial-lelong` now also states the version for currents that Chapter 14 cites.
  - "Generic smooth point" made precise.
  - The undefined case of $\operatorname{ord}_E$ (round 2, check).
- **Ch. 13:**
  - Pointwise versus locally uniform convergence of the kernel series.
  - $E=\mathbb P(N)$ was cited to a result that does not state it.
  - Real (1,1)-forms were called Hermitian forms.
- **Ch. 14:**
  - In `lem:gentle-weighted-normal-residue`: the derivation of `eq:critical-gain-divisor-orders`; the index set for $e_D$; and the construction of an adapted resolution. That construction leaned on an unproved normal-crossing property and was replaced by one application of `thm:marked-order-one-input` (third read: correct).
  - The Fubini–Study metric is not in $\FS(L)$; the reason is now given.
  - The Euclidean form of $L$.
  - An inaccurate opening sentence (round 2, check).
  - In the inputs: the background-independence argument for Hermitian Bedford–Taylor products; the domain of the mollified functions; a Taylor-formula step.
- **Ch. 15:** the definition of positive mixed intersection numbers defined big classes twice.
- **Ch. 16:**
  - The opening of the penalized-equation section had the wrong sign: an upper bound for $\Lambda\ddc f$ is a lower bound for $L f$.
  - A maximum point was not re-chosen for the second constant in `lem:penalized-equation-trace`.
  - "$\alpha$-psh" should be "$\theta$-psh" in `thm:big-metric-laplacian-rooftop`.
  - A factor of $\mathrm i$ in $T[y]^2$.
  - A Lipschitz constant ignored the dimension.
  - Global capacity notions were used before their definition.
  - A misleading "equivalently" in `lem:chern-joint-smoothing`.
  - An unused sentence that cited the wrong result.
- **Ch. 18:**
  - The convex-hull step in `prop:convex-closure-and-dense-convergence`.
  - Curvature claimed only positive where the proofs give positive definite.
  - The order of a monomial along $D_\rho$.
  - An undeclared $P$, the dimension-zero case, closedness for a separation step, and the case $p=0$ (round 2, check and coordinator).
- **Appendix A:**
  - The hypothesis on centres in `def:adapted-blowup-modification`.
  - Simple normal crossings of the support of $H$.
  - Irreducibility of $f(E)$.
  - An unproved and unused claim is removed.
  - The reasons in the common smooth model, Remmert–Stein, the codimension-two bound and the support lemma.
  - A remark on dimensions of images replaces five ad hoc references.
  - The accumulated divisor is now defined on every $M_i$.
  - $\operatorname{ord}_af$ is defined.
- **Appendix B:**
  - Notes that misdescribed the book are corrected:
    - the sign in the Chapter 16 notes;
    - the operator facts in Chapter 11;
    - the barrier construction;
    - the Perron segment endpoints;
    - the weighted Chern–Levine–Nirenberg estimates;
    - the multiplier sign in Chapter 6;
    - "real polar".
  - Cegrell's class is now cited as \cite[Section~3, p.~161]{Ceg04}, where it is attributed to \cite{Ceg98} (checked on the retained PDF).
  - The Lamari and bigness notes are moved to Chapter 17.
  - No citation or locator was removed.

## Tightening and finish

- **Cut:** repeated explanations, opening inventories, defensive remarks and meta sentences.
- **Added:** cross-references, completed justifications and about 340 index entries (920 `\index` commands against 576).
- **Net effect:** the source grew by about 1% (301,343 to 304,557 words) and the book by six pages.

## Points left for the author

- `def:gentle-analytic-singularities`: log resolutions now mean every composite of blowups along closed submanifolds that principalizes the ideal. This is slightly wider than "maps produced by `thm:marked-order-one-input`", so the definition is a little stronger; every gentleness claim in the book still holds (checked).
- `lem:chern-joint-smoothing`: the proof of the kernel square identity is still a sketch, supported by the symbolic check (`scripts/2026-10-06-chern-kernel-identity/`, $n\le2$).
- The title of Chapter 4, "Riesz potentials, energy and capacity": the phrase "Riesz potentials" does not occur in the body, and in modern usage it usually means $|x|^{\alpha-d}$ kernels.
- The new citation `\cite{Ceg98}` has no locator; that paper is not among the retained sources, so the attribution rests on Ceg04, p. 161.
- Hypotheses stronger than the proofs use:
  - `thm:compact-reduction` (only $s\le M$ on $A$ is used);
  - `lem:global-capacity-weighted-measure-convergence` (quasi-continuity of $f_j$);
  - `cor:pseudoconvex-sublevels-products` ($s\ge0$);
  - `lem:bounded-weight-twist` ($\alpha\in L^2_{\loc}$);
  - plus those noted in round 1.
- `cor:zero-lelong-trivial-multiplier-ideal` writes $\mathcal I(tu)$ for quasi-plurisubharmonic $tu$, outside the narrowed meaning of "weight".
- `prop:smooth-target-psh-modification` uses $\nu(\varphi,E)$ for quasi-plurisubharmonic $\varphi$ before the reminder in Chapter 14.
- The backmatter order follows the original sample book (index before references).
- The release archive has not been regenerated.
