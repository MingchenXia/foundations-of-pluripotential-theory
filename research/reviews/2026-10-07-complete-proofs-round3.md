# Round 3: complete proofs and natural hypotheses (7 October 2026)

## Request and scope

After the two presentation rounds (`research/reviews/2026-10-06-presentation-revision.md`, `…-round2.md`, ending at commit `6e7fde0`), the author asked for three things:
- a definition of Riesz potentials, if they are used; otherwise a renamed Chapter 4;
- a complete, detailed proof in the book of every result the book mentions;
- statements given their most natural hypotheses wherever a proof uses less than the statement assumes.

The author confirmed that resolution of singularities and log principalization (`thm:analytic-resolution-input`, `thm:marked-order-one-input`, entry EI-RES of `plan/external-inputs.json`) remain the only results used without proof.

Scope: the 61 active TeX files (front matter, Chapters 1–18, Appendix A, Appendix B). Baseline: `6e7fde0` (742 physical pages).

## Decisions

- **Riesz potentials.** The phrase occurs nowhere in the body, and in modern usage it means potentials of the kernels $|x|^{\alpha-d}$. Chapter 4 is therefore renamed "Potentials, energy and capacity" (`plan/chapters.json` and the generated plan files follow).
- **What counts as proved.** A claim counts as proved if one of the following holds:
  - it has a complete proof in place;
  - an earlier result, cited by an exact `\cref`, states precisely what is used;
  - it is a reader prerequisite;
  - it is one of the two approved external inputs.

  The prerequisites are now stated precisely in the preface:
  - undergraduate real analysis, including the differential calculus of several real variables (the inverse and implicit function theorems) and Lebesgue integration with its convergence theorems;
  - linear algebra;
  - point-set topology;
  - elementary one-variable complex analysis.

  Everything else is developed in the book. This includes Fubini–Tonelli, distributions, the functional analysis for weighted and elliptic estimates, several complex variables, the commutative algebra of germs, complex differential geometry and convex analysis.
- **References inside other proofs.** A reference to a step inside another proof ("as in the proof of …") counts as proved only if the step is restated where it is used. Facts used more than once were made into labelled statements.

## Method

1. **Proof completion**, one agent per unit, 26 units. Each agent did three things:
   - It read its unit completely and listed every result that is stated, used or mentioned. This included remarks, chapter openings and facts used inside proofs.
   - It closed every gap with a complete proof, in place or as a new lemma placed before its first use.
   - It removed hypotheses that the proofs do not use, after checking every caller across the book.
2. **Independent referee**, a different agent per unit. The referee:
   - re-verified every new or expanded proof against `6e7fde0`, together with each hypothesis change and its callers;
   - checked that no other statement drifted;
   - searched the rest of the unit for remaining unproved claims.

   Appendix A was split between two referees.
3. **Final sweep**, eleven file groups. Every reference into another proof, and every reference to an unlabelled "discussion" or "remark", was classified:
   - **A, acceptable:** the step is restated, or the reference is credit only.
   - **B, short gap:** written out in place.
   - **C, reused fact:** made into a labelled statement, or added to the statement of the result whose proof contained it.

   Phrases such as "similarly", "one checks" and "the same argument" were checked the same way. A cross-file pass then turned the remaining shared facts into statements.
4. **Sweep check**, an independent referee for each sweep group and for the cross-file pass.
5. **Notes.** Appendix B was aligned with the new proofs, then checked independently.
6. **Coordinator.** The coordinator relayed cross-unit findings to the running agents. It also made small citation edits and ran scratch full builds during the round.

No external review is claimed. Builds and audits do not certify mathematics.

## Errors corrected

Unless noted, these errors were present in `6e7fde0`.

- **Ch. 1:** a false claim about the vague topology on positive Radon measures (§1.6).
- **Ch. 3:** a strict inequality in the usc-majorant lemma.
- **Ch. 4:** a false remark after `prop:kernel-energy-positivity` about total mass zero in dimension two.
- **Ch. 6:** a statement false for $d=1$ (now $d\geq2$, with the example $x_1^2-x_2^2$); wrong step pointers in a Tonelli argument.
- **Ch. 7:** a wrong constant in Step 3 of `thm:poincare-lelong`: $C_{n,n-1}$ should be $C_{n,1}$.
- **Ch. 9:** the chain rule was stated for complex functions $f$; it is now reduced to real $f$ by linearity.
- **Ch. 11:**
  - `cor:ot-point-value-bound` needed pseudoconvexity for $k=n$;
  - deleting a pointer had left a mollifier undefined (sweep).
