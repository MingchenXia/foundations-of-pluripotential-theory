# LaTeX, bibliography, and final audit

## 1. Canonical project setup

The files in `assets/` are the canonical house-style starting point.
`main-template.tex` is the fixed manuscript skeleton, `cgeometry.sty`
controls packages, typography, theorem numbering, cross-references, and shared
macros, and `ComplexGeometry.bib` is the single shared bibliography database.
For a new manuscript, copy these assets automatically; never ask the user to
upload them again.

For a new paper, copy `main-template.tex` to the desired main `.tex` filename
and place the other two files beside it.  Its fixed preamble is:

```latex
\documentclass[11pt,a4paper]{amsart}
\usepackage{cgeometry}
\addbibresource{ComplexGeometry.bib}
```

The `amsart` class supplies `amsthm`, and `cgeometry` loads BibLaTeX with the
house options.  Copy all three assets exactly instead of regenerating or
selectively retyping them.

Do not load again a package already loaded by `cgeometry.sty` unless options must be passed before the style is loaded. Do not copy selected chunks from the style into the main file. For an established project, retain its local style file and make the smallest compatible change.

If a journal class or submission system prohibits custom style files or requires another bibliography toolchain, follow that external template. Use the bundled assets as the canonical source for compatible theorem, notation, citation, and prose conventions rather than forcing an uncompilable project setup.

For a new house-style project, or when the user explicitly requests standardization, end with `\printbibliography`; do not mix in `\bibliography`, `\bibliographystyle`, `natbib`, or a BibTeX workflow. If an existing project intentionally retains a different bibliography system, preserve it unless migration is in scope, and apply only the compatible prose and structural rules.

## 2. Theorem environments and numbering

`cgeometry.sty` provides a section-numbered theorem counter shared by:

```text
theorem, proposition, corollary, lemma, conjecture, question,
example, definition, condition, remark
```

It also provides an unnumbered `problem` and an alphabetically numbered `maintheorem` counter. Use these semantic environments as they stand.

Rules:

- Never encode rhetorical importance in an environment name. `keylemma`, `bigtheorem`, `technicalproposition`, and `fundamentalclaim` are forbidden.
- Do not create theorem-like environments for `claim`, `fact`, `observation`, `notation`, `setup`, `case`, or `step`. Write these as prose or proof stages.
- Ordinary `theorem`, `proposition`, `lemma`, and `corollary` environments should have no optional title. Allow a title only for a recognized historical name, a cited theorem's established name, or an explicit identification with an earlier numbered statement.
- A manuscript-specific `maincorollary` may share the `maintheorem` counter when the paper genuinely presents a lettered theorem/corollary sequence. Define it once in the preamble:

  ```latex
  \newtheorem{maincorollary}[maintheorem]{Corollary}
  ```

- Put optional theorem titles only when they carry stable mathematical information, not praise.
- Give every numbered theorem-like statement a semantic label immediately after `\begin{...}` or its optional title. Do not leave body results addressable only by their current number.
- Use `\qedhere` or `\qed` only when the display or document structure requires it; do not type ornamental end-of-proof symbols.

## 3. Macros and notation

Before adding any command:

1. Search `cgeometry.sty` for the operator, alphabet, delimiter, category, or font command.
2. Search the manuscript for an existing local command with the same semantic role.
3. Add a macro only if it is reused or prevents a genuine notational inconsistency.

Put manuscript-specific commands after the package setup and group them by role, for example:

```latex
% Analytification and distinguished subsets
\newcommand{\an}{\mathrm{an}}
\newcommand{\divv}{\mathrm{div}}

% Function spaces
\newcommand{\PSHhom}{\operatorname{PSH}_{\mathrm{hom}}}
```

Macro names should express mathematical semantics, not visual recipes. Avoid commands such as `\mybold`, `\specialspace`, or a macro used once. Do not redefine standard commands or house macros to save a few keystrokes.

Write special alphabets directly as `\mathcal{X}`, `\mathbb{R}`,
`\mathfrak{g}`, `\mathscr{L}`, and so on.  Do not define a manuscript macro
whose only effect is to apply `\mathcal`, `\mathbb`, `\mathbf`, `\mathfrak`,
`\mathsf`, `\mathscr`, `\mathds`, or another font wrapper.  Existing commands
in `cgeometry.sty` remain available for backward compatibility, but they are
not a precedent for introducing new font aliases.

The imaginary unit, the base of the natural exponential, and differential
operators are roman:

```latex
\mathrm{i},\qquad \mathrm{e},\qquad
\mathrm{d}x,\qquad \frac{\mathrm{d}}{\mathrm{d}t}.
```

The fixed style provides the aliases `\ii`, `\ee`, and `\rd`.  Use them
consistently when they improve readability, but retain italic $i$, $e$, or
$d$ when the letter is genuinely an index, variable, or coefficient.

## 4. Labels and cross-references

Use a type prefix and a descriptive hyphenated identifier:

