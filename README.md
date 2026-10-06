# Foundations of pluripotential theory

A private mathematics book for Mingchen Xia: a **systematic, self-contained prequel to Part I of Singularities in global pluripotential theory (SGPT)**. It supplies foundations used without complete proofs there, with a small amount of necessary overlap. The author also requests the foundational construction behind SGPT Example 6.1.3 and the complete proof of Theorem 1.2 of arXiv:2607.12797, on ceilings and singularity envelopes at arbitrary mass. Broader Parts II and III remain outside scope.

The book develops classical potential theory, then local and global pluripotential prerequisites, from undergraduate analysis and elementary complex analysis. The source Part I contains psh functions, non-pluripolar products, envelopes, geodesic rays and ample toric potentials. Its complete proof graphs govern which missing results enter this prequel; reproducing all its statements is not the objective.

- [Contents](plan/CONTENTS_OUTLOOK.md), [blueprint](plan/BLUEPRINT.md) and [writing sequence](plan/WRITING_SEQUENCE.md): reader, exact scope, coherent order and completion gates.
- [Part I proof-gap and overlap ledger](research/SGPT_PART_I_GAPS.md): checked source boundary, required foundations and closed source decisions.
- [Progress](plan/PROGRESS.md), [open tasks](plan/OPEN_TASKS.md) and [chapter map](plan/CHAPTER_MAP.md): generated from JSON, with excluded old tasks distinguished.
- [Source inventory](research/SAMPLE_COVERAGE.md), [references](references/README.md) and [scoped reviews](research/reviews): evidence and actual reading scope.

The current draft has eighteen chapters and two appendices, with a checked 512-page PDF and a source archive rebuilt in an empty directory with all page text matching. All 318 Part I source statements have explicit proof/overlap decisions: 123 psh, 47 non-pluripolar, 23 ample-toric, 77 envelope and 48 ray statements. The necessary definitions and foundations remain; source-native energy-metric, ray, multiplier-ideal envelope and later-volume applications stay in SGPT. Broader Parts II/III drafts and their evidence are preserved privately outside the active book. The Example 6.1.3 foundations and the arbitrary/zero-mass proof of arXiv:2607.12797v1 Theorem 1.2 are included at the author's explicit request.

All 109 required tasks have recorded verification evidence. The earlier proof and source reviews adjudicated all 603 labelled results, definitions and examples and 73 cited source identities, with their exact versions, locators, normalizations and reading scopes retained. The two registered resolution/principalization existence interfaces are the only external mathematical inputs. General singular-space disc equivalence and unused broader theory are excluded.

The additional [reader-precision review](research/reviews/2026-10-05-reader-precision-round.json) is complete for all twenty chapter/appendix units. Each has two fresh complete source reads, builds and affected-page inspections. The whole-book and both part introductions now develop the mathematical questions and proof dependencies. Chapter openings, first-use notation and hypotheses have been refined, and verified result locators appear in formal citations. The active project contains 61 TeX inputs. Earlier reviews remain separate historical evidence and are not counted as fresh reads.

The [current delivery record](research/reviews/2026-10-06-reader-precision-final-delivery.json) records the whole-book checks, actual visual scope and fresh source-package rebuild. The [earlier release record](research/reviews/2026-10-05-whole-prequel-final-release.json) preserves its original scope. These are authoring-agent reviews, not independent certification. Build success alone is not mathematical verification. The source package excludes the local operational handoff log; all manuscript, bibliography and build files remain included.

```sh
make check      # Source integrity, dependencies, labels and citations
make audit      # The repository-local house writing audit
make build      # Build the active prequel PDF
make progress   # Regenerate required-scope progress and task views
make verify     # Integrity, audit and build
make release    # Rebuild a tracked source archive in an empty directory
```

Use English in the manuscript and project records; original sources and bibliographic titles retain their language. Preserve svmono, the shared theorem counters, index and single bibliography. Required tools are Python 3, GNU Make, latexmk, pdfLaTeX/BibTeX/makeindex and the template's TeX packages. `scripts/setup-cloud.sh` supplies the cloud dependencies. Work stays private; checked writing is committed and pushed regularly.