- **Ch. 12:**
  - the Arzelà–Ascoli step of `lem:bounded-hilbert-ideal-generation` needed a doubled radius (check);
  - the Hilbert basis step needed closure under scalar multiples (check);
  - the order of $(f\circ\pi)J_\pi$ along a divisor (sweep check).
- **Ch. 14:**
  - `lem:mixed-scalar-poisson` applied a complex Hilbert-space result to a real space;
  - Step 3 of the Siu decomposition lacked a no-mass-on-$D$ argument;
  - Lelong additivity was used with possibly negative coefficients;
  - a smooth-potential lemma was applied without the required neighbourhood.
- **Ch. 15:**
  - `def:extended-psh-capacity-convergence`, `lem:extended-capacity-truncations` and `prop:psh-capacity-topologies` were stated for arbitrary open $D$, but $\operatorname{Cap}_D$ needs $D$ bounded;
  - strong positivity was needed on a neighbourhood of $K$ (check);
  - the AM–GM step missed the cases $k=0,n$ (sweep check).
- **Ch. 16:**
  - "the complex Hessian need not be bounded" is false for $n=1$; it now says $n\geq2$, with a new example `ex:metric-laplacian-unbounded-hessian`;
  - a gradient bound used an $L^p$ proposition with the wrong metric;
  - the derivative order of a remainder was off by one;
  - $C^1$ regularity was used before it was proved;
  - one wrong remark reference.
- **Ch. 17:**
  - a missing factor $\lambda$ in a first variation;
  - capacity convergence was used on a possibly unbounded open set (sweep check).
- **Ch. 18:** rationality of primitive vectors in the Delzant argument.
- **Appendix A:**
  - the cusp/node example was circular;
  - integral closedness in `lem:bounded-holomorphic-removal`;
  - field theory (splitting fields) was used without proof; `lem:finite-integral-algebra` is now proved by linear algebra only;
  - the chart description in `prop:smooth-center-blowup` was proved only near the centre;
  - a discreteness argument needed every component through a point;
  - dimension bookkeeping in the realization theorem;
  - a homotopy-lifting sketch;
  - the root identification needed in Cartan coherence, Step 4 (sweep check).
- **Duplicates removed:**
  - a Chapter 17 measure-comparison lemma now cites Chapter 16;
  - Chapter 16's chart-capacity lemma cites Chapter 15;
  - a Chapter 14 input repeated a Chapter 13 bound.

## Proofs supplied (selection)

- **Part I:**
  - Jensen's inequality, the π–λ theorem, uniqueness of measures, partitions of unity, densities of dominated measures;
  - the change of variables for image measures;
  - Lebesgue measure on products;
  - Arzelà–Ascoli;
  - the Borel structure of spaces of hyperplanes;
  - radial Laplacian and sphere-area formulas, now in statements.
- **Chapters 7–11:**
  - the holomorphic inverse function theorem (`prop:holomorphic-inverse-function`);
  - a metric on compact manifolds (`lem:compact-manifold-metric`);
  - pullback of order-zero currents (`cor:order-zero-current-pullback`);
  - mixed discriminants (`lem:mixed-discriminant-basic`);
  - the $C^2$ criterion and regularization of psh functions (`prop:smooth-psh-criterion`);
  - $\bar\partial$-closed distributions are holomorphic (`lem:dbar-closed-distribution-holomorphic`);
  - $C^{1,1}$ regularity from bounded second differences (`lem:second-difference-regularity`).
- **Chapters 12–14:**
  - the Hilbert basis theorem, Artin–Rees and Krull, all in `lem:analytic-krull-closure`;
  - orders along divisors (`lem:divisor-order-independent`);
  - basic properties of quasi-psh functions (`lem:quasi-psh-basic`);
  - existence of smooth line-bundle metrics;
  - Sobolev spaces on compact manifolds (`lem:compact-sobolev-spaces`);
  - Kähler normal coordinates, the Bochner–Kodaira identity, compactness of $L^2$-bounded holomorphic sections.
