# Envelope regularity: exact source dependencies

This is source research by the authoring agent, not a manuscript proof verification or independent certification. Q10-02 remains drafting. No regularity result is accepted as an external input. The active manuscript remains the reviewed 417-page checkpoint with 55 of 87 provisionally required obligations verified.

## Full real Hessian bounds

SGPT `chapter_npp.tex`, lines 1207–1218, requires the compact Kähler envelope of a real C1,1 obstacle to be C1,1, with a uniform norm bound depending on the fixed geometry and obstacle norm. Tosatti's published Theorem 1.1, pp.281–286, and Theorem 3.1, p.287, are directly checked. All nine published article pages were read; the exact seven-page arXiv v3 was also completely read as text. Their pagination is kept separate. Published PDF pp.1,4–7 were visually inspected.

The route has three distinct proof obligations:

1. Smooth solvability of the penalized equation `(omega + i partial barpartial phi)^n = exp(beta(phi-v)) omega^n`. Tosatti explicitly delegates this to Aubin and Yau. Existing compact *linear* elliptic inversion does not supply this nonlinear equation.
2. Uniform sup and metric-Laplacian bounds, and the `C log(beta)/beta` convergence to the envelope. Published equation (2.2), p.283, delegates these to Berman's zero-temperature paper. No complete Berman proof has been read in this unit.
3. The full real Hessian maximum principle. Equations (2.7)–(2.13), pp.284–286, give the perturbation calculation and the positive beta contribution. The remaining third-derivative absorption is explicitly delegated to Chu–Tosatti–Weinkove, *On the C1,1 regularity of geodesics in the space of Kähler metrics*, proof of Theorem 1.2. Its arXiv lead is 1611.02390. That proof is not yet read or reconstructed here.

Theorem 3.1 smooths a C1,1 obstacle with a uniform *full real Hessian* bound, applies the estimates uniformly and uses sup-norm envelope stability. It does not by itself establish the corresponding claim for barriers with only bounded metric Laplacian.

## Bounded metric Laplacian for rooftop obstacles

SGPT lines 1221–1226 require two C1,bar1 obstacles, where the norm controls the bounded metric Laplacian. Exact Darvas–Rubinstein arXiv v1 Theorem 2.5(ii), p.5, uses this norm; its full statement and pp.4–6 were read. Complete Sections 4.2–4.3, pp.12–18, were read, including the proof of the local C1,1 rooftop obstacle theorem. Original pp.5,13 images were inspected. No published proof read is claimed: Project Euclid returned HTML and the J-STAGE PDF attempt returned HTTP500.

The local argument proves quadratic separation near transversal obstacle crossings, quadratic growth at contact, and then full real Hessian bounds through harmonic Poisson estimates away from contact. It quotes the Lipschitz regularity of a subharmonic envelope of a Lipschitz obstacle. It then glues local subharmonic majorants with a partition of unity to a barrier between the psh envelope and the rooftop obstacle, before using a single-obstacle regularity theorem. Its bounded-Laplacian passage uses weak contact equality and harmonicity off contact. The preprint's proof uses swapped part labels relative to the statement; record actual conclusions rather than inheriting those labels.

Reconstruction must preserve the norm and metric at each step: a bounded metric Laplacian for a non-qpsh barrier does not give a bounded full real Hessian, a bounded complex Hessian or an arbitrary coordinate Euclidean Laplacian bound. Smooth approximation and the gluing/contact calculation must prove the claimed uniform *metric* bound. The already established W2,p and weak contact locality are the relevant internal foundations; no unjustified uniform C1,1 smoothing is allowed.

## Big classes and the ample locus

SGPT lines 1493–1504 delegate the ample-locus bounded-metric-Laplacian envelope theorem to Di Nezza–Trapani. Primary publisher metadata and the five-page final sample were retrieved. Printed pp.1347–1349, including Theorem 1.1 and the proof outline, were completely read; PDF pp.3,5 images inspected. The final sample is not the complete published article. Exact arXiv v3 text reads were pp.1–3,6–7,9–10,18–20; the truncated first attempt at pp.18–20 was repaired by a narrower direct read.

The final published introduction expressly identifies missing mixed terms in BD12 Lemma 1.12. Its stated replacement route is: weaker Hessian estimate giving Hölder regularity; a Lelong–Jensen estimate giving variable-coefficient Hessian bounds; then passage to a modification and suitable line-bundle coordinates to remove those coefficients. The original Chern-exponential regularization estimate, its measure-density comparison and all mixed-term bounds require internal reconstruction. The complete Lemma 3.3 measure argument was read; the displayed implication from exponential smoothing to density still cites BD12 equation (1.16). Lemmas 3.4–3.5 were only partly read, and the Section 4 proof ending does not count as a complete Section 4 read.

Complete arXiv Theorem 4.2 and proof, p.19, were read. It handles finite bounded-Laplacian rooftops in a big class: first a qpsh obstacle, then a dominating Kähler background and its regular rooftop, then resolution and a Kähler modification for the compact complex case. The intermediate Kähler rooftop theorem is delegated to Berman and Darvas–Rubinstein. Thus this citation does not bypass the preceding rooftop obligation or the approximation/ample-locus foundations. The published version's final theorem locator has not been checked.

## Version and normalization record

The primary SMF page confirms the English title, authors, 57 (2024), no.5, pp.1347–1370 and DOI 10.24033/asens.2592. Crossref's later timestamp is not the printed journal year. The existing DNT23 key is retained and its verified DOI/URL added. CZ19's Crossref identity, authors, volume62, issue2, pages371–380 and DOI were checked; its online-first date does not replace the existing issue year. Its proof was not read. Tosatti's published title-page and Crossref identity agree. DR16's DOI identity was independently checked, but this unit does not independently establish its printed page range from a publisher PDF.

These sources use `i partial barpartial`; the book uses `dd^c = i/(2pi) partial barpartial`. Dividing source background forms by 2pi keeps the potential unchanged. Laplacian and volume constants must then be recalculated in the book's declared metric convention. No source estimate is copied without this conversion.

All five fetched PDF versions are retained separately with URLs, dates, exact read scopes and SHA-256 entries. No existing original was overwritten. There are now 110 immutable retained files. Q05-02's own task prerequisites are verified, but its enforced whole-chapter prerequisite A01 remains unfinished; the three envelope PDE scopes remain open.
