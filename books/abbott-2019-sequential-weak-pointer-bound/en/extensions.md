# Finite strength and other observables

A projection allows only the eigenvalues $0$ and $1$. What happens to the bound if an operation keeps just a fraction of a component, for example by multiplying that component by $1/2$?

::: {.corollary #positive-contractions title="Positive contractions" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s2" status="written-proof" proof="pf-positive-contractions" doi="10.5281/zenodo.24212412" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/275"}
Replace each $P_j$ by a positive contraction $0\preceq A_j\preceq I$ on $\mathbb C^d$ and use the same Jordan recursion. At every $n\ge1$, over all finite dimensions, such $A_j$ and density matrices, the exact minimum is still $-c_n$ and the maximum is still $1$.
:::

::: {.proof #pf-positive-contractions}
Write the distinct positive eigenvalues of $A$ as $0<\lambda_1<\cdots<\lambda_k\le1$ and set $\lambda_0=0$. Let $E_i$ project onto the sum of the eigenspaces with eigenvalues at least $\lambda_i$. Then

$$
A=\sum_{i=1}^k(\lambda_i-\lambda_{i-1})E_i+(1-\lambda_k)0.
$$

Along an eigenvector with eigenvalue $\lambda_j$, the first $j$ weights add to $\lambda_j$. On the zero eigenspace all terms vanish. The weights are nonnegative and sum to $1$. For $A=0$, take the zero projection with weight $1$. The expectation is linear in each input separately. Expanding every $A_j$ therefore gives a weighted average of expectations for projection sequences, with weights given by products of the individual weights. Each expectation lies in $[-c_n,1]$. Projections themselves satisfy $0\preceq P_j\preceq I$, so the same constructions attain both endpoints. [Version 2, Corollary 2](https://doi.org/10.5281/zenodo.24212412)
:::

## How Gaussian pointers yield the Jordan product

Take independent, real, centered Gaussian pointer wavefunctions $\phi_j(x)=(2\pi\sigma_j^2)^{-1/4}e^{-x^2/(4\sigma_j^2)}$ with $\sigma_j>0$. The position density $|\phi_j|^2$ has variance $\sigma_j^2$. Coupling $j$ is $e^{-ih_jP_j\otimes p_j}$, where $p_j$ is the pointer momentum operator and $\hbar=1$. It shifts the pointer by $0$ or $h_j$ along the two projection components.

::: {.corollary #gaussian-envelope title="Finite-strength Gaussian envelope" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s3" status="written-proof" proof="pf-gaussian-envelope" doi="10.5281/zenodo.24212412" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/276"}
For any $n\ge1$, finite-dimensional orthogonal projections, density matrix, independent Gaussian pointers as above, and positive couplings $h_j$, the normalized mean $m_n=\mathbb E[x_1\cdots x_n]/\prod_j h_j$ satisfies $-c_n\le m_n\le1$. The width and coupling of the final pointer do not affect $m_n$.
:::

::: {.proof #pf-gaussian-envelope}
Write $E_0=I-P$ and $E_1=P$. A normalized position average pairs the left and right projection components $a,b\in\{0,1\}$. Completing the square in the product of wavefunctions gives a Gaussian centered at $h(a+b)/2$ times an overlap factor.

$$
\int_{\mathbb R}\frac{x}{h}\phi(x-ah)\phi(x-bh)\,dx
=\frac{a+b}{2}\exp\!\left[-\frac{h^2(a-b)^2}{8\sigma^2}\right].
$$

Use this integral as the coefficient of $E_aYE_b$. The $(0,0)$ term vanishes and the $(1,1)$ term gives $PYP$. The two cross terms each have coefficient $t/2$, where $t=e^{-h^2/(8\sigma^2)}$. Thus one step gives the map

$$
T_{P,t}(Y)=t\mathcal J_P(Y)+(1-t)PYP.
$$

Each independent pointer couples once, so the integrals for the product mean can be taken one pointer at a time. Applying each weighted integral to the terminal observable $I$, from the last step to the first, gives $m_n=\operatorname{Tr}[\rho\,T_{P_1,t_1}\cdots T_{P_n,t_n}(I)]$. Since $T_{P_n,t_n}(I)=P_n$, the last parameter $t_n$ drops out.

If $-cI\preceq Y\preceq I$, then $-cP\preceq PYP\preceq P$, so $PYP$ lies in $[-cI,I]$. The Jordan term lies in $[-F(c)I,I]$. Since $F(c)\ge c$ and $0<t\le1$, their weighted average lies in the latter interval. Induction from $P_n$ proves the envelope.

Set $h_j=\varepsilon g_j$ and take $\varepsilon\downarrow0$ with $n$, $\rho$, $P_j$, $\sigma_j$ and $g_j>0$ fixed. Each $t_j\to1$, so the finite composition tends to the Jordan recursion and $m_n\to\mu_n$. Varying couplings can therefore bring the value arbitrarily close to the sharp weak-limit lower endpoint. Finding the exact minimum with prescribed positive couplings requires a separate argument. [Version 2, §1 and Corollary 3](https://doi.org/10.5281/zenodo.24212412)
:::

## When does the spectral product range hold?

::: {.corollary #commuting-symmetric title="Commuting and symmetric observables" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s4" status="written-proof" proof="pf-commuting-symmetric" doi="10.5281/zenodo.24212412" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/277"}
For pairwise commuting orthogonal projections, $0\le\mu_n\le1$ and $0\le m_n\le1$ in the Gaussian model above. For arbitrary Hermitian observables $A_1,\ldots,A_n$, the absolute value of the nested Jordan coefficient is at most $\prod_j\|A_j\|$. If each spectrum is symmetric about zero, the coefficient lies between the smallest and largest products obtained by choosing one value from each spectrum.
:::

::: {.proof #pf-commuting-symmetric}
In the commuting case the recursive $Y$ commutes with $P$, so $PY=YP=PYP$. Both recursions yield $P_1\cdots P_n$. Pairwise commutation makes this product self-adjoint and idempotent, so its expectation lies in $[0,1]$. For general Hermitian matrices the triangle inequality and submultiplicativity give $\|(AY+YA)/2\|\le\|A\|\|Y\|$. Apply this at every step, then use $|\operatorname{Tr}(\rho X_1)|\le\|X_1\|$. If all spectra are symmetric about zero, every nonzero matrix has both extreme eigenvalues $\pm\|A_j\|$. Choosing among these gives the extreme products $\pm\prod_j\|A_j\|$. If a matrix is zero, every product is zero and the norm bound forces the coefficient to be zero. [Version 2, Corollary 4](https://doi.org/10.5281/zenodo.24212412)
:::

## Contribute a formal proof

Lean proves the refutation of the universal bound through the three-dimensional witness. Theorem 1's all-length bounds, attainment and asymptotic, and the three corollaries, each have a formalization request. Coordinate scope in the relevant request and submit a focused PR from your fork to the upstream trureturing $\,\texttt{dev}\,$ branch. [Contribution guide](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md) · [Mathesis record for version 2](https://mathesis-omega-research.apps.chrono-ai.fun/papers/abbott-2019-sequential-weak-pointer-bound?version=2)

- [Sharp bounds and attainment at every length](https://github.com/the-omega-institute/trureturing-requests/issues/274)
- [Sharp bounds for positive contractions](https://github.com/the-omega-institute/trureturing-requests/issues/275)
- [Finite-strength Gaussian envelope](https://github.com/the-omega-institute/trureturing-requests/issues/276)
- [Commuting and symmetric observables](https://github.com/the-omega-institute/trureturing-requests/issues/277)
