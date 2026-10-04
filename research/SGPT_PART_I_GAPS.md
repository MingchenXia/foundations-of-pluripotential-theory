# SGPT Part I: foundational proof gaps and overlap control

The author's scope instructions of 4 October 2026 are controlling: this book is a systematic self-contained prequel to SGPT Part I, with limited necessary overlap. Parts II and III are excluded apart from the author's later explicit request for the foundations of Example 6.1.3 (ex:BBJ). The supplied root, lines 204–209, and the complete `part_prel.tex` directly checked for this decision identify **five** Part I chapters: psh functions, non-pluripolar products, envelopes, geodesic rays and ample toric potentials. There are 318 inventoried statement environments in those chapters; that is an audit queue, not 318 missing proofs.

## Inclusion rule

Include a result if Part I uses it without a complete proof, or if it is needed to prove such a result from the declared reader prerequisites. Record the exact source use, the complete source proof inspected, what is missing, the new internal proof and its earlier dependencies. A statement with a complete SGPT proof is normally excluded from reproduction. Permit only the short overlap necessary for definitions, transitions or a foundational proof. A citation or absence of a proof environment does not by itself establish a gap.

## Confirmed foundations and current open interfaces

| Part I use | Evidence actually checked | Prequel home / disposition |
|---|---|---|
| Nets, subnets and convergence theorems | psh chapter opening delegates net foundations to Willard/Kelley; source preface warns that Fatou/DCT fail for general nets | P01 supplies these prerequisites; keep the exact sequence/net distinctions |
| Canonical distributional psh representatives and holomorphic pullback | psh chapter rigidity theorem and following functoriality delegate proofs to GZ, with the collapse caveat explicit | P03, Q01–Q02 and PSHD supply the analytic proofs; complete result-level mapping still needed |
| Bounded Monge–Ampere positivity, symmetry and monotone continuity | npp lines 20–61 directly read: Proposition `prop:npp:L40` delegates to GZ/CLN; Theorem `thm:contMA` delegates both proofs to GZ | Q08 construction, CLN, decreasing/weighted and increasing continuity are required; exact weighted scope must be maintained |
| Bounded fibre Fubini | complete npp lemma/proof lines 63–123 read; the source already gives the measure-kernel argument | Exclude a second full reproduction unless a specific missing prerequisite requires it; its elementary measure prerequisites remain P01 |
| Convex functions and real Monge–Ampere measures | entire 740-line convex appendix directly read; many supporting-plane, duality, regularization and Alexandrov/mixed-measure results delegate their proofs | Q16's new convex unit supplies these foundations, including measurable subgradient volume, n! normalization and vague/tight convergence distinctions |
| Ample toric geometric setup | toric chapter lines 25–113 explicitly assumes CLS11 and cites the construction/smoothness/orbit-divisor/very-ampleness results | Supply only the needed elementary geometric and lattice prerequisites; the supplied toric dictionary has its own proofs and is not to be reproduced wholesale |
| Toric dimension lattice counts and volume limit | complete toric corollary proof lines 878–964 directly read; both count limits and volume continuity are delegated to appendix results | Q16-05 supplies complete elementary convex-body proofs; the source corollary proof is left in SGPT |
| Exact Guillemin reference metric and character basis | source line 184 delegates entropy/Legendre smooth positive extension; line 664 delegates the global character basis | Q16-02 now proves both internally, including all corners and degree zero; no replacement metric or general classification is substituted |
| Non-pluripolar mass and positivity interfaces | Existing Q09 proof/source reads retained; scalar mixed numbers and trace-mass bounds are internally proved; positive-mass bigness remains open | Retain the required scalar interfaces; the unused general cohomology-valued positive-intersection obligation is excluded by the recorded scope audit; continue source overlap review |
| Relative envelopes, finite energy, equations and geodesic metrics | Existing Q10–Q11 scoped reads retained; contact PDE interfaces remain open; prescribed-measure uniqueness now has an internal one-set concentration proof; the Lp relative bound now has an internal capacity proof | Complete source proof-gap/overlap audit before final inclusion; retain only required foundational proof chains |
| Analytic spaces used by Part I | Existing A01 core reads retained; the all-point FN disc criterion remains unproved internally | Required only at exact Part I uses; no implicit approval of a new external input |
| Compact complex-manifold Josefson | complete psh chapter first pass, line 224: delegated to Vu19; the existing proof is Euclidean | New Q07-07; retain the arbitrary compact complex scope until the source proof is checked |
| Analytic bounded-growth ideal coherence | complete psh proof at lines 1494–1511 replaces the sheaf by a proper direct image without a coherence argument | New Q06-06; only this missing foundation returns from the old Q12 obligation |
| Strict potential extension from a submanifold | psh theorem line 1550 delegates the Hölder-exponential and analytic-preserving potential extension to DRWNXZ | New Q07-06; existing OT section extension is a separate result |