- **Chapters 15–17:**
  - restriction of positive currents to submanifolds;
  - measurable fibre families;
  - the polarized mixed gradient;
  - cutoff weights;
  - global quasi-continuity;
  - the penalized-equation theory, with frozen coefficients, difference quotients, Calabi's third-order estimate and the openness step in $H^s$;
  - a complete hand proof, for every $n$, of the Chern kernel square identity in `lem:chern-joint-smoothing`. The symbolic computations under `scripts/2026-10-06-chern-kernel-identity/`, and the referee's own computation, served only as cross-checks.
- **Appendix A:**
  - the constant rank theorem;
  - dimension bounds for images;
  - irreducible analytic sets;
  - density statements;
  - normalization, with its local construction;
  - prime divisors.

## Natural hypotheses (weakened statements, callers checked)

Each change was verified by the reviser and by the referee, including every caller across the book.

- **Ch. 1:**
  - `lem:dominated-measure-density`: any Borel measure;
  - `lem:weak-poincare-cube`: locally integrable $F$;
  - `prop:arzela-ascoli`: pointwise bounded;
  - `prop:distribution-smoothing`(1);
  - `thm:lebesgue-differentiation`.
- **Ch. 2:** nonempty bounded open sets instead of bounded domains in the Perron section.
- **Ch. 3:**
  - `lem:usc-majorants`: metric spaces;
  - `thm:subharmonic-comparison`(1);
  - `prop:subharmonic-maximum`;
  - `thm:subharmonic-distribution`(2): no local integrability;
  - `thm:riesz-decomposition`: Borel cutoffs;
  - `thm:hartogs-subharmonic`: lower semicontinuous $f$.
- **Ch. 4:**
  - `lem:gaussian-energy`, `lem:lusin-finite-measure`: no compact support;
  - `thm:potential-continuity-principle`: any compact $K\supset\operatorname{Supp}\mu$;
  - `thm:subharmonic-quasicontinuity`.
- **Ch. 5:**
  - `thm:compact-reduction`: $s$ bounded on $A$;
  - `thm:compact-balayage`: $c\geq0$;
  - `prop:reduction-order`;
  - `ex:balayage-harmonic-measure`;
  - `prop:fine-quasi-open`.
- **Ch. 6:**
  - `thm:complex-projection-l2`;
  - `thm:complex-line-incidence`: $K$ bounded;
  - `cor:borel-line-subharmonic-bound`;
  - `thm:high-value-star-energy`;
  - `prop:unitary-invariant-probability`;
  - `lem:projective-ball-volume`: $n\geq1$;
  - `lem:hessian-multiplier-kernel`(2).
- **Ch. 7:**
  - `lem:smooth-dbar-poincare`;
  - `prop:positive-hessian-holomorphic-composition`: open sets.
- **Ch. 9:**
  - `prop:bt-uniform-continuity`;
  - `lem:usc-weight-weak-limit`;
  - `cor:bt-polynomial-weights`;
  - `thm:bt-comparison`: locally bounded;
  - `cor:bt-local-domination`;
  - `lem:quasi-continuous-level-capacity`;
  - `thm:bt-increasing-continuity`;
  - `lem:constant-elliptic-upper-tests`;
  - `lem:local-comparison-capacity-sublevels`: locally bounded, real $s$;
  - `lem:bounded-psh-fixed-measure-continuity`;
  - `prop:energy-controlled-local-capacity-tails`;
  - `lem:capacity-controlled-measure-weights`;
  - `cor:mixed-products-energy-capacity-continuity`;
  - `thm:bounded-multifactor-common-measure`: Borel densities;
  - `lem:weak-derivative-zero-set` and the contact propositions: $W^{1,1}$, $W^{2,1}$;
  - `lem:bounded-psh-current-chain-rule`: $C^1$ $f$, continuous $\tau$.
- **Ch. 10:**
  - `lem:bt-superlevel-locality`;
  - `prop:finite-locus-truncation`;
  - `prop:plurifine-difference-continuity`;
  - `cor:quasi-extrema-common-poles`.
- **Ch. 11:**
  - `thm:hormander-smooth-weight`: psh, not strictly psh;
  - `thm:hormander-singular-lower-bound`;
  - `lem:bounded-weight-twist`;
  - `cor:pseudoconvex-sublevels-products`: no $s\geq0$;
  - `thm:hilbert-complex-solvability`;
  - `thm:oka-boundary-distance`;
  - `prop:logarithmic-point-interpolation`;
  - `cor:ot-point-value-bound`.
