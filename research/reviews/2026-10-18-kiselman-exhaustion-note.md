# Local note after Theorem 8.5.1

The author's requested sentence now follows the proof of Kiselman's minimum principle: on a pseudoconvex domain, the function psi required by the theorem always exists. The sentence points to the existing construction in the proof of Corollary 11.2.6 (`cor:kiselman-pseudoconvex-tube`).

## Mathematical and reading scope

Read the complete Kiselman section, including the theorem, its proof and the product-tube corollary, together with the definition of pseudoconvexity, Oka's boundary-distance theorem and its proof, and the general pseudoconvex-tube corollary in Q04. Consulted the Q02/Q04 dossiers and the reference guide. No external source was freshly audited.

For a proper domain, the existing construction is

`psi(z,w) = |z|^2 + |Re w|^2 + max{-log dist((z,w), C^(m+k) \ Omega), 0}`.

Oka's theorem supplies plurisubharmonicity of minus the logarithm of the distance. The domain's imaginary translations preserve that distance. On the real slice, the quadratic term bounds the Euclidean norm, and the logarithmic term keeps sublevel sets away from the complement. The whole-space case uses only the quadratic term. Thus the cited proof supplies precisely the invariance and compact real-slice sublevels required in Theorem 8.5.1. The new sentence is an explanatory forward reference; the earlier proof does not acquire a new dependency.

Completed a second direct read of the local passage, the surrounding theorem and proof, and the cited construction. This is a local editorial check; earlier whole-chapter verification remains in force.

## Validation

- `make check`: passed.
- `make audit`: zero errors, 82 warnings in the existing manuscript.
- Full `latexmk` build followed by `make build`: passed, 952 physical pages; no unresolved citations/references or fatal errors.
- Inspected physical PDF pages 242 and 245 (printed pages 228 and 231), including the theorem statement, the new sentence, and its transition into Corollary 8.5.2. The cross-reference resolves to Corollary 11.2.6. No overflow occurs in the affected passage.
- The final log contains four small overfull boxes elsewhere (2.05 to 3.63 pt); these unrelated passages were not edited.
- The cloud's retained TeX installation required activation and the missing `qhv.map` font-map registration before the full build succeeded. No tracked build configuration was changed.

Build and check logs are retained under the ignored `build/reviews/2026-10-18-kiselman-note/` directory. No full source-release archive or new whole-book review was performed.