The source convex appendix's general relative-domain sum-duality and several improper-function algebra assertions are broader than the first new finite-primal unit. They remain scoped audit items; no complete-paper or complete-appendix proof claim is made.

All 1,987 saved lines of the psh chapter, including its 123 statement environments and complete displayed proofs, have now received a complete first source read. The scoped record is research/reviews/2026-10-04-psh-source-audit.json. This does not close every target-proof or overlap decision. Its codimension-two direction-projection step and its Lelong-additivity argument need foundational justifications; Q02/A01 and Q05 already contain independent mechanisms at their recorded scopes. The finite analytic multiplier criterion must include strict transforms, as the existing Q05 example checks. The plurifine section mostly supplies its own proofs and must not be duplicated wholesale. The three newly confirmed omissions bring the provisional required count to 85, with 52 reviewed obligations verified.

## Excluded work and preservation

Q12–Q15 and Q17–Q19 are outside the prequel scope. Their existing files, source checks and historical reviews remain in the private repository; Q12, Q13 and Q15 are removed from the active printed root together with their historical sections. The previous broader draft can be reconstructed from `research/working-notes/sgpt-broader-draft.tex` and its preserved history input, or from commit 2b0e9a6. These files are working evidence, not a second requested deliverable.

Q16-03's advanced toric/partial-Okounkov task is excluded. Q16-02 now concerns ample toric geometry; its lattice-counting obligation is separately closed as Q16-05. Q09–Q11 stay provisional pending the overlap audit because their source chapters are in Part I. The earlier 48/110 percentage and 244 full-statement mappings belong to the old broad plan and must not be advertised as current overall completion.

## Next work and completion gate

The convex, lattice and elementary ample toric units are reviewed; their exact scopes are recorded in research/reviews/2026-10-04-q16-prequel.json, research/reviews/2026-10-04-q16-lattice.json and research/reviews/2026-10-04-q16-toric.json. Continue auditing the five Part I proof graphs for externally delegated and incomplete proofs, starting with the earliest analytic prerequisite. Amend Q09–Q11 and their history in connected units after confirming exact missing scope. Register new required tasks when a real Part I gap is found; do not restore excluded later subjects. Completion requires every required gap and prerequisite proved, overlap decisions closed and two whole-prequel reads.

## Complete ample toric first pass and compact interfaces

All 1,127 ample toric source lines and 23 environments have a complete first-pass record in research/reviews/2026-10-04-toric-source-audit.json. Q16-06 supplies the finite compact-domain envelope and full-mass bounded-testing interfaces, with its scoped verified proof record in research/reviews/2026-10-04-q16-compact.json. Geometry, the exact reference metric and lattice prerequisites already have internal proofs; the source toric applications are retained. Two local Yao chart/band corrections and its earlier global interfaces remain in the result-level audit. Two of the five source chapters now have complete first passes; npp, envelopes and rays remain. Current provisional scope is 53 verified among 86 required, not an overall completion percentage.

## Complete non-pluripolar first pass and precise PDE gates

All 1,506 npp source lines and 47 environments have a complete first-pass record in research/reviews/2026-10-04-npp-source-audit.json, bringing explicit complete chapter records to three of five. The three delegated envelope regularity scopes and their contact-density consequences are already included in Q10-02; they are not accepted external inputs. Bounded complex-Hessian regularity must not be confused with full real C1,1. Q08-05 now supplies weak zero-set/Hessian locality and regular contact densities. Compact slicing needs a declared bounded representative at common poles; local theta-balayage needs smooth-potential oscillation control, already supplied in Q10. General contact needs a sufficiently positive background shift. The pseudo-effective envelope identity still needs its exact boundary argument. The new elementary Q08-05 is separately registered; current scope is 54 verified among 87 provisionally required obligations.

Exact DNT arXiv:1912.12720v1 was independently found online and completely read; original pp. 1,3–5,7 inspected. Its C1,bar1 definition is continuous with bounded metric Laplacian. The global metric elliptic W2,p/determinant foundation is now internally proved in P06-05 and the Q10-02 subunit; envelope PDE regularity remains separate. Non-qpsh barriers need not have bounded complex Hessians or become psh after a large smooth background shift. General contact must retain the intermediate regular envelope; its shifted-psh property makes the polynomial passage applicable. Q08-05 supplies weak contact locality and the Euclidean bounded-Laplacian W2,2 foundation.

