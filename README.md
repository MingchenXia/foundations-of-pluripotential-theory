# Foundations of pluripotential theory

A private mathematics book for Mingchen Xia: a **systematic, self-contained prequel to Part I of Singularities in global pluripotential theory (SGPT)**. It supplies foundations used without complete proofs there, with a small amount of necessary overlap. The author also requests the foundational construction behind SGPT Example 6.1.3 and the complete proof of Theorem 1.2 of arXiv:2607.12797, on ceilings and singularity envelopes at arbitrary mass. Broader Parts II and III remain outside scope.

The book develops classical potential theory, then local and global pluripotential prerequisites, from undergraduate analysis and elementary complex analysis. The source Part I contains psh functions, non-pluripolar products, envelopes, geodesic rays and ample toric potentials. Its complete proof graphs govern which missing results enter this prequel; reproducing all its statements is not the objective.

- [Contents](plan/CONTENTS_OUTLOOK.md), [blueprint](plan/BLUEPRINT.md) and [writing sequence](plan/WRITING_SEQUENCE.md): reader, exact scope, coherent order and completion gates.
- [Part I proof-gap and overlap ledger](research/SGPT_PART_I_GAPS.md): checked source boundary, required foundations and closed source decisions.
- [Progress](plan/PROGRESS.md), [open tasks](plan/OPEN_TASKS.md) and [chapter map](plan/CHAPTER_MAP.md): generated from JSON, with excluded old tasks distinguished.
- [Source inventory](research/SAMPLE_COVERAGE.md), [references](references/README.md) and [scoped reviews](research/reviews): evidence and actual reading scope.

The completed book has eighteen chapters and two appendices, with a checked 502-page PDF and a source archive rebuilt in an empty directory with all page text matching. All 318 Part I source statements have explicit proof/overlap decisions: 123 psh, 47 non-pluripolar, 23 ample-toric, 77 envelope and 48 ray statements. The necessary definitions and foundations remain; source-native energy-metric, ray, multiplier-ideal envelope and later-volume applications stay in SGPT. Broader Parts II/III drafts and their evidence are preserved privately outside the active book. The Example 6.1.3 foundations and the arbitrary/zero-mass proof of arXiv:2607.12797v1 Theorem 1.2 are included at the author's explicit request.

All 109 required tasks have recorded verification evidence. Both actual mathematical/editorial source passes cover all 59 active TeX inputs, with complete pre-edit chapter reads and paired saved changed-unit reads distinguished explicitly. All 603 labelled results, definitions and examples have semantic attribution decisions; 73 cited source identities have exact-version, locator, normalization and proof-scope adjudications. The two registered resolution/principalization existence interfaces are the only external mathematical inputs. General singular-space FN equivalence and unused broader theory are excluded.

The [final release record](research/reviews/2026-10-05-whole-prequel-final-release.json) distinguishes direct proof reading, selected page inspection, complete raster/text comparisons, automated checks and the tracked-source empty-directory rebuild. These are authoring-agent reviews; no independent certification or direct visual inspection of all 502 pages is claimed. Build success alone is not mathematical verification.

```sh
make check      # Source integrity, dependencies, labels and citations
make audit      # The repository-local house writing audit
make build      # Build the active prequel PDF
make progress   # Regenerate required-scope progress and task views
make verify     # Integrity, audit and build
make release    # Rebuild a tracked source archive in an empty directory
```

Use English in the manuscript and project records; original sources and bibliographic titles retain their language. Preserve svmono, the shared theorem counters, index and single bibliography. Required tools are Python 3, GNU Make, latexmk, pdfLaTeX/BibTeX/makeindex and the template's TeX packages. `scripts/setup-cloud.sh` supplies the cloud dependencies. Work stays private; checked writing is committed and pushed regularly.
