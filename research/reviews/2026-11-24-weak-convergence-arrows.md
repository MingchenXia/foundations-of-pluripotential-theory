# Weak-convergence arrows and the operator dd^c, 24 November 2026

The author asked that arrows representing weak convergence be written `\rightharpoonup`, and pointed out that Section 9.2 printed the empty identity "dd^c = dd^c".

## Changes

- **Notation.** The Conventions now say that $\rightharpoonup$ denotes weak convergence (of distributions, measures or currents, or in a Hilbert space). Chapter 1 (§`sec:weak-measures`) introduces it in the definition of convergence in the sense of distributions and extends it to vague and narrow convergence of measures; Chapter 7 introduces $T_i\rightharpoonup T$ in the definition of weak convergence of currents. The words naming the topology ("weakly", "vaguely", "narrowly", "in the sense of distributions") are kept.
- **Arrows.** Four agents replaced about 120 arrows (`\to`, and `\longrightarrow` in displays) that denote weak-type convergence, chapter group by chapter group; an independent check reviewed all 125 occurrences of `\rightharpoonup` and scanned the active files for missed ones, and changed nothing. Arrows for maps, numbers (including integrals), indices, pointwise, uniform, $L^p$, in-capacity and total-variation convergence are unchanged. Arrows kept on purpose: one arrow carrying both $L^1_{\loc}$ and distributional convergence (Chapter 3, Chapter 9), and convergences in total variation (Chapter 9 input on bounded subsolutions, two arrows in Chapter 15).
- **dd^c.** The macro `\ddc` and the composition $\mathrm d\mathrm d^{\mathrm c}$ print identically, so "$\mathrm d\mathrm d^{\mathrm c}=\ddc$" was empty in the definition `eq:dc-operator` (Chapter 7), in Section 9.2 and in the energy section of Chapter 17. The display now reads $\mathrm d\circ\mathrm d^{\mathrm c}=\frac{\mathrm i}{2\pi}\partial\bar\partial$, and the two sentences say that the composition of $\mathrm d$ with $\mathrm d^{\mathrm c}$ is $\ddc$. No other such identity occurs.

## Validation

`make check` and `make audit` pass (0 errors, 81 warnings). The forced build has no unresolved references and no overfull boxes; 949 physical pages (log: `research/reviews/logs/2026-11-24-weak-arrows-build.log`). Inspected physical pages 40 (Chapter 1 notation), 253 (Section 9.2) and 256 (Theorem 9.2.5, displayed harpoons).