## All five Part I source chapters have complete reading evidence

The ray chapter's entire 1,610 lines/48 environments were directly read in this pass; record research/reviews/2026-10-04-rays-source-audit.json. The envelope chapter's earlier contiguous 2,458-line/77-environment reads are consolidated honestly in research/reviews/2026-10-04-envelope-source-read-consolidation.json; this is not a fresh full read. Together with the psh, npp and ample toric records, all five source chapters now have complete first-read evidence. The exact target/dependency and overlap audit remains open; first-read completion is not proof completion.

The ray source quotes non-pluripolar bounded-difference integration by parts and plurifine maximality/vanishing. Q11 has internal alternatives. Its infimum-slope assertion omits the parallel proof, supplied internally. Most ray/metric applications have complete native proofs. The source theorem labelled d1raycomplete asserts a metric, not chordal completeness. Arbitrary-base parallel isometries, chordal completeness and finite-energy meet/complete-rooftop extensions are unnecessary at the checked Part I uses; remove their active Q11 continuation after closing exact active callers. Preserve the broader private draft.

The ray continuation has now been removed from the active prequel after exact caller review. Only the missing infimum-slope proof and the new Cs/T cutoff comparison remain in Q11-04; the complete prior Q11 is preserved privately for excluded callers. Scoped review: research/reviews/2026-10-04-q11-ray-pruning.json. The remaining energy/geodesic/metric overlap is still provisional.

The complete source-native energy-metric unit is now removed from active Q11 after exact caller review; Q11-03 is excluded rather than verified. Its only task callers are excluded Q12/Q15. Shared energy tangent bounds and variational equations remain required under Q11-01. The model-density/contact/PDE prerequisite remains open independently in Q10-02. Review: research/reviews/2026-10-04-q11-metric-pruning.json. The broader private Q11 preserves the full old proof chain.

The metric-Laplacian W2,2 and regular mixed contact-density foundation has two scoped direct reads: research/reviews/2026-10-04-q10-metric-contact.json. Two cutoff levels avoid assuming weak first derivatives; positivity and the metric trace identity bound complex coefficients for regular psh potentials. General non-psh barriers need only their contact-restricted determinant here. The stronger global W2,p and signed determinant assertion is now supplied by the new Fourier/compact-inverse subunit. All envelope PDE scopes, arbitrary irregular psh contact and earlier gates remain open.

The global all-finite-p metric-Laplacian and signed barrier determinant foundation now has two complete scoped reads: research/reviews/2026-10-04-p06-q10-lp.json. P06-05 proves the harmonic-analysis prerequisites internally, with verified earlier dependencies. Q10-02 retains the exact envelope PDE and arbitrary irregular-contact obligations. Current provisional required count is 87, with 55 verified; the whole overlap audit and book polishing remain open.

## Local Lp foundation and relative capacity iteration

The exact Part I psh delegation prop:pshlocLp, lines232–243, now has a complete internal proof in Q02-05: cutoff Riesz decomposition, coordinate-by-coordinate integration, an L1-selected center and Holder interpolation. The GZ1.48 finite-p proof Steps1–2, printed30–32, were read with C1-M19 and original images. The false truncation equality is adjudicated; gradient claims are not imported. The global normalized norm bound is derived in Q07.

Q11 now proves bounded relative type under superlinear capacity domination, allowing a residual a mu_phi term with a<1. Summable geometric steps replace the quoted iteration lemma. Explicit finite-moment and energy bounds are included. The Lp-density corollary retains capacity domination; the missing volume-to-capacity estimate and unweighted uniqueness remain. Review: research/reviews/2026-10-04-q02-q11-capacity.json. Q02-05 has verified earlier gates; Q07/Q11 retain theirs. Current scope56 verified among88 provisional required tasks, with30 historical exclusions.

## Author-requested exception: Example 6.1.3

The author explicitly adds the foundations of the comparison chapter's Example 6.1.3, labelled ex:BBJ, source lines 339–343. Root inclusion order and the original class's separate section-local example counter identify this as the third example in Section 6.1, rather than its third shared theorem environment. Only this example's foundational chain returns: P04 constructs a binary polar Cantor set and an atom-free probability measure whose own potential is minus infinity on every support point; Q05 derives trivial multiplier ideals at every real positive scale from zero Lelong numbers; Q09 constructs the normalized spherical potential, identifies point masses with Lelong numbers and calculates zero first-degree non-pluripolar mass. The former fine-topology Cantor example now uses this same construction.