```text
sec:, subsec:, thm:, prop:, lem:, cor:, conj:, prob:, ques:,
ex:, def:, cond:, rem:, eq:
```

Good labels:

```latex
\label{thm:homogeneous-birational-reflection}
\label{lem:smooth-uniform-twist}
\label{eq:reflection-divisorial-identity}
```

Bad labels:

```latex
\label{thm:main2}
\label{lem:technical}
\label{eq:key}
```

Use `\cref` inside a sentence and `\Cref` at its beginning. Use `\eqref` when referring specifically to an equation as an equation. Do not type “Theorem 4.3” or “the section below” when a stable cross-reference is available.

Use `$...$` for every inline formula.  Do not use `\(...\)`.  This convention
applies equally in titles, theorem statements, footnotes, and bibliography
annotations written in the manuscript.

Label displays that are cited later. Do not label every line of an aligned calculation; label the logical identity or inequality that later arguments use.

In the house style, a numbered `equation` has an `eq:` label. Use `\[...\]` or another unnumbered display for a calculation that will not be referenced.

## 5. Displays and local formatting

- Do not apply automatic 80-column wrapping to TeX source. Source line breaks should mark paragraphs, environments, list items, display structure, or deliberate logical boundaries, not merely a column count. Avoid inserting multiple source newlines inside ordinary prose when they have no effect on the typeset output.
- Use display math for mathematical structure, not to make a short formula look important.
- Align on the actual relation being compared. Do not add alignment columns solely for visual symmetry.
- Put punctuation in the surrounding sentence correctly.
- Introduce every display grammatically and explain the consequence after it when it is not immediate.
- Use `\text{...}` for mathematical conditions inside displays and ordinary prose outside them.
- Keep long proofs readable with real stages, not an excess of headings, `itemize`, or boxed formulas.
- Use `enumerate` only for genuinely parallel assertions that are referred to individually.

## 6. Bibliography policy

Treat `assets/ComplexGeometry.bib` as the shared, curated source for every
house-style paper.  Copy it into the manuscript project before adding or
changing records, and put every cited item in that project-local copy.  Never
create another `.bib` file or an inline bibliography.  When maintaining this
skill or when the user asks for the bibliography to remain available to
future papers, merge newly verified records back into the bundled asset.

Do not globally sort, reindent, normalize fields, remove the leading control data, or rename old keys merely to make this large legacy database look uniform. Add a missing record in a clearly commented project- or revision-specific block near the end, matching the cleaner local convention around it.

### Before adding or changing an entry

1. Search by citation key, author, title fragments, DOI, and MR number.
2. Determine whether the item is a preprint, a published article, an erratum, or one part of a preprint later split into several papers.
3. Verify the final publication record in MathSciNet when available; check the publisher or journal page as a second source when metadata conflict.
4. Verify that the cited result occurs in that version and record its exact locator.

### Entry standards

- Prefer the published version over arXiv whenever publication data exist.
- Retain exact author names and diacritics.
- Encode family names exactly as published.  For compound or hyphenated family
  names, add an explicit `label` author code made from the initials of all
  family-name components.  Thus `Di Nezza` has `label = {DN}`, while an entry
  by Darvas, Di Nezza, and Lu has `label = {DDNL}`.  Do not use `D` for
  `Di Nezza`.  The label field contains no year because the alphabetic style
  appends it.  Apply the same rule to analogous compound surnames.
- Use stable, meaningful keys consistent with the database. If the natural key is occupied, add a semantic suffix rather than silently changing another entry.
- Preserve useful MathSciNet fields when available: `JOURNAL`, `FJOURNAL`, `VOLUME`, `YEAR`, `NUMBER`, `PAGES`, `ISSN`, `MRCLASS`, `MRNUMBER`, `MRREVIEWER`, `DOI`, and `URL`.
- Do not keep duplicate preprint and published records unless the text genuinely cites materially different versions.
- Keep an erratum as a separate entry and cite it where the corrected assertion is used.
- If one preprint became two or more published papers, map every cited theorem to the correct published part. Do not globally replace the old key with only one part.
- If the arXiv and published texts differ materially, cite the version that actually supports the claim and locator. Keep both records only when the manuscript truly depends on both versions, and explain the distinction at the citation if a reader could otherwise be misled.
- Do not invent missing metadata. If MathSciNet or the primary source cannot be accessed, mark the entry for verification instead of guessing.
- Protect capitalization that BibLaTeX must retain with braces, including proper names and mathematical letters in titles.

### Citation placement

Put a citation immediately after the assertion it supports. Prefer pinpoint forms such as:

```latex
\cite[Theorem~5.20]{Key}
\cite[\S3, Proposition~3.1]{Key}
```

