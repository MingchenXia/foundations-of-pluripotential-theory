# Writing and revising a complete chapter

## Start from the book's actual state

Read the project instructions, current plan, chapter map and latest checked status. Distinguish an old historical plan from an active priority. Preserve the current checkout's user edits. Locate the actual root document and follow its active `input` and `include` graph, including nested figures and generated inputs that contribute content. A filename called `chapter_...` is not the complete chapter when it includes other files.

For a new book, settle its intended reader, prerequisites, central mathematical questions and deliverable from the request and source material. Design a dependency order and assign foundations, conventions, specialized theory, examples and historical discussion their natural homes. Ask only for missing choices that materially affect the book; proceed with independent writing work meanwhile. Do not impose a fixed number of chapters or reproduce a research paper's architecture in every chapter.

For an existing book, take the next authorized chapter from the live queue. Record the baseline and inherited build failures when practical. Read the chapter continuously, not only search results or selected theorem statements. Consult previous and following transitions and the internal inputs on which a changed argument depends. Earlier verified inputs may retain their recorded scope; do not describe a statement-level consultation as a fresh proof audit.

## Plan the mathematical change before rewriting

Use a short working map of the chapter's problem, main constructions, proof dependencies, examples and actual unresolved points. Include a first-use map of symbols and their scopes: ambient spaces, dimensions, backgrounds, measures, domains, maps and local auxiliary objects. Read introductions and theorem motivation as mathematics too. A declaration that occurs later, in an input filename, or only in the author's working context does not supply the reader's missing setup. Record which declarations carry through a section and where the setting actually changes. For each result being changed or relocated, compare:

| Item | Questions that affect the edit |
|---|---|
| Hypotheses | Which are inherited, genuinely new, or used only in one result? |
| Conclusion | Does it concern a function, scalar, measure, class or selected limit? |
| Limits | Which topology, fixed reference, normalization and uniform estimates apply? |
| Exceptions | Which infinite values, empty competitors, singular loci or dimensions affect the proof? |
| Dependencies | Is the cited input proved earlier under the needed hypotheses? |
| Status | Is this proved here, imported, conditional, disproved or still open? |

Do not turn the map into boilerplate in every statement. Its purpose is to prevent silent changes while making the text shorter.

For a moved foundation lemma, retain a stable label where possible, repair every caller, and check its new position against the entire dependency chain. A renamed chapter or merged theorem can change numbers everywhere; use labels rather than manual numbers. Preserve an old label as an alias only if the surviving assertion actually supports its callers.

## Rewrite at the right level

An opening should reveal a mathematical transition. For example, replace “This chapter collects results on trace and mass” with the concrete issue that finite linear trace does not itself control the nonlinear mass needed in the next equation. The exact statement must be supported by the book. Do not invent an obstruction merely to make an introduction sound purposeful.

Delete a repeated definition and point to its original location. Keep a changed regime explicit: passing from a Hermitian form to an arbitrary smooth background, or from a smooth density to integrable data, can change the argument. A sentence declaring the change is useful; another full preliminaries section usually is not.

Distinguish a redundant sentence from a necessary condition. “Choose u in PSH(X,theta)” already supplies nonemptiness for that assertion; an existence theorem must establish it or state the hypothesis it needs. A restriction or limit can become identically minus infinity even if the original functions were not; check that operation without restoring redundant introductory disclaimers.

Remove duplicated consequences, repeated named statements and recaps only after checking downstream references. Preserve concise existing prose and the author's local edits. Use a display for a calculation or mathematical structure, not to give a familiar short formula ceremonial prominence. Do not mechanically hard-wrap prose in TeX source.

## Integrate sources without turning the body into a survey

For each external claim that matters to the revision, identify the precise source version and locator, compare its hypotheses with the book's claim, and record what was actually read. Prefer the published version when it contains the claim; a published theorem number is not interchangeable with its preprint number. An abstract search can identify a lead but cannot verify the proof.

When papers belong in final historical notes, give the body its self-contained mathematical argument or an explicitly identified external input. Link the body result to a focused history paragraph, and link that paragraph back to the result and exact paper locator. Do not merely remove citation commands or imply that an imported theorem was proved in the book. If the author explicitly waives citations for a specified class of supplied material, apply that exception, remove obsolete citation entries and source-only recaps, and preserve citations to its independently used published dependencies. Follow the same scoped instruction about retaining original papers; review notes are distinct from paper backups. Classify a source by what it is; a book manuscript can have a `misc` bibliography entry.

Preserve the project's single bibliography and verified metadata. A new paper may settle an old problem or apply only under additional assumptions. Check both possibilities before integrating it. “Not proved in this book” is different from “open in the literature”; do not claim the latter without appropriate verification.

## First and second review

For a complete chapter revision:

1. Read every revised input from statements through proofs, checking the working map against the final prose. Compare changed claims with the original, and check the source and hypothesis distinctions.
2. Run the compatible house audit on all relevant TeX inputs, using the absolute script path resolved from the installed `mingchen-writing` skill. It does not recursively discover inputs for you. Review warnings in context rather than renaming labels or changing correct prose merely to reduce the count.
3. Build with the project's documented command. Inspect the chapter's pages and changed adjoining pages, including relocated foundations, contents, historical notes and bibliography when affected. Check figures as mathematics as well as layout.
4. Reread the complete finished chapter a second time after the first build and visual review. Check argument continuity, notation, references, redundancy, balance and the remaining research questions. This is a direct read, not a second automated scan.
5. Apply justified corrections, rerun affected audits and the full build, and inspect the final affected output. If pagination changes, follow the text across its new page range; do not reuse old page numbers without checking.

Avoid a heading stranded above two lines, a short proposition split before its conclusion, a definition separated from the display it explains, or a final page containing only an avoidable recap. Use local spacing adjustments after inspecting the output. Do not force every theorem or section onto a new page; excessive whitespace is also a defect.

Page text comparison detects content drift but does not prove layout equality. A page whose rendered image is byte-identical to a directly inspected version can carry that visual review forward. Inspect changed or new images directly and state this method accurately. Compilation, house-style warnings, mathematical review and visual review are separate checks.

## Release and continuation

Follow the project's established release requirements. For this book, a significant manuscript release includes a source archive rebuilt in a fresh empty directory, both book and companion outputs, and comparison with the checked output. Verify the archive's source payload and exclusions; exact PDF bytes may differ because of build metadata, so distinguish page-text agreement from byte equality.

Do not rerun a manuscript build for a skill-only or research-record-only edit unless it affects the build or content. Do not modify historical verifier results or describe a direct reread as an independent verification. Keep review records scoped and compact instead of appending the same checklist to every file.

Commit, synchronize and publish within the author's explicit scope. When an authorized build also updates a public book listing, keep its PDF and description together, derive the advertised extent from the author's chosen pagination convention, and verify the deployed files. A successful upload is distinct from completed website deployment, just as a successful build is distinct from mathematical review. Verify remote success before saying that work is backed up. Update the next chapter in the live queue without declaring the whole book finished. Research into new results must not displace an outstanding author-requested chapter rewrite.
