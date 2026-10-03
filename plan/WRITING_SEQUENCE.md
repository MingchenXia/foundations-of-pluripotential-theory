# Writing sequence and completion gates

This is the operational plan for the complete 27-unit book. The chapter architecture, task graph and sample coverage queue are authoritative in `chapters.json`, `tasks.json` and `research/sample-inventory.json`; these records distinguish a source assignment from a checked proof.

## Dependency order

| Stage | Units | Interface to establish before proceeding |
|---|---|---|
| Classical analysis | P01–P03 | Radon measures, distributions, harmonic boundary theory, canonical subharmonic representatives, limits and envelopes |
| Classical singular sets | P04–P06 | Kernel energy, capacity, quasi-continuity, polar exceptional sets, fine topology/balayage, Fourier energy and complex-line incidence |
| Local complex theory | Q01, Q02, Q08, Q03, Q04 | Forms and positive currents, psh and adjacent USC proof, local bounded products/capacity, pluripolarity and plurifine topology, weighted L2 and extension |
| Geometric interface | A01, before Q05 | Complex spaces, modifications and precise resolution/principalization interfaces; prove every additional local analytic tool used |
| Singularities and global classes | Q05–Q07 | Lelong normalization, coherent multiplier ideals, strong openness and subadditivity, approximation and quantitative regularization, global positivity |
| Global nonlinear products and envelopes | Q09–Q10 | Non-pluripolar products, global mass/comparison/monotonicity and model envelopes, using the earlier local Q08 foundations |
| Energy and singularity geometry | Q11–Q16 | Energy/metric completeness, geodesics, singularity preorders, I-good volume, traces, rays, convex/toric foundations |
| Algebraic and asymptotic interfaces | Q17–Q19 | Graded series, valuations, Okounkov bodies, b-divisors, non-Archimedean potentials, Bergman/equilibrium limits |
| Final integration | H01 and all active inputs | Exact attribution, checked metadata, global notation/index/citation audit, adjoining transitions and whole-book rereads |

Within a stage, take the earliest unfinished chapter whose prerequisites are verified in the current chapter-map order. Q01 is independent of the remaining classical fine/incidence chapters after P03, but P04–P06 are written first to keep Part I coherent. A01 is physically an appendix; its proofs must be completed and available before Q05 uses them. No theorem is accepted merely because it appears in a supplied book or paper.

## Interfaces settled in the first writing pass

P01 supplies positive-functional representation and compactness without silently importing functional analysis. P02 constructs Perron solutions using continuous subsolutions, so it does not depend on P03. Its Green interface is bounded regular domains, without a symmetry claim. P03 supplies pointwise representatives and almost-everywhere envelope equality; the stronger polar discrepancy theorem belongs to P04's finite-energy/capacity argument. P04 then proves explicit ball Green symmetry, kernel energy, compact and outer relative capacity, capacitability, polar discrepancy sets and quasi-continuity. These boundaries keep the first chapters acyclic.

Q02 proves Kiselman minimum under an explicit invariant exhaustion and for product tubes. Q04 supplies the pseudoconvex boundary-distance foundation before deriving the general pseudoconvex-tube formulation. Q02 also proves extension across Hausdorff-null sets; A01 supplies the analytic dimension estimate before this is advertised as codimension-two extension. These are internal proof interfaces, not accepted external inputs.

Q08’s local bounded-product, monotone-continuity, comparison and capacity foundations now precede Q03. Q03’s Josefson and pluripolar envelope proofs require these nonlinear inputs; leaving them after Q03 would create a circular or unproved dependency. Q08 uses Q02 and local positive-current calculus only. Global positivity and non-pluripolar products remain Q07/Q09, and Q09 explicitly depends on both Q03 and Q07. Stable chapter/task IDs and all source obligations are preserved.

Q04 proves the local flat-domain extension and its submanifold integrable-germ consequence. The compact positive-metric extension and compact Bergman sequence are assigned to Q07-05, after the compact Kähler and global metric foundations; Q06 retains local Bergman approximation, patching and quantitative regularization. The compact source Hisamoto Theorem 1.4 is projective in the checked arXiv v2, whereas the sample states a compact Kähler form under a big-line-bundle hypothesis. Establish the necessary geometric scope instead of silently transferring that citation. This relocation preserves all obligations and avoids using global geometry before its definitions.

Maintain the sample's dd^c, Lelong, multiplier-weight, quadratic-metric and rational analytic-singularity conventions throughout. The Nakamaye regularization interface has exactly its two recorded conclusions; approximation properties not present in that statement require separate results. Resolution/principalization is the only initially permitted long geometric input; its exact source statements still need registration. All other listed major results require proofs unless the author grants an exact external interface.

## Source coverage and research

For each source result used, read its statement and full proof at a checked locator, convert conventions, and record the actual read scope. Search online independently when an exact dependency or bibliographic identity needs a source. Retain accessible originals with retrieval dates and checksums; keep OCR/build derivatives ignored. For each sample inventory item, classify its role and attach a task and surviving book label, or an explicit reason for exclusion. This semantic audit remains part of the unfinished book work; the initial extraction is not completion evidence. Pair every future GZ use with a scoped adjudication of the unofficial errata.

## Completion gates

Each coherent unit needs complete statements and proofs, earlier exact dependencies or approved inputs, worked examples where needed, index entries and focused historical attribution. Read every active input directly; perform the first mathematical/editorial read, build, and inspect all affected pages. Then make a second complete direct read, correct it, rebuild, and inspect the changed pages. Byte-identical page images may retain their previous visual review; record this accurately. Store review scope and logs and only then mark the task and chapter verified.

The final release requires every required task verified, every sample coverage decision resolved, no dangling mathematical interface, a complete bibliography/index and two direct whole-book reads after integration. Run integrity/audit/build checks, inspect the final PDF, rebuild the source archive in an empty directory and compare page text. Keep releases private. Compilation and automated checks do not certify the mathematical arguments.

Q05 now has complete proofs and two reads, including strong openness and the general uniform-parameter valuative criterion. Its task order places coherence before Siu, and its whole-chapter A01 dependency gate remains open. Independent Q06 research and drafting may continue using the explicitly proved interfaces; no blocked dependency is thereby marked verified.

Q06 supplies the local background and quadratic metric definitions before its global patching: smooth potentials on fixed balls, Hermitian/Kähler forms, quasi-psh/theta-psh and Kähler blowups. Q07 retains global Hodge/dd^c, cohomology, normalized compactness, cones and compact extension. Local Bergman and overlap/patching foundations precede the quantitative theorem and the quasi-equisingular sequence in the Q06 task graph. The sample bounded-growth ideal coherence foundation is explicitly assigned to Q12-01.

Q07 now has complete proofs and two full integration reads through positive classes, minimal multiplicities and loci, quadratic section metrics, compact point/Bergman approximation and arbitrary-submanifold extension for singular positive metrics. The trace equation, twisted estimate, critical logarithmic gain and resolution-based annular residue are proved internally. The complete chapter has second-read status and retains the A01/Q05/Q06 verification gate. Continue independent Q09 construction and global mass proofs using the explicitly proved interfaces; neither a projective theorem nor a globally cut-out case is silently enlarged.
