# 每个长度的精确界

从 $X_n=P_n$ 开始，特征值介于 $0$ 和 $1$。向外再套一层 Jordan 乘积，最小特征值可以跌到 $-1/8$。下面的定理给出每一步最远能跌到哪里。

::: {.theorem #sharp-bounds title="精确的有限长度界" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s1" status="written-proof" proof="pf-sharp-bounds" doi="10.5281/zenodo.24212412" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/274"}
令 $c_1=0$，$c_{r+1}=F(c_r)$，其中 $F(c)=(1+c)^2/[8(1-c)]$。对任意 $n\ge1$、任意有限维数 $d\ge1$、$\mathbb C^d$ 上的正交投影 $P_1,\ldots,P_n$ 和密度矩阵 $\rho$，有 $-c_n\le\mu_n\le1$。下界可在 $n$ 维用实的余维一投影和纯态达到。$n=1$ 时取零投影即可。上界 $1$ 也可达到。

$$
0\le c_n<\tfrac13,\quad c_n\uparrow\tfrac13,\qquad
c_2=\tfrac18,\quad c_3=\tfrac{81}{448},\quad c_4=\tfrac{279841}{1315328},
\qquad \tfrac13-c_n\sim\tfrac{16}{27n}.
$$

因此跨所有长度和维数的下确界为 $-1/3$，有限长度均达不到。
:::

::: {.proof #pf-sharp-bounds}
**把矩阵问题变成二次函数。** 对厄米矩阵，$-cI\preceq X\preceq I$ 表示其特征值全在 $[-c,1]$。设 $0\le c\le1/3$。区间的中点和半宽是 $a=(1-c)/2$、$b=(1+c)/2$，所以 $X=aI+bH$，其中 $H$ 厄米且算子范数 $\|H\|\le1$。范数是矩阵能把单位向量拉伸到的最大长度。对单位向量 $\psi$，令 $s=\|P\psi\|\in[0,1]$。因为 $P=P^*=P^2$，有 $\langle\psi,P\psi\rangle=s^2$。Cauchy–Schwarz 不等式给出 $|\langle P\psi,H\psi\rangle|\le s$，于是

$$
as^2-bs\ \le\ \langle\psi,\mathcal J_P(X)\psi\rangle
=as^2+b\,\operatorname{Re}\langle P\psi,H\psi\rangle
\ \le\ as^2+bs\ \le\ 1.
$$

左边的抛物线最低点在 $y=b/(2a)=(1+c)/[2(1-c)]\in[1/2,1]$。配方得到最低值 $-b^2/(4a)=-F(c)$。因此 $-F(c)I\preceq\mathcal J_P(X)\preceq I$。迭代所需的区间条件来自两个恒等式

$$
F(c)-c=\frac{(1-3c)^2}{8(1-c)},\qquad
\tfrac13-F(c)=\frac{(1-3c)(c+5)}{24(1-c)}.
$$

从 $c_1=0$ 出发，$c_n$ 严格增加且始终低于 $1/3$。从 $P_n$ 开始归纳得 $-c_nI\preceq X_1\preceq I$，取密度矩阵期望即得两侧界。所有投影取 $I$ 达到上界。将 $c_1,c_2,c_3$ 依次代入 $F$ 给出所列分数。

**让每一步都恰好触底。** 先在二维令 $X=\operatorname{diag}(1,-c)$，故 $H=\operatorname{diag}(1,-1)$。设 $\alpha=\sqrt{(1-y)/2}$，$\beta=\sqrt{(1+y)/2}$，$\psi=(\alpha,\beta)^{\mathsf T}$，$p=(-\alpha,\beta)^{\mathsf T}$，$P=pp^{\mathsf T}$。两向量都是单位向量，$p=-H\psi$，$\langle p,\psi\rangle=y$。于是 $s=y$，而 $\langle P\psi,H\psi\rangle=-y$，两项取等条件同时满足。因 $\mathcal J_P(X)$ 厄米且下界是 $-F(c)$，取等的 $\psi$ 是特征值 $-F(c)$ 的特征向量。

在实 $n$ 维空间取标准正交基 $e_0,\ldots,e_{n-1}$，从 $X^{(1)}=P_n=I-e_0e_0^{\mathsf T}$ 和 $v_1=e_0$ 开始。第 $r$ 步令 $v_r$ 是已用坐标空间中对应 $-c_r$ 的单位向量，其余 $e_k$（$k\ge r$）仍有特征值 $1$。在基 $(e_r,v_r)$ 的平面使用上述二维构造。用 $c_r$ 算出的系数记为 $\alpha_r,\beta_r$，令

$$
q_r=\beta_r e_r+\alpha_r v_r,\qquad P_{n-r}=I-q_rq_r^{\mathsf T},
\qquad v_{r+1}=\alpha_r e_r+\beta_r v_r.
$$

$q_r$ 为单位向量，所以 $P_{n-r}$ 是余维一投影。它在该平面投到 $-\alpha_r e_r+\beta_r v_r$ 的方向，在平面的正交补上为恒等。$X^{(r+1)}=\mathcal J_{P_{n-r}}(X^{(r)})$ 因此在 $v_{r+1}$ 上有特征值 $-c_{r+1}$，且仍固定 $e_k$（$k>r$）。最终取 $v_n$ 的纯态恰好得到 $-c_n$。$n=1$ 时初始零投影已经取等。加上恒等块可以把构造放进任意 $d\ge n$。

**长序列的极限。** 单调性给出极限，$F$ 在 $[0,1/3]$ 连续，所以极限是它的固定点。由 $F(c)-c$ 的公式，唯一固定点是 $1/3$。令 $\delta_n=1/3-c_n>0$。代入得到

$$
\delta_{n+1}=\delta_n\frac{16-3\delta_n}{16+24\delta_n},
\qquad
\frac1{\delta_{n+1}}-\frac1{\delta_n}
=\frac{27}{16-3\delta_n}\longrightarrow\frac{27}{16}.
$$

把相邻差相加后除以 $n$，首项贡献趋于零，趋于 $27/16$ 的差值的平均也趋于 $27/16$。因此 $1/(n\delta_n)\to27/16$。每个 $c_n$ 严格小于 $1/3$，取等构造又能随 $n$ 逼近 $-1/3$，这证明了下确界及其不可达性。

论证来自版本 2 的定理 1。一步谱估计、递推和收敛率的来源见[文献](README.md#文献与来源)。[原论文](https://doi.org/10.5281/zenodo.24212412)
:::

## 另一个乘积能走到哪里？

Abbott 等人在式 (25) 中构造有序弱值 $w_n=\operatorname{Tr}(\rho P_n\cdots P_1)=-\cos^{n+1}(\pi/(n+1))$，它随 $n$ 趋向 $-1$。指针系数每一步都做次序平均，在 $c=1/3$ 时一步估计保持整个区间 $[-1/3,1]$。其最小值与参照点 $-1$ 的距离 $1-c_n$ 严格大于 $2/3$，并趋于 $2/3$。在固定 $d<n$ 或所有投影都要求秩一且 $n\ge3$ 的情况下，这个构造没有给出精确最小值。[Abbott 等人](https://arxiv.org/abs/1805.09364v3)
