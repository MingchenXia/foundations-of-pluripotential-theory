# SGPT Part I: foundational proof gaps and overlap control

The author's scope instructions of 4 October 2026 are controlling: this book is a systematic self-contained prequel to SGPT Part I, with limited necessary overlap. Parts II and III are excluded. The supplied root, lines 204–209, and the complete `part_prel.tex` directly checked for this decision identify **five** Part I chapters: psh functions, non-pluripolar products, envelopes, geodesic rays and ample toric potentials. There are 318 inventoried statement environments in those chapters; that is an audit queue, not 318 missing proofs.

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
| Non-pluripolar mass and positivity interfaces | Existing Q09 reads and source evidence retained; local density and positive-mass bigness remain open | Audit Q09 result by result; keep missing foundations and compress/exclude SGPT-native arguments |
| Relative envelopes, finite energy, equations and geodesic metrics | Existing Q10–Q11 scoped reads retained; contact equalities, prescribed-measure uniqueness/relative bounds remain open | Complete source proof-gap/overlap audit before final inclusion; retain only required foundational proof chains |
| Analytic spaces used by Part I | Existing A01 core reads retained; the all-point FN disc criterion remains unproved internally | Required only at exact Part I uses; no implicit approval of a new external input |

The source convex appendix's general relative-domain sum-duality and several improper-function algebra assertions are broader than the first new finite-primal unit. They remain scoped audit items; no complete-paper or complete-appendix proof claim is made.

## Excluded work and preservation

Q12–Q15 and Q17–Q19 are outside the prequel scope. Their existing files, source checks and historical reviews remain in the private repository; Q12, Q13 and Q15 are removed from the active printed root together with their historical sections. The previous broader draft can be reconstructed from `research/working-notes/sgpt-broader-draft.tex` and its preserved history input, or from commit 2b0e9a6. These files are working evidence, not a second requested deliverable.

Q16-03's advanced toric/partial-Okounkov task is excluded. Q16-02 now concerns ample toric prerequisites and lattice counting only. Q09–Q11 stay provisional pending the overlap audit because their source chapters are in Part I. The earlier 48/110 percentage and 244 full-statement mappings belong to the old broad plan and must not be advertised as current overall completion.

## Next work and completion gate

The first convex foundation unit is reviewed; its exact finite-primal scope is recorded in research/reviews/2026-10-04-q16-prequel.json. Continue the dependency-ready ample toric and lattice-counting prerequisites, and audit the five Part I proof graphs for externally delegated and incomplete proofs, starting with the earliest analytic prerequisite. Amend Q09–Q11 and their history in connected units after confirming exact missing scope. Register new required tasks when a real Part I gap is found; do not restore excluded later subjects. Completion requires every required gap and prerequisite proved, overlap decisions closed and two whole-prequel reads.
