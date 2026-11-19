# Extending Sun–Luo–Ye bounds to refute Abbott et al.'s pointer-product conjecture

**Authors:** Haobo Ma, Wenlin Zhang

Extending the spectral bounds of Sun, Luo and Ye [Mathematics of Operations Research 45, 233–271 (2020)], we refute the arbitrary-rank interpretation of the pointer-product conjecture of Abbott, Silva, Wechs, Brunner and Branciard [Quantum 3, 194 (2019), Section 4, p. 5, after equation (26); arXiv:1805.09364v3]. Three orthogonal projections on C^3 give the normalized weak-limit pointer product -1/6 < -1/8. For n measurements in unrestricted finite dimension, the exact minimum is -c_n, where c_1=0 and c_(n+1)=(1+c_n)^2/[8(1-c_n)]. Codimension-one projections attain every finite-length minimum, and c_n increases to 1/3. Thus pointer products have infimum -1/3, separated by 2/3 from the limiting ordered weak value -1. The same bounds hold as envelopes at every finite coupling strength for independent centered Gaussian pointers.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24212412](https://doi.org/10.5281/zenodo.24212412)
- Concept DOI: [https://doi.org/10.5281/zenodo.24212411](https://doi.org/10.5281/zenodo.24212411)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [abbott-2019-sequential-weak-pointer-bound](https://mathesis-omega-research.apps.chrono-ai.fun/papers/abbott-2019-sequential-weak-pointer-bound?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Extending Sun–Luo–Ye bounds to refute Abbott et al.'s pointer-product conjecture. Mathesis, version 2. https://doi.org/10.5281/zenodo.24212412

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/ea30c256f9857dcf2582db122a9570836d8a5f18/D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.lean) | No public receipt |
| Corollary (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/ea30c256f9857dcf2582db122a9570836d8a5f18/D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/ea30c256f9857dcf2582db122a9570836d8a5f18/D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/ea30c256f9857dcf2582db122a9570836d8a5f18/D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/abbott-2019-sequential-weak-pointer-bound/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/abbott-2019-sequential-weak-pointer-bound/abbott-2019-sequential-weak-pointer-bound/zh/) · [Read in English](https://papers.trureturing.org/abbott-2019-sequential-weak-pointer-bound/abbott-2019-sequential-weak-pointer-bound/en/)

[Slides](https://papers.trureturing.org/abbott-2019-sequential-weak-pointer-bound/abbott-2019-sequential-weak-pointer-bound/slides/) ([sources](books/abbott-2019-sequential-weak-pointer-bound/slides/)) · [Videos](https://papers.trureturing.org/abbott-2019-sequential-weak-pointer-bound/abbott-2019-sequential-weak-pointer-bound/films/) ([sources](books/abbott-2019-sequential-weak-pointer-bound/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/abbott-2019-sequential-weak-pointer-bound/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `commuting-symmetric` | variant | `D5/S3/Quantum/Algebra/CommutingProjectionFourSector.commuting_projection_four_sector_criterion` |
| `gaussian-envelope` | none | — |
| `pointer-refutation` | same | `D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.result` |
| `positive-contractions` | variant | `D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.result` |
| `sharp-bounds` | variant | `D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/abbott-2019-sequential-weak-pointer-bound/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
