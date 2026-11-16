## 模糊算子

### 1. 三角范数与对偶

**定义 1**（三角范数）：称 $I=[0,1]$ 区间上的二元算子 $T$ 是一个三角范数，$\forall a,b,c \in I$, 若 $T$ 满足：1. $T(a,b)=T(b,a)$; 2. $T(T(a,b),c)=T(a,T(b,c))$; 3. 若 $a \leq c, b \leq d$, 则 $T(a,b) \leq T(c,d)$; 4. $T(a,1)=a, \forall a \in I$.

**定义 2**（三角余数）：称 $I=[0,1]$ 区间上的二元算子 $S$ 是一个三角余数，$\forall a,b,c \in I$, 若 $S$ 满足：1. $S(a,b)=S(b,a)$; 2. $S(S(a,b),c)=S(a,S(b,c))$; 3. 若 $a \leq c, b \leq d$, 则 $S(a,b) \leq S(c,d)$; 4. $S(a,0)=a, \forall a \in I$.

**定义 3**（补算子）：称 $N: [0,1] \to [0,1]$ 是补算子，若 $N$ 满足：1. $N$ 单调递减；2. $N(0)=1, N(1)=0$.

**例 4**（标准补算子）：$N(a) = 1-a,\forall a \in I$. 

**定义 5**（$T$ 和 $S$ 关于 $N$ 对偶）：称 $T$ 和 $S$ 关于 $N$ 对偶，若 $\forall a,b \in I$, 都有 $S(a,b) = N(T(N(a), N(b))), T(a,b) = N(S(N(a), N(b)))$.

**定义 6**（$T$ 的剩余蕴含算子）：给定三角范数 $T$, 定义 $T$ 诱导的蕴含算子 $\theta$ 为
$$\theta(a,b) = \sup\{c \in I: T(a,c)\leq b\}.$$ 特别地，当 $T$ 下半连续时，$\theta$ 被称为 $T$ 诱导的剩余蕴含算子。

**定义 7**（$S$ 的剩余蕴含算子）：给定三角余数 $S$, 定义 $S$ 诱导的蕴含算子 $\sigma$ 为
$$\sigma(a,b) = \inf\{c \in I: S(a,c)\geq b\}.$$ 特别地，当 $S$ 下半连续时，$\theta$ 被称为 $S$ 诱导的剩余蕴含算子。

$$
\begin{align*}
T\overset{N}{\longleftrightarrow}S\\
\downarrow\hspace{27pt}\downarrow\\
\theta\hspace{2pt}\overset{N}{\longleftrightarrow}\sigma
\end{align*}
$$

### 2. 模糊集的范数交和余数并

<!-- 为什么用范数定义并，余数定义交 ？ -->

**定义 8**：给定三角范数、三角余数和补算子分别为 $T, S, N$, 且 $T$ 和 $S$ 关于 $N$ 对偶。设 $A,B C \in F(U)$, 则：
1. 如果 $\forall x \in U, C(x) = S(A(x), B(x))$, 记 $C = A \cup_S B$, 并称 $C$ 是 $A$ 和 $B$ 关于 $S$- 余数的并；
2. 如果 $\forall x \in U, C(x) = T(A(x), B(x))$, 记 $C = A \cap_T B$, 并称 $C$ 是 $A$ 和 $B$ 关于 $T$- 范数的并；

## 模糊粗糙集的数学基础

设信息系统 $IS = \langle U,A \rangle$, 其中论域 $U = \{x_1, x_2, \cdots, x_n\}$ 且 $A$ 表示属性集，包括条件属性集 $C$ 和决策属性集 $D$. 任取 $x \in U$ 以及 $a \in C$, $x^a$ 表示样本 $a$ 在条件属性 $a$ 下的值。

设 $F \in U^{[0,1]}$, 称 $F$ 是 $U$ 上的模糊集。$U$ 上的模糊关系定义为 $R: U \times U \to [0,1]$. 任取 $(x,y) \in U \times U$, $R(x, y)$ 表示样本 $x$ 和 $y$ 在模糊关系 $R$ 下的相关程度。模糊关系 $R$ 还可用矩阵 $M(R)=(r_{ij})_{n\times n}$ 来描述，其中每行代表一个模糊集且 $r_{ij}=R(x_i, x_j)$. 

### 1. 模糊 $T$- 等价关系及其上的模糊逼近

称模糊关系 $R$ 是一个模糊等价关系，如果 $R$ 对任意 $x,y,z \in U$ 满足：1. $R(x, x)=1$; 2. $R(x,y) = R(y,z)$; 3. $\max_{y \in U}\min(R(x,y), R(y,z)) \leq R(x,z)$. 显然模糊等价关系对应的关系矩阵在主对角线元上全为 $1$ 且是对称矩阵。设 $T$ 为模糊算子，若将传递性$3$替换为：$T(R(x,y),R(y,z)) \leq R(x,z)$, 则称 $R$ 是模糊 $T$- 等价关系。
 
任取条件属性 $C$ 的子集 $B$, $B$ 上的 模糊关系 $R_B$ 可将论域 $U$ 划分为模糊信息粒子簇 $IG(R_B) = \{ [x_1]_B, [x_2]_B, \cdots, [x_n]_B \}$, 其中 $[x_i]_B=(r_{i1}^B, r_{i2}^B, \cdots, r_{in}^B)$ 表示 $x_i$ 上的模糊信息粒子。$IG(R_B)$ 称作模糊粒化结构。$[x_i]_B$ 的基数为 $\vert [x_i]_B \vert=\sum_{j=1}^n R_B(x_i,x_j)$.

**定义 1**（上下近似）给定信息系统 $IS=\langle U,A \rangle$. 任取条件属性子集 $B$ 和样本 $x \in U$, 令 $U$ 上的模糊关系 $R_B$ 和 模糊集 $F$. 则模糊集 $F$ 在模糊关系 $R_B$ 下的上下近似是：$$\begin{align*}
\underline{R_B}F(x) &= \inf_{y \in U}\max\{\mathcal{N}(R_B(x,y)), F(y)\}, \\
\overline{R_B}F(x) &= \sup_{y \in U}\min\{R_B(x,y), F(y)\},
\end{align*}
$$ 其中 $\mathcal{N}: [0,1] \to [0,1]$ 是标准补算子，即 $\mathcal{N}(x)=1-x, \forall x \in I$.

<!-- 为什么使用 $\inf_{y \in U}\max$ 的结构定义 $x$ 在模糊集 $F$ 的下近似 $\underline{R_B}F$ 下的隶属度 ？ -->

一般模糊关系上的一般模糊粗糙集模型：

**定义 1'**（上下近似）给定信息系统 $IS=\langle U,A \rangle$. 任取条件属性子集 $B$ 和样本 $x \in U$, 令 $U$ 上的模糊关系 $R_B$ 和 模糊集 $F$. 则模糊集 $F$ 在模糊关系 $R_B$ 下的上下近似是：$$\begin{align*}
\underline{R_B}F(x) &= \inf_{y \in U}S(\mathcal{N}(R_B(x,y)), F(y)), \\
\overline{R_B}F(x) &= \sup_{y \in U}T(R_B(x,y), F(y)),
\end{align*}
$$ 其中 $T: [0,1] \times [0,1] \to [0,1]$ 是 $[0,1]$ 上的[三角范数](../notes/fuzzy_operator.md)，$S$ 是 $[0,1]$ 上的[三角余数](../notes/fuzzy_operator.md)。

<!-- [《应用粗糙计算》中还给出两种基于模糊 $T$- 等价关系的上下近似](../reference/books/应用粗糙计算.pdf) -->