- **Ch. 12:**
  - `cor:zero-lelong-trivial-multiplier-ideal`: psh plus bounded measurable;
  - real $m>0$ in `lem:multiplier-order-lelong-bounds` and `cor:divisorial-lelong-ideal-recovery`;
  - `prop:general-necessary-valuative-bound`;
  - `lem:curve-extension-norm-lower-bound`;
  - `lem:bounded-domination-curve`.
- **Ch. 13:**
  - `thm:analytic-bounded-growth-coherence`;
  - `lem:bergman-smoothness-and-resolution`;
  - `lem:bergman-diagonal-comparison`;
  - `prop:quasi-equisingular-comparison`.

  The quantitative regularization `thm:quantitative-lower-bound-regularization` keeps exactly its two conclusions.
- **Ch. 14:**
  - `prop:smooth-target-psh-modification`: any complex manifold;
  - `cor:divisorial-logarithmic-residual`: real coefficients;
  - `lem:analytic-complement-cutoffs`;
  - Hermitian $\omega$ in `lem:kahler-bundle-l2-estimate` and `lem:twisted-kahler-line-estimate`;
  - `lem:local-critical-gain-extension`;
  - in the inputs: `thm:holder-positive-potential-extension`, `lem:hermitian-extremal-pole-alternative`, `lem:hermitian-bounded-products`(2);
  - `lem:l2-bounded-holomorphic-compactness`(2),(3): any compact complex manifold;
  - `lem:compact-section-hilbert-space`: any compact complex manifold, except the gentleness assertion, which needs the Kähler setting of `def:gentle-analytic-singularities`.
- **Ch. 15:**
  - `lem:relative-weighted-cln`;
  - `thm:compact-nonpluripolar-finiteness`: semipositive $\tau_j$;
  - `prop:auxiliary-projective-mass`;
  - `lem:projective-simplex-fibre-formula`;
  - `lem:bounded-product-fibre-fubini`;
  - `prop:positive-mixed-mass-bound`: any pseudo-effective added class;
  - `cor:relative-full-mass-capacity-convergence`;
  - `prop:nonpluripolar-multifactor-common-measure` and its corollaries;
  - `cor:weighted-nonpluripolar-capacity-limits`.
- **Ch. 16:**
  - `thm:quasicontinuous-obstacle-contact`;
  - `prop:rooftop-algebra`;
  - `prop:p-envelope-calculus`(2);
  - `thm:positive-mass-model-characterization`;
  - `prop:rooftop-full-mass-substitution`;
  - `prop:relative-capacity-sublevel-estimate`;
  - `thm:model-order-rooftop-extrapolation`;
  - `lem:global-singular-weighted-cln`;
  - `lem:full-mass-capacity-downward-comparison`;
  - `lem:chart-capacity-comparison`(3): any atlas;
  - in the inputs: `prop:metric-laplacian-regular-contact-density` ($W^{2,1}_{\loc}$), `lem:penalized-equation-trace`, `prop:penalized-envelope-uniform-limit` (every $\beta>0$), `lem:varying-log-radius-minimum`, `lem:smooth-decreasing-usc-approximation`.
- **Ch. 17:**
  - `lem:global-capacity-weighted-measure-convergence`: no quasi-continuity of $f_j$;
  - `lem:relative-cross-energy-estimate`;
  - `thm:relative-variational-characterization`: no $\nu(X)=m$;
  - `lem:nonpluripolar-measure-lower-bound-lone-limit`: no bigness;
  - `lem:relative-exponential-maximizer-equation`: any finite positive Borel $\nu$;
  - in the inputs: `lem:prescribed-density-mixed-trace`, `thm:relative-capacity-dominated-boundedness`.
- **Ch. 18:**
  - `lem:full-mass-real-measure-bounded-testing`;
  - `prop:convex-decreasing-smooth-growth-approximation`;
  - `lem:polytope-facets-and-vertex-cones`(1).
- **Appendix A:**
  - `prop:weierstrass-division`: $m\geq0$, every holomorphic $f$;
  - `lem:normal-locus-open`;
  - `thm:unibranch-connected-fibers`: $(X,x)$ irreducible;
  - `thm:divisor-smooth-blowup-realization`: compact.

