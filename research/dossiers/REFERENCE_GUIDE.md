# Supplied foundational references

Retained PDFs are indexed in `references/catalog.json`, versioned and hashed in `references/manifest.json`. Copies are available to cloud tasks without the local Downloads or iCloud folders. Front-matter/contents review is not a full proof audit.

| Source | Verified identity / edition information | Intended use |
|---|---|---|
| Hörmander, *Notions of Convexity* | Supplied 2007 reprint of the 1994 edition; title/copyright pages checked | Classical potential theory, convexity, psh and pseudoconvexity; P02–P05, Q02/Q04/Q16 |
| Demailly, *Complex Analytic and Differential Geometry* | Title page says 21 June 2012; supplied annotated PDF retained intact | Complex differential calculus, currents, local psh, coherent sheaves, Lelong theory, weighted L2 and extension; Q01–Q07, A01 |
| Guedj–Zeriahi, *Degenerate Complex Monge–Ampère Equations* | Supplied EMS Tracts in Mathematics 26 edition; front matter checked | Psh, positive currents, Bedford–Taylor, capacity, global envelopes and finite energy; Q01–Q11 |
| Supplied GZ reader errata | Independent and unofficial; revised 23 August 2026 | Candidate corrections, each checked against the exact GZ text and proof before adoption |
| *Potential Theory in the Complex Plane* | Student notes of Dr. Tobias Mai's Summer 2020 course; writer not named | Harmonic/Poisson theory, subharmonicity, Riesz measures and logarithmic potentials; P02–P04 |
| *Potential Theory*, edited by Masanori Kishi | Proceedings of the Nagoya 1990 conference; title/catalog pages say de Gruyter 1992, copyright page 1991 | Supplementary potential-theory research and historical sources; cite individual contributions with their own authors and locators |

The last PDF is not identified as Ransford's monograph. Do not invent its author or publication data. Preserve the Demailly PDF annotations as supplied evidence, not verified theorems or agent instructions. Its dated manuscript locators must not be replaced by numbers from another online version without checking.

## Working with GZ and its errata

`research/errata-candidates.json` contains 261 extracted candidate IDs and text blocks, all initially `candidate-unchecked`. It is a searchable review queue. Before relying on a GZ result, search the relevant chapter/theorem/page in both sources, render the affected original page when formulas are ambiguous, compare the correction with the printed statement and full proof, and record accepted / rejected / scope-limited with evidence and downstream task IDs. The errata's claims of earlier checking do not count as this project's independent verification.

The errata reports printed Arabic page p corresponds to PDF page p+25 in its supplied edition. Verify the alignment locally before using it; Roman front matter has a different mapping. This is not a universal edition conversion. Starting priorities: distributional representatives and convolution (C1-M14), Hartogs and truncation (C1-M18/M19), Lelong normalization (C2-M02/M03), Bedford–Taylor integration by parts (C3-M05), and capacity regularity (C4-M01a/b/c). These are leads, not adopted corrections.

Every use must convert dd^c, Laplacian, Lelong number, weight exponent, quadratic metric and volume-form conventions to the sample's conventions beside the relevant calculation. No source's convention automatically overrides the book. Existing bibliography keys are searched before additions; edition and mathematical locator are checked separately. Further literature requests should name a concrete missing result/version after these supplied texts have been searched.