P/I preorder comparisons, dS and the broader excluded Q12 remain in SGPT. The exception is registered separately in the JSON ledger so it cannot silently expand the Part I inventory or reinstate all Part II obligations. The Carleson p.31 source cited by SGPT was not obtained; an explicit internal construction replaces that input. Review: research/reviews/2026-10-04-example613.json.


## Uniform exponential input and the Lp density bound

Q02-06 proves the exponential input from the earlier cutoff Riesz decomposition, Jensen and complex-line polar integration. Q07 derives a uniform bound over normalized global theta-psh potentials. The positive-mass model compact envelope in Q10 then gives an exponential volume-to-capacity estimate and all-power domination for Lp densities. This closes the extra capacity hypothesis in the earlier Q11 density corollary, with mass and residual-term constants explicit. The earlier conditional checkpoint above is superseded at this exact scope. General prescribed-measure uniqueness, local mixed inequalities, envelope PDE/contact gates and final overlap/polishing obligations remain. Scoped source and proof review: research/reviews/2026-10-04-uniform-exponential.json.

## Continuous-density prerequisite for the mixed inequality

Q08-06 now supplies the positive-semidefinite matrix formulas, upper-test characterization, internally proved constant elliptic distributional bridge and bounded mixed lower bound for continuous Lebesgue densities. This is a recursive prerequisite to the delegated thm:Yau_rel uniqueness proof, not the general common-measure theorem itself. Exact EGZ/Dinew first preprints and published metadata were checked; no quoted local Dirichlet, energy or stability result is adopted. Review: research/reviews/2026-10-04-q08-mixed-continuous.json. Current provisional scope59/92 verified, with30 historical exclusions.

## Continuous-density Dirichlet prerequisite

Q08-07 proves the local ball equation for continuous nonnegative density and continuous boundary value, the bounded-subsolution envelope, root-density stability with the boundary error, and C1,1 regularity for C2 root/boundary data. Its proof uses exact-center automorphisms and the earlier internal linearization/Taylor foundations. Exact GZ printed143–149 was paired with C5-M16/M17/M18/M19; no Dirichlet result is imported. Two scoped reads and final437-page evidence: research/reviews/2026-10-04-q08-dirichlet.json. Current provisional scope60/93 verified, with30 historical exclusions. Measurable/common-measure approximation, unweighted relative uniqueness, earlier FN/PDE/positivity gates and the whole PartI overlap/polishing audit remain open.

## Bounded-measurable Dirichlet prerequisite

Q08-08 supplies the bounded-measurable local ball equation, exact envelope/uniqueness and common-bound L1/local-capacity stability. This closes the bounded-density existence prerequisite of the general canonical-measure approximation, whose nonuniform energy/stability estimates remain required. Exact GZ5.17/5.18 proofs and original printed150–151 images checked. Review:research/reviews/2026-10-04-q08-measurable.json. Current provisional61/94 verified,30 historical exclusions; general common-measure mixed inequalities, relative uniqueness and earlier FN/PDE/positivity/overlap/polishing gates remain open.

## Author-requested addition: arbitrary-mass ceiling identity

The complete proof of Theorem1.2 of exact arXiv:2607.12797v1 is now a separate required task, Q11-05. It follows internal bounded-density variational existence in Chapter17. A single perturbation family, a uniform normalized mixed tail bound, rooftop contact and full-mass comparison prove convergence even at zero mass. A direct ceiling-competitor argument and envelope monotonicity then prove both requested identities. No ceiling regularization calculus or general-measure uniqueness is imported; the paper's other results and broader SGPT comparison/dS chapters remain excluded. Earlier Q09/Q10/Q11 verification gates remain. Scoped review:research/reviews/2026-10-04-q11-ceiling.json.

## Canonical grid energy prerequisite

Q08-09 closes the bounded-subsolution moment criterion and its preservation under cube averages for the local mixed/uniqueness prerequisite. It gives uniform solution energy moments and full-ball L1 subsequential compactness. Self-integral convergence, capacity convergence and the limiting equation remain open. Review:research/reviews/2026-10-04-q08-energy-moments.json. Current provisional scope62/96 verified,30 historical exclusions.

## Canonical self-integral prerequisite

