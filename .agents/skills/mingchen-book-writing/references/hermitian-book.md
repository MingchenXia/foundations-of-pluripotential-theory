# Profile: non-Kähler pluripotential theory

Apply this profile only to `MingchenXia/non-kahler-pluripotential-theory`. It records the author's choices for this book, not universal requirements for every monograph.

## Find the live state

The current local repository is `/Users/mingchen/Projects/Yethlas/non-kahler-pluripotential-theory`. If it moves, identify it by its configured remote and project files rather than creating a new competing checkout. Read `AGENTS.md`, `PLAN.md`, `BLUEPRINT.md`, `research/STATUS.md`, and the active entries of the two queues in `research/editorial/`. Follow the current plan when this profile becomes stale.

The skill's maintained source is `research/editorial/skills/mingchen-book-writing/`. Its installed copy is `/Users/mingchen/.codex/skills/mingchen-book-writing/`. The base house skill remains separately maintained at `/Users/mingchen/.codex/skills/mingchen-writing/`. Do not duplicate the base assets into this skill or automatically modify them during feedback updates.

## Editorial and mathematical choices

- Preserve the supplied monograph template and the existing bibliography in `book/references.bib`. This intentional setup is not the base skill's new-paper template.
- Keep general psh foundations in the first chapter, with proofs and exact hypotheses. Replace later duplicates by internal references. Keep specialized Monge–Ampère, singularity and geometric arguments in their natural chapters.
- Keep non-book citations, exact source locators and historical attribution in the final historical chapter. Book citations may remain beside the mathematics. The history chapter should explain the relationship between results, not merely list citation keys. Exception explicitly requested on 27 September 2026: papers manually supplied by the user with no author are integrated without a paper citation or bibliography entry, including in the history chapter. Do not back up those original papers or archives to GitHub. Read them locally and keep only the scoped review records needed for the book. This exception does not apply to authored works, external published dependencies, or a merely incomplete author field in an unrelated bibliography record.
- Preserve the full singularity/I-goodness program alongside equations and Gauduchon geometry. New equation results must not turn the book into an equation survey or displace the outstanding chapter revision.
- Develop the general theory without an implicit universal mass assumption. Keep substantial bounded-mass and positive-lower-mass regimes in the designated separate part. Preserve distinctions between closed classes and nonclosed backgrounds, one reference or density and all potentials, finite trace and nonlinear mass, ordinary and ideal singularity type, and scalar uniqueness and potential uniqueness.
- Use the author's established $P_\theta[u]_{\mathcal I}$ multiplier-ideal envelope notation. Do not restore the abandoned $Q_\theta[u]$ shorthand. Keep the operator convention once in the front matter and avoid redundant introductory qualifications.
- Maintain a whole-book Introduction explaining the differences from Kähler theory through mass, comparison, energy, equations and singularities. Distinguish the background's closedness from the ambient manifold's geometry. Keep a subject index with generated page references after the bibliography; update meaningful entries when revising or adding material.

The supplied ZIP's documents require complete proof/dependency review before integration at their claimed scope. Filenames are not evidence of authorship, verification or publication. Consult the actual integration queue rather than assuming that every supplied result is pending or already settled.

Preserve the temporarily hidden Nakamaye sources, original references and historical verifier outputs. Do not reactivate a hidden chapter or infer new mathematical authority from old verifier reports. The special instruction about consulting the private working reference before any new reliance on Popovici results remains in `PLAN.md`; follow it at the relevant source use. The private working reference is not book or skill content.

## Checks and continuation

Use the established book and companion build commands and citation-placement check in `scripts/`. Resolve the house audit from the installed base skill and pass the relevant recursive author inputs. For a significant manuscript release, follow the existing source-package reconstruction procedure and preserve package exclusions. A skill-only change needs skill validation and source/installation comparison, not a new book build or a claim of a new mathematical release.

Existing private source synchronization authorization and its exact command are in `AGENTS.md`. On 30 September 2026 the author separately authorized publishing the book PDF after every successful full-book build to `https://mingchenxia.github.io/Papers/SHPT_vibe.pdf`, together with its matching homepage description. Use the build hook and publisher recorded in `AGENTS.md`, reading the final printed page number from the PDF rather than its physical page count and updating the date. Change only that PDF and description; the source repository remains private. A companion-only build or source-package reconstruction does not publish. Verify the deployed PDF and homepage, and retain/retry a locally compiled PDF if publication fails. Keep the chapter queues aligned and consult current status for the next chapter. Do not store an advancing chapter number, page count or verification count as a permanent skill rule.

When the author intervenes, apply the correction, update the relevant skill rule and editorial memory, validate, reconcile the installed copy, and record the change in the existing project history. Future writing should use the revised skill without requiring the author to repeat the same correction.
