# Quantitative Demailly regularization

Source: user-supplied `Transcendental Nakamaye theorem (Copy).zip`; extracted manuscript *A transcendental Nakamaye theorem*, Duc Viet Vu and Mingchen Xia. The locators below are stable TeX labels in the exact retained version. Statement and full proof of `lem:regularization` (source lines 827–941), and patching context (770–814), read. No complete independent proof verification has been performed.

## Exact added assertion

`lem:regularization`: for a fixed compact Kahler manifold (Z,omega_Z), dim_C Z=d, there is c>0 depending **only on (Z,omega_Z)** such that for every smooth closed real (1,1)-form zeta, every phi in PSH(Z,zeta), and every integer m≥1, a global quasi-psh phi_m exists with

1. zeta+dd^c phi_m ≥ -(c/m) omega_Z;
2. locally phi_m ≥ m^(-1) psi_(I(m phi))+O(1).

Here `psi_J` is locally log(sum |f_i|^2) for holomorphic generators of J; generator changes contribute bounded terms. The O(1) is a local bounded term, not a constant stated uniform in m, phi or zeta. This lemma does **not** state that phi_m has analytic singularities, is monotone, converges to phi, or is quasi-equisingular. Prove those properties for the separate sample Demailly theorem, with their own hypotheses and sequence construction.

## Proof dependencies and constants

`lem:patching`: finite nested coordinate balls, fixed cutoff Hessian bounds and an overlap bound a≥0; boundary competitors are dominated by a chart whose inner set contains the point. This domination is non-strict, and the local formula becomes a maximum over a fixed finite index set. Recover the full patching conclusion, including the local two-sided bound, not just the word "gluing".

`lem:regularization` Step 1: fixed geometry/chart/volume-comparison data; local smooth h_j with dd^c h_j=zeta; weighted holomorphic Hilbert spaces with exp(-m(phi+h_j)); local Bergman potentials m^(-1) log K_j-h_j. Generator existence uses DEL00 Proposition 1.2, with its source weight m(phi+h_j)/2 because DEL uses exp(-2 weight). Nadel coherence gives finite local generators. Neither needs a constant uniform in phi for the local O(1).

Step 2: on overlaps choose a common local potential g. Holomorphic gauges cancel h_j-g, so constants do not depend on zeta. Solve dbar with singular weight m Psi+2d log|z-x|+|z|^2 on B_l. Cutoffs and the separation r>0 are fixed geometrically. The weighted estimate gives a norm bound independent of Psi, m and x; the logarithmic pole and local upper boundedness of Psi force u(x)=0, preserving interpolation. Compare kernels and take the maximum of finitely many overlap constants.

Step 3: patch with a=C_B/m to obtain c=C_B C_chi. Check that chosen coordinate balls/pseudoconvex domains, common potential balls and all distance/volume bounds have only fixed geometric dependence. Record the norm-to-kernel inequality and the direction of each comparison.

Natural home Q06; prerequisites Q04 (full singular-weight Hörmander and interpolation) and Q05 (coherent generators). Preserve sample multiplier weight exp(-phi), logarithm of squared norms and dd^c scaling. Check source versions of DEL00/Dem92/DPS01/Pop04/DemCADG before active citation. The source reports difficulty with Pop04's argument; this is a source statement, not evidence that Pop04 is false.

## Remaining integration

Read and reconstruct `lem:ideal-function` separately if used, including codimension/zero-ideal cases; recover qualitative gentle and quasi-equisingular approximation without silently borrowing this lemma's rate. Q10/Q14/A01 collect rooftop, trace, numerical restricted volume and relative principalization interfaces used by the rest of the Nakamaye paper. Its main theorem is not marked proved in this new book.
