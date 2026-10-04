# Writing blueprint

## Purpose and exact scope

Write a systematic, self-contained prequel to **Part I of Singularities in global pluripotential theory (SGPT)**. The author's 4 October 2026 clarification supersedes the earlier plan to develop all later SGPT subjects. SGPT Parts II and III are outside this book's scope. Substantial repetition of SGPT is not a goal; a small amount of overlap is permitted where a complete foundational argument or a coherent transition requires it.

The retained SGPT root actually places five chapters in Part I: `chapter_pshfunctions.tex`, `chapter_npp.tex`, `chapter_envelopes.tex`, `chapter_rays.tex` and `chapter_toric_ample.tex`, after `part_prel.tex`. Thus geodesic and ample toric prerequisites belong to the audit. Test curves, dS/I-good classification, traces, partial Okounkov bodies, b-divisors, big toric theory, non-Archimedean potentials and partial Bergman applications belong to Parts II/III and must not drive this prequel.

The unit of coverage is a missing proof or foundational dependency in SGPT Part I, not every SGPT statement. Check the complete source proof before deciding that a result needs inclusion. Distinguish a proof delegated to a reference, a missing intermediate argument, a definition requiring a construction, and a result already completely proved in SGPT. Give complete internal proofs of the first three and their prerequisite chains. Leave the fourth in SGPT, except for the limited overlap needed for a connected exposition. Automated proof-environment detection is triage, not a judgment of mathematical completeness.

## Reader and mathematical architecture

Assume undergraduate real analysis, including integration and convergence theorems, linear algebra, point-set topology and elementary one-variable complex analysis. Supply the measure regularity, distributions, functional analysis, complex differential geometry and several-variable tools actually used. Complex geometry and convex analysis are developed rather than treated as additional prerequisites.

Keep two main parts: **Potential theory**, then **Pluripotential theory**. The reader's route is:

1. Measures, distributions, harmonic/subharmonic functions, kernel energy, capacity and exceptional sets; fine topology and the Fourier/incidence tools needed for canonical psh representatives.
2. Complex forms and positive currents; psh functions and their pointwise representatives; local bounded Monge–Ampere products, nonlinear capacity and pluripolarity.
3. Weighted L2 estimates and extension, coherent multiplier ideals, Lelong theory and strong openness, analytic singularities and approximation, global potentials and positive classes.
4. Only the missing foundations for Part I's non-pluripolar products, envelopes, full-mass/finite-energy theory and geodesic constructions. The existing Q09–Q11 drafts undergo a proof-gap/overlap audit before final inclusion.
5. Convex duality, subgradient measures, lattice-volume counting and the geometric prerequisites assumed in the ample toric chapter. Do not reproduce the toric pluripotential dictionary already proved in SGPT.

An appendix supplies the complex-space and modification tools needed on this route. A final historical chapter records exact attribution and checked versions. Stable chapter IDs may survive a relocation or exclusion; they are not a requirement to print all 27 old units.

## Self-containedness and conventions

Every result used must have a complete proof, an exact earlier internal dependency, or the previously permitted exact resolution/principalization interface in `external-inputs.json`. Do not silently import weighted estimates, extension, coherence, strong openness, Siu, Bedford–Taylor, approximation, local mixed inequalities, equation solvability, metric completeness or convex measure theory. A missing proof is unfinished work.

Preserve dd^c=i/(2pi) partial barpartial, Lelong(log|z|^2)=1, multiplier weight exp(-phi), quadratic Hermitian metrics and rational analytic singularities. Keep pointwise representatives distinct from distributional almost-everywhere classes. Preserve the original psh definition and prove PSHD's redundancy theorem beside it. Check common poles, infinite values, empty envelopes, dimension zero, reference potentials, topology and uniform constants at the point of use.

The quantitative Nakamaye regularization has only its two recorded conclusions. Its foundational regularization argument is required; the full later Nakamaye application and trace/restricted-volume theory are outside this prequel. Consult the retained exact references and paired unofficial GZ errata before adopting a claim.

## Coverage, review and delivery

`research/SGPT_PART_I_GAPS.md` and its JSON ledger record the scope boundary, missing-proof candidates, confirmed gaps, internal target and overlap decision. The full source inventory is retained as evidence; Parts II/III entries are excluded from prequel completion. Historical full-statement mappings and old page counts are not a progress denominator.

Read each coherent unit completely, including its recursive dependencies and seams; perform the first mathematical/editorial read, build and visual inspection, then a second complete direct read and final affected inspection. Preserve svmono, shared counters, the index and the single bibliography. Keep editorial tracking out of the printed mathematics.

Complete the book only after the Part I missing-proof and overlap audit, every required internal proof, integration and two whole-prequel reads are finished. The current required task count is provisional until the gap audit closes. Preserve excluded drafts privately without treating them as obligations. Commit and push checked work regularly; do not publish, merge or change repository visibility.
