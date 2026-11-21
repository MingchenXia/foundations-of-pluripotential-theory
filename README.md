# Foundations of pluripotential theory

A public mathematics book by Mingchen Xia: a **systematic, self-contained prequel to Part I of Singularities in global pluripotential theory (SGPT)**. It supplies foundations used without complete proofs there, with a small amount of necessary overlap. The author also requests the foundational construction behind SGPT Example 6.1.3 and the complete proof of Theorem 1.2 of arXiv:2607.12797, on ceilings and singularity envelopes at arbitrary mass. Broader Parts II and III remain outside scope.

[Read the PDF](https://mingchenxia.github.io/Papers/FPT_vibe.pdf) or [browse the shared Pome reference](https://mingchenxia.github.io/Pome/). Pome combines contributions by mathematical topic, with source attribution and a formalization status beside each tagged statement. No formalization repository has been supplied yet.

The book develops classical potential theory, then local and global pluripotential prerequisites, from undergraduate analysis and elementary complex analysis. The source Part I contains psh functions, non-pluripolar products, envelopes, geodesic rays and ample toric potentials. Its complete proof graphs govern which missing results enter this prequel; reproducing all its statements is not the objective.

- [Contents](plan/CONTENTS_OUTLOOK.md), [blueprint](plan/BLUEPRINT.md) and [writing sequence](plan/WRITING_SEQUENCE.md): reader, exact scope, coherent order and completion gates.
- [Part I proof-gap and overlap ledger](research/SGPT_PART_I_GAPS.md): checked source boundary, required foundations and closed source decisions.
- [Progress](plan/PROGRESS.md), [open tasks](plan/OPEN_TASKS.md) and [chapter map](plan/CHAPTER_MAP.md): generated from JSON, with excluded old tasks distinguished.
- [Source inventory](research/SAMPLE_COVERAGE.md), [references](references/README.md) and [scoped reviews](research/reviews): evidence and actual reading scope.

```sh
make check      # Source integrity, dependencies, labels and citations
make audit      # The repository-local house writing audit
make build      # Build the active prequel PDF
make progress   # Regenerate required-scope progress, task views and prerequisite graph
make verify     # Integrity, audit and build
make release    # Rebuild a tracked source archive in an empty directory
```

Use English in the manuscript and project records; original sources and bibliographic titles retain their language. Preserve svmono, the shared theorem counters, index and single bibliography. Required tools are Python 3, GNU Make, latexmk, pdfLaTeX/BibTeX/makeindex and the template's TeX packages. `scripts/setup-cloud.sh` supplies the cloud dependencies. The source repository is public; checked writing is committed and pushed regularly. GitHub Actions CI is currently disabled at the author's request; checks and publication are performed locally.

The [15 October integration and issue audit](research/reviews/2026-10-15-integration-issue-audit.md) records the consolidated branches, local build, and evidence supporting closure of issues #1–#4. Those issue closures rely on the retained scoped reviews and are not a new independent mathematical certification.
