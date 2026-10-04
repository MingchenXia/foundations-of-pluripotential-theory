# Foundations of pluripotential theory

A private mathematics book for Mingchen Xia: a **systematic, self-contained prequel to Part I of Singularities in global pluripotential theory (SGPT)**. It supplies foundations used without complete proofs there, with a small amount of necessary overlap. SGPT Parts II and III are outside scope.

The book develops classical potential theory, then local and global pluripotential prerequisites, from undergraduate analysis and elementary complex analysis. The source Part I contains psh functions, non-pluripolar products, envelopes, geodesic rays and ample toric potentials. Its complete proof graphs govern which missing results enter this prequel; reproducing all its statements is not the objective.

- [Blueprint](plan/BLUEPRINT.md) and [writing sequence](plan/WRITING_SEQUENCE.md): reader, exact scope, coherent order and completion gates.
- [Part I proof-gap and overlap ledger](research/SGPT_PART_I_GAPS.md): checked source boundary, required foundations and pending audit.
- [Progress](plan/PROGRESS.md), [open tasks](plan/OPEN_TASKS.md) and [chapter map](plan/CHAPTER_MAP.md): generated from JSON, with excluded old tasks distinguished.
- [Source inventory](research/SAMPLE_COVERAGE.md), [references](references/README.md) and [scoped reviews](research/reviews): evidence and actual reading scope.

The active draft retains the classical/local complex foundations, the global Q07 core, provisional Q09–Q11 foundations, the reviewed convex Q16 unit and the analytic-space appendix core. Q09–Q11 still require a result-level overlap audit. Ample toric geometric and lattice-counting prerequisites remain to be written. Test curves, dS/I-good classification, traces, partial Okounkov bodies, b-divisors, non-Archimedean and partial Bergman applications are excluded. Prior broader drafts and review evidence remain in the private repository.

The required task count is provisional until the Part I gap audit closes. Build success and historical statement mappings are not mathematical completion. FN, remaining local mixed/equation/contact/positivity interfaces, ample toric prerequisites, source audit and whole-prequel polishing remain as scoped obligations.

```sh
make check      # Source integrity, dependencies, labels and citations
make audit      # The repository-local house writing audit
make build      # Build the active prequel PDF
make progress   # Regenerate required-scope progress and task views
make verify     # Integrity, audit and build
make release    # Rebuild a tracked source archive in an empty directory
```

Use English in the manuscript and project records; original sources and bibliographic titles retain their language. Preserve svmono, the shared theorem counters, index and single bibliography. Required tools are Python 3, GNU Make, latexmk, pdfLaTeX/BibTeX/makeindex and the template's TeX packages. `scripts/setup-cloud.sh` supplies the cloud dependencies. Work stays private; checked writing is committed and pushed regularly.
