# Writing and proof architecture

This is a house style for research mathematics. Its governing principle is economy under full logical accountability: say exactly what the proof needs, at the place where the reader needs it, with no prose added merely to sound polished.

## 1. Build the introduction around the theorem

A strong introduction normally proceeds in the following order, omitting any item that the paper does not need:

1. Fix the setting and the indispensable notation.
2. State the central property or problem precisely.
3. Separate what was known from what remains open, using pinpoint citations.
4. State the paper's purpose in one direct sentence.
5. Give the main theorem early.
6. State the theorem's true scope: hypotheses removed, dimensions or characteristics covered, and limitations that remain.
7. Record the main formal consequence, proving it immediately in prose if the proof is genuinely one line.
8. Identify the concrete mathematical obstructions. Each obstruction should be an actual failed implication, missing estimate, bad functoriality, singularity issue, or limiting problem.
9. Explain the proof as a dependency chain. Name the construction or invariant that resolves each obstruction and point to the internal result where it is established.
10. Place related work by topic and mathematical relation, not as a list of names.
11. Give a short organization paragraph and precise conventions only if they save repetition later.

Do not begin with a universal-history paragraph or broad claims about the importance of the field. Do not announce the same theorem three times in different language. The roadmap should reveal why the proof works, not merely say that each section proves its title.

Keep global preliminaries minimal. Package repeatedly used external facts into a proposition or other standard interface, with sources recorded item by item. Introduce specialized background used only once—such as one test-ideal construction or one subintegral-extension fact—near the proof that uses it.

### Abstract

Use one concise, clear paragraph whenever possible.  Its reader should be able
to identify the setting, theorem, and mathematical consequence without
consulting the introduction.  Include only:

- the exact setting;
- the main result;
- the named conjecture or gap it resolves, if applicable;
- the sharp consequence or converse that explains significance.

Mention the proof mechanism only when it materially distinguishes the result.
Exclude literature surveys, section-by-section narration, undefined notation,
secondary lemmas, repeated versions of the theorem, and promotional
adjectives.  During the automatic second pass, rewrite the abstract after the
body is stable and remove every sentence that does not identify the setting,
result, mechanism, or sharp consequence.

Do not spend abstract space listing hypotheses that are absent when the main
statement can express its scope positively.  In the introduction, mention a
removed hypothesis once when it identifies the precise advance over prior
work; thereafter let the theorem statement carry its own scope.  Repeat the
absence of a hypothesis only at a proof step where that absence creates a
specific mathematical obstruction.

## 2. Use result environments to encode logical status

Choose the environment from the role of the statement:

- **Definition:** a concept reused later and worth naming.
- **Lemma:** an instrumental result whose purpose is mainly downstream.
- **Proposition:** a substantial intermediate result or reusable package.
- **Theorem:** a primary result of a section or of the paper.
- **Corollary:** a formal or short consequence of an earlier result.
- **Remark:** genuinely useful context, limitation, comparison, or warning that does not belong in the proof.
- **Example:** an object that tests or illuminates a definition or statement.
- **Conjecture:** a precise open assertion, with its status and source made clear.
- **Question:** a genuinely interrogative mathematical problem that is not being asserted.
- **Problem:** an unnumbered standalone research problem when numbering and later citation are unnecessary.
- **Condition:** a reusable named hypothesis or package of hypotheses, not an ordinary sentence beginning with “assume”.

Do not promote an estimate to a named “key lemma” merely because it is important. Importance belongs in the mathematical dependency graph, not in an ad hoc environment name. Do not demote a multi-use structural result to an inline claim if later arguments depend on it.

State each result so that it can be read independently at its point of use:

- make quantifiers and ambient categories explicit;
- distinguish “for every”, “there exists”, and “after replacing”;
- include normality, projectivity, characteristic, positivity, and regularity hypotheses when used;
- define nonstandard symbols before the statement or locally within it;
- avoid proof language in the statement unless it specifies a canonical construction.

Ordinary results should normally have no optional title. Permit a title only for a recognized historical name, the name of an imported theorem, or an explicit declaration that the body theorem is the theorem already stated in the introduction. Never attach “Key”, “Crucial”, “Fundamental”, “Master”, “Powerful”, or “Main technical” to manufacture importance.

## 3. Make proofs expose the mechanism

Before writing a proof, identify:

- the target assertion;
- the input results and the exact form in which they are needed;
- the invariant or estimate transported through the argument;
- the exceptional loci and degenerate cases;
- the topology or order relation used in every limiting passage.

If one of these inputs is absent from the source, do not hide the absence with polished prose. State the missing proof obligation or leave an explicit verification marker. A stylistic rewrite is never authority to invent a lemma, hypothesis, estimate, reference, or argument.

If the supplied statement and proof are inconsistent, do not repair the theorem by silently adding hypotheses or weakening its conclusion, and do not edit the proof to conceal the conflict. Isolate the first incompatible step and report what additional mathematical decision is needed.

Write a continuous proof when the argument has one line of motion. Use `\emph{Step 1.}`, `\emph{Step 2.}`, and so on only when a long proof has real stages—for example construction, uniform estimate, descent, limiting passage, and identification. A step must accomplish a named proof obligation; it must not contain one arbitrary paragraph merely to shorten the page.

