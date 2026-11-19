# A rational counterexample

Use coordinates $(x,y,z)$ for an arrow in three dimensions. The first projection retains the line through $(1,1,-1)$. The second retains the plane $y=z$ by averaging the second and third coordinates. The third retains $x=z$ by averaging the first and third coordinates. Their ranks are $1,2,2$. Start in the unit state $\psi=e_3=(0,0,1)^{\mathsf T}$.

Write $B=P_2P_3+P_3P_2$. Applying the plane projections in both orders gives

$$
P_2P_3e_3=(1/2,1/4,1/4)^{\mathsf T},\qquad
P_3P_2e_3=(1/4,1/2,1/4)^{\mathsf T}.
$$

The first projection gives $P_1e_3=(-1,-1,1)^{\mathsf T}/3$. Since $P_1$ and $B$ are real symmetric, the expectation of the four-term expansion reduces to one dot product.

$$
\mu_3=\tfrac14\langle e_3,(P_1B+BP_1)e_3\rangle
=\tfrac12\langle P_1e_3,Be_3\rangle
=\tfrac12\frac{-3/4-3/4+1/2}{3}=-\tfrac16.
$$

All three coordinates of $Be_3$ are positive. The first two coordinates of $P_1e_3$ are negative, and their contributions to the dot product outweigh the positive term. That gives the value below $-1/8$.

::: {.theorem #pointer-refutation title="Refutation of the universal −1/8 bound" lean="D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.result" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s1"}
The assertion that $\mu_n\ge -1/8$ for all finite dimensions, positive lengths, orthogonal projections and unit pure states is false.
:::

This is the witness in §3 of the paper. The Lean theorem proves the negation using these three projections and the indicated pure state. The recursion defining $X_1$ inserts a factor of $1/2$ at each step, matching the single factor $2^{-(n-1)}$ in the Lean definition for $n$ projections. The [sharp bound at each length](bounds.md) determines how much further below $-1/6$ the coefficient can go.
