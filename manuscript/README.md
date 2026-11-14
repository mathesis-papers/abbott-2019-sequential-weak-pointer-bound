# Sharp sequential pointer-product bounds

The note refutes the arbitrary-rank interpretation of the conjecture in Abbott,
Silva, Wechs, Brunner and Branciard, *Anomalous Weak Values Without
Post-Selection*, Section 4, following equation (26), arXiv:1805.09364v3.
The rational witness gives -1/6. For n measurements in unrestricted finite
dimension, the exact minimum is -c_n, with c_1=0 and
c_(n+1)=(1+c_n)^2/[8(1-c_n)]. The uniform infimum is -1/3.

The interval method, scalar recurrence and its asymptotic rate are credited to
Sun, Luo and Ye, *On the Efficiency of Random Permutation for ADMM and
Coordinate Descent*, Mathematics of Operations Research 45 (2020), 233–271;
the locators use arXiv:1503.06387v3. The note supplies explicit finite-length
attainment in the pointer problem.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively use a standard LaTeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is included in `note.tex`; BibTeX and external figures are not
needed. `source.zip` contains the complete source and verification files.

## Mathematical coverage

- Written proofs: the normalized fixed-length Gaussian limit, spectral bounds,
  exact minima and attainment, the asymptotic rate, positive contractions,
  the finite-strength centered Gaussian envelope and final-pointer independence,
  and the commuting-projection and Hermitian-norm corollaries.
- Exact algebra and finite checks: `verify.py` generates `verification.json`,
  including the rational -1/6 witness, an exact -81/448 extremizer, symbolic
  scalar and Gaussian identities, eight constructions at lengths 1 through 64,
  and 360 reproducible matrix controls. Four further sets of 144 controls
  check the Gaussian envelope, positive contractions, commuting projections
  and Hermitian norm bounds; exact identities check the Gaussian-map
  decomposition and final-pointer independence. Finite checks supplement the written
  all-parameter proofs.
- The pinned declaration
  `D5.S3.Quantum.Measurement.Weak.SequentialWeakPointerRefutation.result`
  proves the negation of the universal -1/8 nested-product claim using the
  rational witness. Its parameter 2 represents three observables. Its source is
  `https://github.com/the-omega-institute/trureturing/blob/ea30c256f9857dcf2582db122a9570836d8a5f18/D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.lean`.
  The general sharp bounds and Gaussian limit have the written proofs in the note.

Run the supporting calculations with Python 3.13 and the listed dependencies:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python verify.py
```

The expected console result begins `PASS: exact witnesses`. The numerical
tolerance is 1e-11; exact and symbolic assertions use exact arithmetic. The
scope and individual values appear in `verification.json`.

## Authors and license

1. Haobo Ma — ChronoAI Pte Ltd, Singapore.
2. Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

Copyright 2026 Haobo Ma and Wenlin Zhang. The note and accompanying original
source are licensed under Creative Commons Attribution 4.0 International
(CC BY 4.0), identifier `cc-by-4.0`.
