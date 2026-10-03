# Writing blueprint

## Aim and scope

Develop pluripotential theory from classical potential theory. Place the sample book's foundational definitions, results, techniques, limiting arguments and geometric prerequisites where readers first need them, and supply complete proofs. Assume undergraduate real analysis, including integration and convergence theorems, linear algebra, point-set topology and elementary one-variable complex analysis. Establish the measure regularity, distributions, functional analysis, complex differential geometry and several-variable tools actually used. Familiarity with complex geometry must not become an unstated prerequisite.

The two main parts are I. Potential theory and II. Pluripotential theory. An appendix treats complex spaces and precise external geometric interfaces; the final chapter provides historical and bibliographic notes. Chapter IDs remain stable while printed numbers follow the manuscript. Write P01–P06 first, then proceed through the complex theory along the dependency graph. The sample's chapter order does not dictate the new book's order. The full chapter sequence and its prerequisites are in [CHAPTER_MAP.md](CHAPTER_MAP.md) and `chapters.json`.

Use English for the entire manuscript and all project documentation, plans, progress records and handoff prompts. Retain the source language of original reference documents and original bibliographic titles.

## The self-containedness contract

Every result used must have a complete proof, an exact earlier internal interface, or an accepted external interface in `external-inputs.json`. Resolution of singularities and principalization are the currently permitted long external inputs, with precise statements and checked source locators still required. Assess other long, established results individually; difficulty alone does not make a result a standard input. Initially plan proofs of Hörmander estimates, Ohsawa–Takegoshi extension, multiplier-ideal coherence and subadditivity, strong openness, Siu's theorem, Bedford–Taylor theory, Demailly approximation, Monge–Ampère mass monotonicity, energy and metric completeness, and trace results.

Record any reliance on unfinished later material as a dependency and an open obligation. Do not close a proof gap with “standard arguments.” PSHD's distributional characterization must not depend circularly on its automatic upper semicontinuity theorem: first establish the locally bounded distributional case independently. Its Borel selection tools likewise need sufficient proofs, or a separately assessed external-input proposal.

## Coverage of the sample

Extract foundations from every sample chapter and appendix. `research/sample-inventory.json` records result environments, labels, locations, citations and nested inputs; `research/SAMPLE_COVERAGE.md` assigns chapter material to its natural home. Automated extraction creates a review queue and does not verify the extracted claims. Subsequently classify each item as foundational, application, duplicate or external-input candidate, and connect it to a new result label and task ID. The sample's original research results enter through foundational interfaces or advanced chapters; reproducing every research conclusion of the original book is a separate scope decision.

## Additional sources

For PSHD, retain the usual psh definition and prove the redundancy of upper semicontinuity immediately beside it. Preserve the sample's other conventions. Establish Borel measurability, uniform star energy, L2 projection onto complex hyperplanes, the incidence argument and pointwise representative identification before the final theorem.

For the Nakamaye source, place `lem:patching` and `lem:regularization` in Q06. Prove that the positivity-loss constant depends only on the fixed geometry `(Z, omega_Z)`. State quantitative regularization separately from gentle and quasi-equisingular approximation. Develop the foundations for trace, rooftop envelopes, restricted volumes and relative principalization in their corresponding chapters. The complete Nakamaye theorem is an optional application beyond this initialization's writing unit.

The remaining supplied references support the chapter tasks listed in `references/catalog.json` and the reference guide. Check each relevant Guedj–Zeriahi assertion against its exact retained version and the unofficial errata candidates before importing it.

## Rigor and delivery

A coherent unit includes all recursive inputs, definitions, statements, proofs, examples, transitions, index entries and source obligations. Review it through a first complete read, build and visual inspection, then a second complete direct read and final affected build and inspection. Set a unit to verified only when these records and its prerequisite evidence are complete. Review circular references, first use of symbols, dimension-zero cases, common poles, empty envelopes, limit topologies, uniform constants, changes of background and the actual status of open problems.

Preserve the sample's typesetting. Use one `ComplexGeometry.bib`, retain its existing keys, and add metadata only after checking it. Give exact dependencies in the mathematical text and precise attribution in the historical chapter. Keep progress and audit records in project documentation. Source files and PDFs stay in the private repository or private Actions artifacts; public publication requires a separate author instruction.

The operational dependency order and completion gates are in [WRITING_SEQUENCE.md](WRITING_SEQUENCE.md). The first four chapters are active; [PROGRESS.md](PROGRESS.md) records their actual review status and the remaining obligations. The whole book is complete only after all required proofs, semantic source coverage and final integration reviews are finished.
