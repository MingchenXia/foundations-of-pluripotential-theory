# Foundations of pluripotential theory

A private writing repository for Mingchen Xia's book, **Foundations of pluripotential theory**. All manuscript text, project documentation, plans, editorial records and task prompts use English. Original reference documents and bibliographic titles retain their source language. The book is in progress; the active draft now contains the first three mathematical chapters.

- [Writing blueprint](plan/BLUEPRINT.md): audience, scope, two-part structure and the self-containedness contract.
- [Writing sequence](plan/WRITING_SEQUENCE.md): chapter interfaces, dependency order, source research and final completion gates.
- [Chapters and dependencies](plan/CHAPTER_MAP.md), [progress](plan/PROGRESS.md) and [open tasks](plan/OPEN_TASKS.md): JSON is the authoritative task state; the script generates the Markdown views.
- [Sample coverage matrix](research/SAMPLE_COVERAGE.md): foundations and application dependencies extracted from all sample chapters, appendices and nested inputs.
- [Source library](references/README.md): original manuscript, zip, PDFs, checksums, bibliographic identities and the actual reading scope.
- [PSHD results](research/dossiers/PSHD.md) and [quantitative Demailly regularization](research/dossiers/DEMAILLY.md): exact conclusions, proof dependencies, convention conversions and unresolved checks.
- [Cloud continuation](codex/CLOUD.md) and [first writing task](codex/FIRST_TASK.md). Both writing skills and the audit script are included in `.agents/skills/`; the skill memory's Chinese feedback has been translated into English.

Writing continues in the private repository. The JSON task records and scoped review records distinguish completed chapter work from the remaining book and sample-source audit.

## Local commands

```sh
make check      # Validate dependencies, status evidence, labels/citations and source integrity
make audit      # Run the actual mingchen-writing audit script
make build      # Run pdfLaTeX, BibTeX and makeindex; produce build/book.pdf
make progress   # Regenerate progress and open-task views from JSON
make verify     # Run check, audit and build
make release    # Verify and create source/PDF packages in build/release/
```

Requirements: Python 3, GNU Make, latexmk, pdfLaTeX, BibTeX, makeindex and TeX Live with newtx, tikz-cd, dsfont and the other template packages. `scripts/setup-cloud.sh` installs the Ubuntu dependencies. Builds do not depend on the author's local Downloads or skill installation paths; the retained references are available offline.

The active manuscript contains the preface, global conventions, P01 (measures and distributions), P02 (harmonic functions and boundary values), P03 (subharmonic functions), and their historical notes. Later chapter skeletons are excluded from the printed draft. Activate each coherent chapter in `book.tex` after writing and review. The sample's `svmono[envcountsect]`, fonts, macros, index and single BibTeX bibliography are preserved; the result environments share one counter per section while retaining their individual reference types.

Mathematical completion requires complete proofs and two recorded reads. `make verify` checks repository integrity and compilation; it does not certify mathematical correctness.