The Stacks Project is a single bibliographic work: keep exactly one `Stacks` record in the project-local `ComplexGeometry.bib`, and cite every Stacks result through the same `Stacks` key, putting the exact tag in that citation's postnote. Retain a direct link to each cited tag when the house style does so. Multiple tags may occur in the text, but they must all resolve to that one reference-list entry. Do not create a separate `.bib` entry for each tag, section, chapter, or result. A broad Stacks citation without the checked tag is insufficient when the proof needs a particular theorem.

Do not use `\nocite{*}`. Let the bibliography contain the records actually cited by the manuscript.

Bibliographic correctness has two independent parts:

1. **Metadata correctness:** the entry identifies the final publication accurately.
2. **Mathematical correctness:** the cited location proves the statement under the manuscript's hypotheses.

Check both.

## 7. Compilation and verification

Before compiling a project that uses the house assets, resolve `scripts/audit_tex.py` relative to this reference file's parent skill directory and invoke its absolute path against the changed TeX files and their project-local bibliography. Do not execute a same-named script found in the manuscript project. Pass every changed file reached through `\input` or `\include`; the script does not traverse the inclusion graph automatically. The audit detects ad hoc theorem environments, generic labels, unresolved citation keys, mixed BibTeX commands, stale arXiv-only entries requiring review, repeated words, and common AI filler. The audit is deliberately conservative: inspect warnings in context and do not rewrite a mathematically appropriate phrase merely to silence it. For an existing project that intentionally retains a different toolchain, use only the compatible checks.

Use the project's existing build command when present. If no command is documented and the project uses the house assets, compile through Biber, for example with `latexmk -pdf`, or with the explicit cycle below. For a journal-template exception, use the toolchain required by that template instead.

```text
pdflatex main
biber main
pdflatex main
pdflatex main
```

When practical, build once before editing and record any existing errors or warnings. After editing, do not attribute a pre-existing failure to the revision, but do not claim that the manuscript compiles cleanly either; report the baseline condition and whether the changes introduced any new failure.

Inspect and resolve:

- undefined citations and references;
- multiply defined labels;
- Biber data-model or inheritance warnings;
- accidental font or package substitutions;
- overfull boxes that obscure formulas or references;
- theorem counter or capitalization anomalies;
- PDF bookmarks broken by mathematics in headings.
- a stale rerun request or a `.bbl` produced from an earlier bibliography state.

Use `\texorpdfstring` when mathematical section titles need a plain-text bookmark form.

Do not add broad warning filters to obtain a clean log. Resolve the cause; preserve only the narrow warning suppression already documented in the house style.

## 8. Final audit

### Mathematics

- Every hypothesis is used or explicitly retained. Removing a hypothesis strengthens the statement and requires independent mathematical verification; never do it as a stylistic cleanup.
- Every implication has a visible reason; no adjective substitutes for an argument.
- Exceptional and degenerate cases are handled.
- Limit passages state the topology/order and justify interchange operations.
- Constants and auxiliary choices have the required uniformity.
- Every use of “fixed”, “uniform”, or “independent” records its parameter dependencies.
- Caveats about infinite values, common zeroes, separability, and the locus of validity occur at the relevant operation.

### Exposition

- The abstract states the setting, theorem, and significance without a survey.
- The introduction reaches the main result early and describes actual proof mechanisms.
- Each heading names mathematical content.
- Each paragraph performs one mathematical job.
- No repeated roadmap, canned recap, inflated claim, or ornamental conclusion remains.
- The author's concise voice and existing good passages are preserved.
- A literal copyedit has caught repeated words and small grammatical or spacing errors.

### LaTeX

- The project uses the intended `cgeometry.sty` and `ComplexGeometry.bib` files, or the required journal-template exception has been documented and only compatible conventions were imported.
- No duplicate package or existing macro has been reintroduced.
- No new command merely abbreviates a special alphabet such as `\mathcal`, `\mathbb`, `\mathbf`, `\mathfrak`, or `\mathscr`.
- No unnecessary theorem environment has been created.
- Labels are semantic and all cross-references resolve.
- Displays are grammatical, punctuated, and labeled only when useful.
- Inline formulas use `$...$`, never `\(...\)`.
- The constants $\mathrm{i}$ and $\mathrm{e}$ and differential operators
  $\mathrm{d}$ are roman; genuine variables or indices named $i$, $e$, or
  $d$ remain italic.

### Citations

- Every external dependency has a source at the point of use.
- Every locator has been checked in the cited version.
- Published versions replace stale preprints where appropriate.
- Split papers and errata are handled explicitly.
- MathSciNet metadata, DOI, journal, year, volume, issue, and pages agree.
- Every cited key belongs to the single project-local `ComplexGeometry.bib`.
- Compound surnames retain all required initials in the alphabetic label;
  in particular, `Di Nezza` contributes `DN`.

### Build

- A clean house-style baseline still completes its LaTeX/Biber build without unresolved-reference errors. Under a documented journal-template exception or pre-existing failure, the applicable build has no new failures and the remaining limitations are reported.
- The final PDF has been spot-checked at theorem statements, long displays, bibliography transitions, and page breaks in long proofs.
