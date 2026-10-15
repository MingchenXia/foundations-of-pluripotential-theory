# Symbolic check of `eq:chern-kernel-square-identity`

Evidence for the correction made on 2026-10-06 in `chapters/inputs/q10-big-envelope-regularity.tex` (lemma `lem:chern-joint-smoothing`).

`fast4.py n seed trials degree` builds an exact finite-jet model of the Chern exponential-map kernel at the centre (random Kähler curvature coefficients and higher-order jet coefficients with the required symmetries), computes the joint Levi form of the smoothed function for random real polynomial test functions, and compares it with three versions of the right-hand side of the identity:

- `text`: the identity as printed before the correction (with the original conjugation and without the extra term);
- `sfix`: with the conjugation in $\Xi$ corrected but without the extra integration-by-parts term;
- `full`: the corrected identity as now printed.

Output `fast4_n1.out` (n = 1, two random trials) shows `full ZERO` and the other two nonzero. `fast4_n2.out` records the same check for n = 2 when it has been run. `verify_QJ.py`, `verify_kernel.py`, `fast3.py` and `value_term.py` are the auxiliary checks of the expansions of the kernel norm, the Jacobian and the value term. These scripts are verification aids written during review; they are not part of the book.
