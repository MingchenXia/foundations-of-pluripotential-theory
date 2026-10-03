# PSHD: automatic upper semicontinuity

Source: `references/originals/PSHD_vibe.pdf`, six pages, fetched 2026-10-03; exact hash in manifest. Printed title: *Subharmonicity on All Affine Complex Lines Forces Upper Semicontinuity*. No author printed. All six pages read; theorem/proof structure checked against sample `def:psh` and `thm:psh_rigid`. Full independent verification and reconstruction remain open.

## Exact interface

Theorem 1.1 (p.1): for a domain Omega in C^n and phi:Omega→[-infinity,infinity), phi not identically -infinity, if phi is subharmonic or identically -infinity on **every connected component of every affine complex-line section**, then phi is upper semicontinuous and hence psh. Keep the sample's definition and prove this equivalence beside it (Q02). A fixed coordinate splitting is insufficient; Remark 2.2 refers to Wiegerinck's example. Treat n=0 separately under the sample convention, and n=1 directly.

## Proof chain to reconstruct

- Lemma 1.2 (pp.1–2): local Borel measurability from upper semicontinuity in z' and subharmonicity in w. Use truncated disc means, reverse Fatou and continuity under translations; only ultimately bounded truncations recover the actual value. Do not assume joint measurability before proving it.
- Lemma 1.3 (pp.2–3): a Borel probability on the high-value annular star with Riesz energy I_(2n−2) ≤ C_(n,R), independent of u, x, A. Compact circle fibers of the Hopf map admit a Borel selector. Product radius/projective-space dimension is 2n−1, so the energy kernel is integrable. P06 supplies this material.
- Lemma 1.4 (pp.3–4): averaging over complex hyperplanes gives the |zeta|^(-2) Fourier weight, hence L2 projection densities with integral of squared norms equal to a positive dimensional constant times I_(2n−2). Prove Fourier energy identity and Plancherel in P06, and the averaging formula directly.
- Lemma 1.5 (p.4): compact inner approximation and Cauchy–Schwarz give a uniform positive incidence-measure bound; the limsup has positive measure, so one affine line meets infinitely many high sets.
- Proposition 2.1 (pp.4–5): induction for finite nonnegative functions, then Borelness, local upper boundedness via incidence, positivity of dd^c by slicing/Fubini, and equality everywhere with the canonical psh representative via polar coordinates on line directions. The distributional characterization used here must be proved independently in Q01/Q02, without using the theorem being proved.
- Theorem 1.1 proof (p.6): max(phi,-m)+m is finite nonnegative; subtract m and decrease to phi. Decreasing upper semicontinuous functions have upper semicontinuous limit. Track identically -infinity sections throughout.

## Open dependencies and normalization

The paper invokes Arsenin–Kunugui (Kechris Theorem 18.18), the Fourier energy formula (Mattila Lemma 12.12), Plancherel, and the sample distributional characterization. These are not silently accepted external inputs. Reconstruct the precise compact-fiber selection case or obtain an explicit author decision; the Fourier and representative arguments must be proved. Fourier convention is exp(-2pi i Re<y,zeta>). Its positivity arguments are compatible with the sample dd^c scaling; no exact Fourier constants are printed, so do not invent them.

Citation metadata for Arsove, Kechris, Mattila, Wiegerinck and any future attribution of the PDF must be checked before adding new active bibliography entries. Full-source retention and this dependency map are separate from a proof audit.
