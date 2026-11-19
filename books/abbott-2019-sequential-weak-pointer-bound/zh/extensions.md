# 有限强度与其他观测量

投影只允许特征值 $0$ 和 $1$。如果一个操作在某个方向上只保留一部分，例如将分量乘以 $1/2$，精确界还成立吗？

::: {.corollary #positive-contractions title="正压缩算子" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s2" status="written-proof" proof="pf-positive-contractions" doi="10.5281/zenodo.24212412" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/275"}
允许每个 $P_j$ 换成 $\mathbb C^d$ 上的正压缩算子 $0\preceq A_j\preceq I$，并使用同样的 Jordan 递推。对每个 $n\ge1$，在所有有限维数、这样的 $A_j$ 和密度矩阵上，精确最小值仍为 $-c_n$，最大值仍为 $1$。
:::

::: {.proof #pf-positive-contractions}
设 $A$ 的不同正特征值为 $0<\lambda_1<\cdots<\lambda_k\le1$，取 $\lambda_0=0$。令 $E_i$ 投影到特征值至少为 $\lambda_i$ 的特征空间之和。则

$$
A=\sum_{i=1}^k(\lambda_i-\lambda_{i-1})E_i+(1-\lambda_k)0.
$$

在特征值为 $\lambda_j$ 的方向上，前 $j$ 项的权重相加恰为 $\lambda_j$。在零特征空间上所有项都为零。整个和的权重非负且总和为 $1$。若 $A=0$，直接用权重为 $1$ 的零投影。期望对每个输入都线性，所以分别展开每个 $A_j$，得到若干投影序列的期望的加权平均，权重是各项权重的乘积。每一项都在 $[-c_n,1]$。投影本身也满足 $0\preceq P_j\preceq I$，因而仍可用原构造达到两端。[版本 2，推论 2](https://doi.org/10.5281/zenodo.24212412)
:::

## 高斯指针怎样留下 Jordan 乘积？

对第 $j$ 支指针，取独立、实且中心为零的高斯波函数 $\phi_j(x)=(2\pi\sigma_j^2)^{-1/4}e^{-x^2/(4\sigma_j^2)}$，其中 $\sigma_j>0$。其位置密度 $|\phi_j|^2$ 的方差为 $\sigma_j^2$。第 $j$ 次耦合为 $e^{-ih_jP_j\otimes p_j}$，其中 $p_j$ 是指针动量算子，$\hbar=1$。它沿不同投影分量让指针平移 $0$ 或 $h_j$。

::: {.corollary #gaussian-envelope title="有限强度高斯包络" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s3" status="written-proof" proof="pf-gaussian-envelope" doi="10.5281/zenodo.24212412" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/276"}
对任意 $n\ge1$、有限维正交投影、密度矩阵、独立的上述高斯指针，以及任意正耦合 $h_j$，归一化读数乘积 $m_n=\mathbb E[x_1\cdots x_n]/\prod_j h_j$ 满足 $-c_n\le m_n\le1$。最后一支指针的宽度和耦合强度不影响 $m_n$。
:::

::: {.proof #pf-gaussian-envelope}
写 $E_0=I-P$、$E_1=P$，一次归一化读数的平均由左右两个投影分量 $a,b\in\{0,1\}$ 配对得到。对波函数乘积配方，得到中心在 $h(a+b)/2$ 的高斯密度，乘上重叠因子。

$$
\int_{\mathbb R}\frac{x}{h}\phi(x-ah)\phi(x-bh)\,dx
=\frac{a+b}{2}\exp\!\left[-\frac{h^2(a-b)^2}{8\sigma^2}\right].
$$

把积分当作 $E_aYE_b$ 的系数，$(0,0)$ 给零，$(1,1)$ 给 $PYP$，两个交叉项分别带系数 $t/2$，其中 $t=e^{-h^2/(8\sigma^2)}$。于是一次作用的映射为

$$
T_{P,t}(Y)=t\mathcal J_P(Y)+(1-t)PYP.
$$

每支指针只耦合一次，且各指针独立，故乘积平均的各积分可以逐个做。把各坐标的加权积分按从最后一次到第一次的次序应用在末端的 $I$ 上，得到 $m_n=\operatorname{Tr}[\rho\,T_{P_1,t_1}\cdots T_{P_n,t_n}(I)]$。由于 $T_{P_n,t_n}(I)=P_n$，最后一个 $t_n$ 消失。

若 $-cI\preceq Y\preceq I$，则 $-cP\preceq PYP\preceq P$，所以 $PYP$ 仍在 $[-cI,I]$ 内。Jordan 项在 $[-F(c)I,I]$ 内。因为 $F(c)\ge c$ 且 $0<t\le1$，加权平均也在后一个区间内。从 $P_n$ 出发归纳即得包络。

令 $h_j=\varepsilon g_j$，固定 $n$、$\rho$、$P_j$、$\sigma_j$ 和 $g_j>0$ 后取 $\varepsilon\downarrow0$。每个 $t_j\to1$，有限次映射复合直接趋于 Jordan 递推，故 $m_n\to\mu_n$。因此可通过改变耦合逼近弱极限的下端点。若预先固定所有正耦合，求其精确最小值需要另一个论证。[版本 2，§1 与推论 3](https://doi.org/10.5281/zenodo.24212412)
:::

## 哪些情形不会越出光谱乘积的范围？

::: {.corollary #commuting-symmetric title="对易投影与对称光谱" mathesis="collected:abbott-2019-sequential-weak-pointer-bound:2:s4" status="written-proof" proof="pf-commuting-symmetric" doi="10.5281/zenodo.24212412" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/277"}
若所有正交投影两两对易，则 $0\le\mu_n\le1$，且上述高斯模型满足 $0\le m_n\le1$。若改用任意厄米观测量 $A_1,\ldots,A_n$，其嵌套 Jordan 系数的绝对值不超过 $\prod_j\|A_j\|$。若每个观测量的光谱都关于零对称，则该系数位于从各光谱各取一值所得乘积的最小值与最大值之间。
:::

::: {.proof #pf-commuting-symmetric}
对易时，递推中的 $Y$ 与 $P$ 对易，因此 $PY=YP=PYP$。两种递推都给出 $P_1\cdots P_n$，其自伴性和幂等性来自两两对易，故其期望在 $[0,1]$。对一般厄米矩阵，三角不等式和范数的次乘性给出 $\|(AY+YA)/2\|\le\|A\|\|Y\|$。向外逐层应用，再用 $|\operatorname{Tr}(\rho X_1)|\le\|X_1\|$，即得乘积界。若每个光谱关于零对称，每个非零矩阵都具有两个极端特征值 $\pm\|A_j\|$。取这些值便能得到乘积的两个极端 $\pm\prod_j\|A_j\|$。若有零矩阵，所有乘积都为零，系数也由范数界知为零。[版本 2，推论 4](https://doi.org/10.5281/zenodo.24212412)
:::

## 形式化贡献

Lean 已证明三维反例所推出的普遍下界的否定。定理 1 的任意长度界、取等构造和渐近式，以及三个推论各有独立的形式化任务。贡献者可在相应请求中协调范围，并从自己的分支向 trureturing 的 $\,\texttt{dev}\,$ 提交聚焦的 PR。[贡献指南](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md) · [版本 2 的 Mathesis 记录](https://mathesis-omega-research.apps.chrono-ai.fun/papers/abbott-2019-sequential-weak-pointer-bound?version=2)

- [任意长度的精确界与取等](https://github.com/the-omega-institute/trureturing-requests/issues/274)
- [正压缩算子的精确界](https://github.com/the-omega-institute/trureturing-requests/issues/275)
- [有限强度高斯包络](https://github.com/the-omega-institute/trureturing-requests/issues/276)
- [对易投影与对称光谱](https://github.com/the-omega-institute/trureturing-requests/issues/277)
