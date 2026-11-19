# 有理数反例

用三维坐标 $(x,y,z)$ 表示箭头。第一个投影保留 $(1,1,-1)$ 所在的直线。第二个投影保留平面 $y=z$，把第二、第三坐标换成它们的平均值。第三个保留平面 $x=z$，把第一、第三坐标换成它们的平均值。这三个保留空间的维数分别是 $1,2,2$。取初态 $\psi=e_3=(0,0,1)^{\mathsf T}$。

令 $B=P_2P_3+P_3P_2$。把两个平面投影按两个次序各做一遍，得到

$$
P_2P_3e_3=(1/2,1/4,1/4)^{\mathsf T},\qquad
P_3P_2e_3=(1/4,1/2,1/4)^{\mathsf T}.
$$

第一个投影给出 $P_1e_3=(-1,-1,1)^{\mathsf T}/3$。由于 $P_1$ 与 $B$ 都是实对称矩阵，四项展开的期望可合并为两向量的点积。

$$
\mu_3=\tfrac14\langle e_3,(P_1B+BP_1)e_3\rangle
=\tfrac12\langle P_1e_3,Be_3\rangle
=\tfrac12\frac{-3/4-3/4+1/2}{3}=-\tfrac16.
$$

$Be_3$ 的三个坐标都为正，但 $P_1e_3$ 的前两个坐标为负，它们对点积的贡献超过了正项。原来低于 $-1/8$ 所需的负号，就出在这个内积里。

::: {.theorem #pointer-refutation title="普遍 −1/8 下界的反例" lean="D5/S3/Quantum/Measurement/Weak/SequentialWeakPointerRefutation.result" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s1"}
对所有有限维空间、所有正长度、所有正交投影和所有单位纯态都满足 $\mu_n\ge -1/8$ 的命题为假。
:::

上面的计算是原论文 §3 给出的反例。Lean 定理以三维纯态和这三个投影证明这一否定命题。对 $n$ 个投影，$X_1$ 的每一层各带一个 $1/2$，因此与 Lean 将 $2^{-(n-1)}$ 一次提出的定义一致。要知道 $-1/6$ 以下还能走多远，需要[每个长度的精确界](bounds.md)。