## Notes (Appendix B)

About twenty descriptions now match the book, among them:
- Jensen–Lelong, which is no longer proved via Stokes' formula;
- the Chapter 17 continuity lemma, now proved by a parallelogram argument;
- strong positivity, measurability and the contact propositions;
- `lem:finite-integral-algebra`.

There are new one-sentence mentions of the π–λ theorem, Jensen's inequality, the Hilbert basis theorem with Artin–Rees and Krull, and Calabi's third-order estimate. Their locators (Tao, Lemma 35; Song–Weinkove, §2.5, p. 24) were verified in the retained sources and lie inside existing citations. No citation or locator was added or removed.

## Coordinator edits

- The preface states the prerequisites precisely.
- Chapter 14 justifies the curvature formula for every local frame, since $\log|g|^2$ is pluriharmonic.
- In Chapter 16 (main file), a Baire-category argument is replaced by the density statement of `prop:generic-divisorial-lelong`.
- Citations of `lem:mixed-discriminant-basic` are added in Chapters 9 and 18.
- Two stale pointers to a remark that became part of `lem:smooth-partition-unity` are repointed.
- One overfull display in Chapter 14 is split.
- In the Chapter 16 inputs, a long unbreakable display is split so that it no longer leaves a short page.

## Validation

- `make check`: integrity OK (27 chapter units, 139 obligations, 61 active TeX files).
- `make audit`: 0 errors, 92 advisory warnings, of the same kinds as before (label prefixes, optional standard titles, arXiv-only entries).
- Forced full build (`latexmk -g`) and `scripts/project.py check-log`: no unresolved references or citations, no fatal errors, no overfull or underfull boxes. Log: `research/reviews/logs/2026-10-07-complete-proofs-round3-final-build.log`.
- **Length.** 932 physical pages, last printed page 918; the baseline had 742 and 728.
- **Short pages.** A scan of all 932 pages finds short pages only at chapter ends, in the front matter, on part pages and in the references.
- **Visual inspection.** I inspected these pages directly: printed 172 (`lem:mixed-discriminant-basic`), 206 (`prop:smooth-psh-criterion`), 451 (`lem:compact-sobolev-spaces`), 650–651 (`eq:chern-kernel-square-identity`) and 815 (`lem:finite-integral-algebra`).
- **Preservation against `6e7fde0`.**
  - The multiset of `\cite` commands with their locators is identical.
  - No `\label` and no `\index` entry was lost.
  - No label is duplicated.
  - Labels went from 1166 to 1316, and `\index` commands from 993 to 1113.
  - The two approved input theorems are byte-identical, and `plan/external-inputs.json` is unchanged.
- **Source size.** The `.tex` sources of chapters and front matter grew from 325,764 to 422,968 words.

Builds and audits do not certify mathematics.

## Points for the author

- **External inputs.** Resolution and principalization remain the only results used without proof (EI-RES unchanged).
- **Two normal-coordinates lemmas, kept apart on purpose:**
  - `lem:kahler-normal-coordinates` (Ch. 14): pointwise existence, normalization $\frac{\mathrm i}{2}$;
  - `lem:kahler-normal-coordinates-uniform` (Ch. 16): an explicit chart with bounds uniform in the point, normalization $\frac{\mathrm i}{2\pi}$.
- **A redundant theorem.** `thm:bounded-density-relative-exponential-equation` is a special case of `thm:nonpluripolar-relative-exponential-equation`; it is kept because the notes cite it.
- **Notes section title.** The notes section for Chapter 4 keeps its title, "Energy, capacity and exceptional sets".
- **Prerequisites used without proof.** Besides the stated prerequisites, the book uses:
  - completeness of $L^p$;
  - the spectral theorem for Hermitian matrices;
  - the change of variables for diffeomorphisms;
  - Laurent expansions in one variable.
- **Round-2 author points now resolved:**
  - the Chapter 4 title;
  - the Chern kernel sketch;
  - the hypotheses listed there;
  - `cor:zero-lelong-trivial-multiplier-ideal` for quasi-psh $tu$;
  - the Lelong-number reminder before `prop:smooth-target-psh-modification`.
- **Length.** The book grew from 742 to 932 physical pages.
- **Release archive.** It has not been regenerated.
