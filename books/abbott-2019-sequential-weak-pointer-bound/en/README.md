# How three pointers go below −1/8

Imagine three pointers that start near zero and can end up on either side of it. Multiply the three signed readings on each run, then average those products over all runs. Abbott, Silva, Wechs, Brunner and Branciard asked whether this average, after normalization, always stays at or above $-1/8$. When the projections can have arbitrary ranks, **the third pointer is enough to break the bound**. Haobo Ma and Wenlin Zhang give a three-dimensional example with value $-1/6$ and find the minimum for every length. For three pointers the actual minimum is $-81/448$. The minima for finite lengths approach $-1/3$.

## Keeping part of an arrow

Draw a line through the origin and drop the tip of an arrow perpendicularly onto the line. The resulting arrow retains the component along the line. Two examples are $P(x,y)=(x,0)$ and $Q(x,y)=((x+y)/2,(x+y)/2)$, which project onto the horizontal axis and the diagonal. Starting with $(0,1)$, applying $Q$ then $P$ yields $(1/2,0)$. Applying $P$ first gives zero. Each operation keeps a component, and the order changes the result.

In higher dimensions a projection can retain a direction or an entire plane. The dimension of the retained subspace is the **rank**. A projection acts by $1$ on that subspace and by $0$ on the perpendicular subspace. In matrix notation an orthogonal projection satisfies $P=P^*=P^2$, with $P^*$ the conjugate transpose.

## From readings to matrices

In the idealized experiment each measurement has its own independent pointer, initially centered at zero. If the state lies wholly in the subspace retained by projection $j$, the initial position distribution shifts right by $h_j$. In the perpendicular subspace the shift is zero. A general state can have both components. All runs enter the average, without filtering by the final state. The statistic for readings $x_j$ is $\mathbb E[x_1\cdots x_n]/(h_1\cdots h_n)$. Hold the length, state and projections fixed while reducing all couplings together. The result is the weak-limit coefficient $\mu_n$. The [finite-strength chapter](extensions.md) derives this limit from the Gaussian model.

Start the matrix calculation with the final projection. Write $\mathcal J_P(X)=(PX+XP)/2$ for the **Jordan product**. Bring in one earlier projection at a time, averaging the two multiplication orders at each step.

$$
X_n=P_n,\qquad X_j=\mathcal J_{P_j}(X_{j+1}),\qquad
\mu_n=\operatorname{Tr}(\rho X_1).
$$

Each $X_j$ is Hermitian, meaning $X_j^*=X_j$, so its eigenvalues are real. For a unit state vector $\psi$, the coefficient is the real number $\langle\psi,X_1\psi\rangle$. A general density matrix $\rho$ is positive semidefinite with trace $1$. It averages pure-state expectations with nonnegative weights summing to $1$. The expectation of one projection thus lies between $0$ and $1$. Where does the negative sign enter the nested average? The [three-dimensional example](witness.md) reduces it to a dot product you can compute by hand.

::: {.film src="001-pointer-product"}
How three measurements give $-1/6$ and how the lower bound changes when one more measurement enters the sequence.
:::

## Sources

- Haobo Ma and Wenlin Zhang, *Extending Sun–Luo–Ye bounds to refute Abbott et al.'s pointer-product conjecture*, version 2, CC BY 4.0. [Paper](https://doi.org/10.5281/zenodo.24212412)
- Abbott, Silva, Wechs, Brunner and Branciard, *Anomalous Weak Values Without Post-Selection*, 2019. The all-length conjecture appears in §4 after (26). Appendix C proves the two-projection bound for arbitrary ranks. [Paper](https://doi.org/10.22331/q-2019-10-14-194)
- Sun, Luo and Ye studied this recurrence and convergence rate in randomized optimization. See §6.2 and §6.4, equations (78), (80) and (118) in arXiv v3. They credit Gilbert Strang for the one-step spectral estimate for Jordan products. [Sun, Luo and Ye](https://arxiv.org/abs/1503.06387v3) · [Strang](https://doi.org/10.2307/2312733)

A seminar deck follows the argument with speaker notes for every frame.

::: {.slides src="pointer-bounds"}
From the three-dimensional counterexample to the sharp bound at every length.
:::
