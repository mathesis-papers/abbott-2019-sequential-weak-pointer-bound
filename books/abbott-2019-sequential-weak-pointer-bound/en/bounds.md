# The sharp bound at each length

Start with $X_n=P_n$, whose eigenvalues lie between $0$ and $1$. One more Jordan product can take the bottom eigenvalue to $-1/8$. The theorem gives the furthest down it can go at each step.

::: {.theorem #sharp-bounds title="Sharp finite-length bounds" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s1" status="written-proof" proof="pf-sharp-bounds" doi="10.5281/zenodo.24212412" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/274"}
Put $c_1=0$ and $c_{r+1}=F(c_r)$, where $F(c)=(1+c)^2/[8(1-c)]$. For every $n\ge1$, finite dimension $d\ge1$, orthogonal projections $P_1,\ldots,P_n$ on $\mathbb C^d$, and density matrix $\rho$, we have $-c_n\le\mu_n\le1$. The lower bound is attained in dimension $n$ by real codimension-one projections and a pure state. For $n=1$ the zero projection suffices. The upper bound $1$ is also attained.

$$
0\le c_n<\tfrac13,\quad c_n\uparrow\tfrac13,\qquad
c_2=\tfrac18,\quad c_3=\tfrac{81}{448},\quad c_4=\tfrac{279841}{1315328},
\qquad \tfrac13-c_n\sim\tfrac{16}{27n}.
$$

The infimum across all lengths and dimensions is $-1/3$, unattained at any finite length.
:::

::: {.proof #pf-sharp-bounds}
**Reduce the matrix problem to a quadratic.** For Hermitian $X$, the notation $-cI\preceq X\preceq I$ means all its eigenvalues lie in $[-c,1]$. Let $0\le c\le1/3$. The interval has midpoint $a=(1-c)/2$ and half-width $b=(1+c)/2$, so $X=aI+bH$ for a Hermitian matrix $H$ with $\|H\|\le1$. Here the operator norm is the greatest length of the image of a unit vector. For a unit vector $\psi$ put $s=\|P\psi\|\in[0,1]$. Since $P=P^*=P^2$, we have $\langle\psi,P\psi\rangle=s^2$. Cauchy–Schwarz bounds $|\langle P\psi,H\psi\rangle|$ by $s$, giving

$$
as^2-bs\ \le\ \langle\psi,\mathcal J_P(X)\psi\rangle
=as^2+b\,\operatorname{Re}\langle P\psi,H\psi\rangle
\ \le\ as^2+bs\ \le\ 1.
$$

The lower parabola has its vertex at $y=b/(2a)=(1+c)/[2(1-c)]\in[1/2,1]$. Completing the square gives its minimum $-b^2/(4a)=-F(c)$. It follows that $-F(c)I\preceq\mathcal J_P(X)\preceq I$. Two identities keep the iteration within the range where this argument applies.

$$
F(c)-c=\frac{(1-3c)^2}{8(1-c)},\qquad
\tfrac13-F(c)=\frac{(1-3c)(c+5)}{24(1-c)}.
$$

Starting from $c_1=0$, the sequence strictly increases and stays below $1/3$. Starting with $P_n$ and iterating yields $-c_nI\preceq X_1\preceq I$. Taking an expectation in $\rho$ gives the two bounds. Identity projections attain $1$. Substituting $c_1,c_2,c_3$ into $F$ in turn gives the displayed fractions.

**Reach the bottom at every step.** First set $X=\operatorname{diag}(1,-c)$ in two dimensions, so $H=\operatorname{diag}(1,-1)$. Let $\alpha=\sqrt{(1-y)/2}$, $\beta=\sqrt{(1+y)/2}$, $\psi=(\alpha,\beta)^{\mathsf T}$, $p=(-\alpha,\beta)^{\mathsf T}$, and $P=pp^{\mathsf T}$. The two vectors are unit vectors, $p=-H\psi$, and $\langle p,\psi\rangle=y$. Thus $s=y$ and $\langle P\psi,H\psi\rangle=-y$, giving equality in both steps of the lower bound. Since $\mathcal J_P(X)$ is Hermitian with all eigenvalues at least $-F(c)$, a unit vector attaining the bound is an eigenvector for $-F(c)$.

In real dimension $n$ take an orthonormal basis $e_0,\ldots,e_{n-1}$ and start with $X^{(1)}=P_n=I-e_0e_0^{\mathsf T}$ and $v_1=e_0$. At stage $r$ let $v_r$ be the unit eigenvector for $-c_r$ in the coordinates used so far, with each $e_k$ for $k\ge r$ still an eigenvector of eigenvalue $1$. Apply the two-dimensional construction in the plane with basis $(e_r,v_r)$. With $\alpha_r,\beta_r$ calculated from $c_r$, set

$$
q_r=\beta_r e_r+\alpha_r v_r,\qquad P_{n-r}=I-q_rq_r^{\mathsf T},
\qquad v_{r+1}=\alpha_r e_r+\beta_r v_r.
$$

The direction $q_r$ is unit, so $P_{n-r}$ is a codimension-one projection. In the chosen plane it projects onto $-\alpha_r e_r+\beta_r v_r$, and on the perpendicular complement it is the identity. Hence $X^{(r+1)}=\mathcal J_{P_{n-r}}(X^{(r)})$ has eigenvalue $-c_{r+1}$ at $v_{r+1}$ and still fixes every $e_k$ for $k>r$. The pure state of $v_n$ therefore attains $-c_n$. At $n=1$ the initial zero projection already gives equality. Appending identity blocks embeds the construction in any $d\ge n$.

**Pass to long sequences.** Monotonicity gives a limit, and continuity of $F$ on $[0,1/3]$ makes it a fixed point. The formula for $F(c)-c$ gives $1/3$ as the sole fixed point. Put $\delta_n=1/3-c_n>0$. Substitution yields

$$
\delta_{n+1}=\delta_n\frac{16-3\delta_n}{16+24\delta_n},
\qquad
\frac1{\delta_{n+1}}-\frac1{\delta_n}
=\frac{27}{16-3\delta_n}\longrightarrow\frac{27}{16}.
$$

Sum these consecutive differences and divide by $n$. The first term contributes zero in the limit, and the average of differences tending to $27/16$ also tends to $27/16$. Thus $1/(n\delta_n)\to27/16$. Every $c_n$ is strictly below $1/3$, and the equality construction approaches $-1/3$ as $n$ grows. This proves both the infimum and its nonattainment.

This is the argument of Theorem 1 in version 2. The [sources](README.md#sources) give the attribution for the one-step estimate, recurrence and rate. [Paper](https://doi.org/10.5281/zenodo.24212412)
:::

## How low can the ordered product go?

In their equation (25), Abbott and colleagues construct ordered weak values $w_n=\operatorname{Tr}(\rho P_n\cdots P_1)=-\cos^{n+1}(\pi/(n+1))$ that tend to $-1$. The pointer coefficient averages the two orders at each step. At $c=1/3$ the one-step estimate preserves the interval $[-1/3,1]$. The distance from its finite-length minimum to the reference point $-1$ is $1-c_n$, strictly above $2/3$ and decreasing to $2/3$. The construction gives the unrestricted-dimension minimum. Prescribed $d<n$ and the all-rank-one case with $n\ge3$ fall outside its scope. [Abbott et al.](https://arxiv.org/abs/1805.09364v3)
