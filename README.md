# Foundations of pluripotential theory

A private writing repository for Mingchen Xia's book, **Foundations of pluripotential theory**. All manuscript text, project documentation, plans, editorial records and task prompts use English. Original reference documents and bibliographic titles retain their source language. The book is in progress; the active draft now contains the first sixteen mathematical chapters and an independently reviewed appendix core.

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

The active manuscript contains the preface, global conventions, P01 (measures and distributions), P02 (harmonic functions and boundary values), P03 (subharmonic functions), P04 (energy and capacity), P05 (fine topology and balayage), P06 (Fourier energy and complex-line incidence), Q01 (complex forms, positive currents and divisors), Q02 (plurisubharmonic functions and invariant minima), Q08 (bounded Bedford–Taylor products, local capacity and homogeneous Dirichlet theory), Q03 (pluripolar sets and the plurifine topology), Q04 (weighted L2 estimates and local holomorphic extension), Q05 (Lelong numbers, multiplier ideals, strong openness and the valuative criterion), Q06 (analytic singularities, quantitative regularization and decreasing gentle approximation), Q07 (global potentials, positive classes, loci, section metrics, compact point and submanifold extension, and global analytic Bergman approximation), Q09 (non-pluripolar construction, general mass monotonicity, scalar mixed bounds, full-mass convergence, comparison, fibre integration and modification invariance), Q10 (obstacles, contact concentration, extrapolation, relative domination, model characterization, rooftop mass inequalities, multiplier-ideal envelopes and monotone/background limits), the independent core of A01 (complex spaces, normalization, proper images and relative principalization), and their historical notes. A01-04 remains unfinished; the checked Fornæss–Narasimhan external-interface proposal awaits author approval or an internal proof. Q05 and Q06 have completed their two reads but retain the unfinished A01 chapter dependency gate. Q07 has completed two full integration reads and retains the same dependency gate. Q09 remains drafting: the local construction and general mass/convergence/comparison arguments have completed two reads; positive mass implies bigness, the cohomology-valued positive-intersection interface and semantic sample coverage remain unfinished. Q10 has two reads of its envelope core, positive-mass model/rooftop unit and monotone/background calculus. Generalized singularity-constrained obstacles, regularity, relative capacities and quantitative rooftops remain unfinished. Later chapter skeletons are excluded from the printed draft. Activate each coherent chapter in `book.tex` after writing and review. The sample's `svmono[envcountsect]`, fonts, macros, index and single BibTeX bibliography are preserved; the result environments share one counter per section while retaining their individual reference types.

Mathematical completion requires complete proofs and two recorded reads. `make verify` checks repository integrity and compilation; it does not certify mathematical correctness.