Q08-10 closes fixed-measure continuity and the canonical moving-measure absolute self-integral convergence in the bounded-subsolution/compact-support regime. These are recursive prerequisites of local mixed inequalities and relative prescribed-measure uniqueness. No equation stability imported. Review:research/reviews/2026-10-04-q08-grid-convergence.json. Current provisional63/97 required tasks verified,30 historical exclusions. Capacity/limit-equation and the earlier book gates remain.

## Canonical capacity prerequisite

Q08-11 closes local outer-capacity convergence and the finite-mass/total-variation estimate for bounded truncations of the canonical limit. It uses the earlier self-integral result and strict shifted comparison, with only second moments. The limiting boundary trace and equation still need the bounded-subsolution comparison. Review:research/reviews/2026-10-04-q08-grid-capacity.json. Current provisional64/98 verified,30 historical exclusions; mixed/uniqueness and earlier gates remain.

## Compact-measure local equation prerequisite

Q08-12 closes the limiting equation and zero boundary trace in the compact-support bounded-subsolution ball regime. It also proves the exact pointwise envelope, uniqueness and full canonical-sequence L1/capacity/self-integral convergence. Review:research/reviews/2026-10-04-q08-subsolution.json. Current provisional65/99 required tasks verified,30 historical exclusions. Mixed energy, general common-measure inequality, relative uniqueness and earlier book gates remain.

## Mixed truncation-energy prerequisite

Q08-13 closes the bounded local mixed-energy estimate and energy-controlled mixed-product continuity with bounded limits. This supplies the canonical mixed-limit step for the general common-measure inequality required by SGPT PartI relative uniqueness. Review:research/reviews/2026-10-04-q08-mixed-energy.json. Provisional66/100 required tasks verified,30 historical exclusions; general mixed inequality/relative uniqueness and earlier book gates remain.

## General local mixed inequality prerequisite

Q08-14 closes the bounded common-Radon-measure mixed and sum inequalities, with all grid solvability/energy/stability inputs proved internally. This is the local input for the non-pluripolar relative uniqueness foundation. Review:research/reviews/2026-10-04-q08-common-measure.json. Provisional67/101 required tasks verified,30 exclusions; non-pluripolar extension, unweighted relative uniqueness and earlier book-wide gates remain.

## Non-pluripolar mixed bounds and unweighted uniqueness

Q09-06 passes the internally proved bounded common-measure inequality through strict finite-level restrictions. Domination forces both densities to vanish on the local pole union, allowing an arbitrary common reference measure. Positive multilinearity supplies the convex-combination lower bound. Q11-06 combines that bound with earlier arbitrary non-pluripolar existence: one auxiliary solution concentrates its whole positive reference mass on a strict comparison set. Full-mass comparison and the first-order convex coefficient ratio contradict nonconstant difference. A null distribution level justifies dominated convergence, and two-way domination gives pointwise equality up to a constant. These proofs complete the delegated uniqueness foundation of source thm:Yau_rel, with positive reference mass retained. They do not add source-native ray or metric applications.

Complete original BEGZ Proposition1.11 p211 and DDNL2018 Theorem4.29 pp2079–2080 proofs/images were checked. The latter source assumes small unbounded locus; our proof uses the earlier internal arbitrary-model interfaces. Review: research/reviews/2026-10-04-q09-q11-uniqueness.json. Earlier FN/positivity/envelope PDE and final source-overlap/polishing gates remain.

## Strictly positive submanifold potentials

Source CT-thm-refined at psh line1550 delegates potential extension to DRWNXZ Theorem6.1. Q07-06 now supplies its complete proof, with exact restriction and a strict ambient curvature margin. The earlier normal-pole construction, explicit block positivity, logarithmic sum and Holder projection estimate justify a fixed-index maximum glue. Rational analytic singularities with bounded remainder are preserved. The proof also gives continuous potentials off the submanifold and Holder exponentials, and handles Y=X and a point separately. It adds none of the source paper's Okounkov/volume applications. Review:research/reviews/2026-10-04-q07-potential-extension.json. Earlier verification gates and global Josefson remain open.

## Scalar-mass scope and final-audit dependency repair

The scoped audit in research/reviews/2026-10-04-prequel-scope-dependencies.json removes only the unused general higher-degree cohomology-valued positive-intersection obligation. Q09-02 is second-read on its retained complete proof reviews, behind Q09-01; the explicit SGPT positive-mass bigness gap remains Q09-04. H01-01 now depends on the nine required mathematical terminal tasks rather than excluded Q19 tasks. Their ancestor closure covers all 100 required mathematical obligations. No mathematical statement, manuscript page or whole-book completion gate changes.