At every transition, give the reason close to the assertion:

- not “by continuity”, but continuity in which topology and of which map;
- not “by standard arguments”, but the particular compactness, comparison, approximation, or base-change result;
- not “the result follows”, but the one-sentence implication when it is short;
- not “similarly” if the second case changes a hypothesis, direction of inequality, or exceptional locus.

Close logical gaps explicitly, especially:

- empty sets and vacuous suprema;
- identically `-\infty` functions or base-locus points;
- normalization, inseparability, and residue-field extensions;
- nets versus sequences in non-metrizable spaces;
- passage from divisorial points to the whole analytification;
- interchange of limits, envelopes, pullbacks, maxima, and suprema;
- uniformity of constants in auxiliary indices.

Maintain a dependency ledger. Whenever the proof says “fixed”, “uniform”, “independent”, “sufficiently large”, “after passage to a subsequence”, or “choose a common”, record what may depend on what. A sentence such as “the exponent may depend on the degree and the section, but the twisting line bundle is fixed” carries essential mathematical content.

Put each caveat beside the risky operation. If an identity initially holds only on divisorial points or points of generic support, say so there and name the principle extending its consequences. If a formula meets common zeroes or infinite values, state how it is interpreted there. Do not postpone these checks to a generic paragraph called “technical details”.

Do not add a separate proof environment for a one-sentence formal consequence. Conversely, do not compress a delicate reduction into “the claim is clear”.

If the proof of one main theorem occupies most of a section, it may be clearer to state the theorem, announce that the proof occupies the remainder of the section, and use unnumbered mathematical subheadings for its genuine stages, ending with a single `\qed`. Do not force a many-page argument into an opaque proof box merely for formal symmetry.

## 4. Keep paragraphs and sentences mathematical

Each paragraph should perform one recognizable job: set notation, state a difficulty, make a construction, establish an estimate, pass to a limit, identify an object, or record a consequence. Merge paragraphs that merely repeat the previous sentence. Split only when the proof changes jobs.

Prefer direct connective prose:

- “Choose … such that …”
- “By [precise result], …”
- “It remains to prove …”
- “Since …, the family is decreasing; hence …”
- “Conversely, …”

Use “we” for deliberate mathematical actions, not for stage directions. Avoid “Let us now turn to”, “We can easily see”, “It is worth noting that”, and “In order to” when “To” suffices.

Keep notation stable. Once an object has a name, do not alternate among synonyms. Favor established notation over explanatory prose only when the notation is reused enough to reduce cognitive load.

Start a technical section with its standing assumptions and deliverable, usually in one or two sentences. “Fix a finite surjective morphism …; the aim is to prove …, after establishing …” is useful navigation. “In this section we explore …” is not.

## 5. Use restrained emphasis

Headings should name mathematical content or mechanisms, for example “Weighted field norms”, “Finite descent”, or “A divisorial bound for test ideals”. Avoid headings such as “The key idea”, “A powerful new approach”, “Technical preparations”, or “Putting everything together”.

Use italics for proof stages or a locally defined term, not for praise. Avoid boldface inside mathematical prose unless the document has a specific typographic convention.

Do not add adjectives such as “crucial”, “remarkable”, “elegant”, “deep”, “novel”, or “powerful” in place of explaining the mathematical role. If a distinction matters, state it concretely: the estimate is uniform in the model, the construction commutes with finite pullback, or the argument avoids resolution of singularities.

## 6. Remove generic AI fingerprints

Delete or rewrite the following unless the mathematics specifically requires them:

- throat-clearing: “In this section, we delve into …”;
- fake reader guidance: “It is important to keep in mind …”;
- unsupported evaluation: “This beautiful result is of independent interest”;
- redundant recaps after every subsection;
- lists whose items are complete miniature essays rather than a genuine classification;
- symmetrical prose that hides an asymmetrical proof;
- invented terminology for a construction used once;
- parenthetical asides that should be a hypothesis or a proof sentence;
- citations placed at the end of a broad paragraph without identifying what they support;
- “clearly”, “obviously”, or “straightforward” at the point of greatest difficulty;
- a final “Conclusion” that only restates the introduction.

The test is not whether a phrase sounds formal. The test is whether removing it loses mathematical information, logical orientation, or a necessary transition.

Allow repetition only when it changes level: the abstract states significance, the introduction states the theorem, the strategy explains the mechanism, and the final body theorem assembles established inputs. Repeating the same information at the same level is clutter. Do not replace a technical term with a synonym merely to avoid repetition.

## 7. Revision protocol

For each changed passage:

1. Compare the revised claim with the original claim symbol by symbol.
2. Check that every pronoun and demonstrative has a unique referent.
3. Replace vague dependencies with the exact internal result or external locator.
4. Remove duplicated notation and duplicated motivation.
5. Read the paragraph without displayed equations; its logical direction should remain visible.
6. Read only the displayed equations; their order should still express the calculation.
7. Preserve the author's concise formulation when it already passes these tests.
8. Run a literal copyedit pass for repeated words, missing articles, malformed spacing, and punctuation. Do not preserve an accidental typo merely because the source manuscript supplied the style model.
