# 0x36 组合计数

## 基本概念

[排列组合](https://oi-wiki.org/math/combinatorics/combination/)：加法原理、乘法原理、排列数、组合数

### 组合数的求法

首先易得组合数有三个性质：

$$
\begin{aligned}&1.C_{n}^{m}=C_{n}^{n-m}\\&2.C_{n}^{m}=C_{n-1}^{m}+C_{n-1}^{m-1}\\&3.C_{n}^{0}+C_{n}^{1}+C_{n}^{2}+\cdots+C_{n}^{n}=2^{n}\end{aligned}
$$

根据性质 2 可以用递推法在 $O(n^2)$ 内求出 $0 \leq y \leq x \leq n$ 的所有组合数 $C_x^y$。

若题目要求 $C_n^m$ 对 $p$ 取模后的值，且均存在乘法逆元，则可以先计算分子的取模，然后算分母取模的逆元，然后相乘。时间复杂度为 $O(n)$。

若在计算阶乘的过程中，将 $0\leq k\leq n$ 的每个 `k! mod p` 及其逆元分别保存在 `jc` 和 `jc_inv` 中，则可以在 $O(n\log n)$ 的预处理后以 $O(1)$ 的时间回答 $0\leq y\leq x\leq n$ 的所有组合数 $C_x^y \bmod p=$ `jc[x] * jc_inv[y] * jc_inv[x-y] mod p`。

若题目要求对 $C_n^m$ 进行高精度运算，为了避免除法，可以用阶乘分解的做法，把分子和分母快速分解质因数，在数组中保存各项质因子的指数，然后对应相减消去分母，最后把剩余的质因子乘起来。时间复杂度为 $O(n\log n)$。

[二项式定理](https://oi-wiki.org/math/combinatorics/combination/#%E4%BA%8C%E9%A1%B9%E5%BC%8F%E5%AE%9A%E7%90%86)

### AcWing 211 计算系数

题意：给定多项式 $(ax+by)^k$ 要求求出多项式展开后 $x^ny^m$ 的系数。

二项式定理长这样：

$$(a+b)^k=\sum_{i=0}^kC_k^ia^ib^{k-i}$$

所以 $x^ny^m$ 的系数是 $C_k^na^nb^m$，可以用快速幂和逆元计算。

```c++
int qmi(int a, int k){
    a %= mod;
    int res = 1 % mod;
    while (k){
        if (k & 1) res = res * a % mod;
        a = a * a % mod; k >>= 1;
    }
    return res;
}

int main(){
    int a, b, k, n, m;
    scanf("%d%d%d%d%d", &a, &b, &k, &n, &m);
    int res = qmi(a, n) * qmi(b, m) % mod;
    for (int i = 1, j = k; i <= n; i ++ , j -- ) {
        res = res * j % mod;
        // 费马小定理，当然也可以用扩展 GCD 解线性同余方程
        res = res * qmi(i, mod - 2) % mod; 
    }
    printf("%d\n", res); return 0;
}
```

## 多重集

多重集是指包含重复元素的广义集合，设 $S=\{ n_1a_1,n_2a_2,\cdots,n_ka_k\}$ ，记 $n=n_1+\cdots+n_k$，$S$ 的全排列个数（多重集的排列数）为

$$\frac{n!}{n_1!n_2!\cdots n_k!}$$

从 $S$ 中取出 $r$ （$r\leq n_i$）个元素组成一个多重集（不考虑元素顺序），所产生不同多重集的数量（特殊情况下多重集的组合数）为

$$C_{k+r-1}^{k-1}$$

上式等价于 $r$ 个 $0$ 和 $k-1$ 个 $1$ 组成的多重集的全排列个数，其中 $k-1$ 个 $1$ 将 $r$ 个 $0$ 分成 $k$ 组，每组 $0$ 的数量对应 $x_i$。对于更一般的 $r$ 的情况详见 0x37 章。

### AcWing 212 计数交换

题意：（将全排列变成递增序列的最小交换次数，以及最小交换次数下的方案数）给定一个全排列 p1,p2,...,pn，可进行若干次操作，每次选择两个整数 x,y，交换 px,py。设把 p1,p2,...,pn 变成单调递增的排列 1,2,...,n 至少需要 m 次交换。求有多少种操作方法可以只用 m 次交换达到上述目标，输出结果对 10e9+9 取模之后的值。

思路 [@扶摇直上九万里](https://www.acwing.com/solution/content/7776/)：

对于一个排列 p1,p2,...,pn，每个 pi 向 i 连一条边，构成一张由若干个环组成的图。目标状况为 n 个自环。用数学归纳法可以证明，将一个长度为 n 的环变成 n 个自环，至少需要 n-1 次操作。

设 Fn 表示用最少的步数将一个长度为 n 的环变成 n 个自环，共有多少种方法。设 $T(x,y)$ 表示有多少种交换方法可以把长度为 n 的环变成长度为 x 和 y 的两个环（$x+y=n$），显然

$$
T(x,y) = 
\begin{cases}
     \frac{n}{2}, &x=y \\
     n, &x\neq y
\end{cases}
$$

根据多重集的排列数、加法原理、乘法原理可得两个环的方法数为

$$
F_n = \sum_{x+y=n}T(x,y)*F_x*F_y*\frac{(n-2)!}{(x-1)!(y-1)!}
$$

最初的排列可能存在 k 个环，长度分别为 l1, l2, ..., lk，那么最终的答案就是

$$
F_n = F_{l_1}*F_{l_2}*\cdots*F_{l_k}*\frac{(n-k)!}{(l_1-1)!(l_2-1)!*\cdots*(l_k-1)}
$$

```c++
void Init() {
    fc[0] = 1;  //阶乘 factorial
    for(int i=1;i<=1000;++i) fc[i] = fc[i-1] * i % mod;
    f[1] = 1;
    for(int i=2;i<=1000;++i) {
        for(int j=1;j<=i/2;++j) {   // (x,y)和(y,x)只能算一次 
            int inv = Pow(fc[i-j-1]*fc[j-1]%mod, mod-2);
            f[i] = (f[i] + f[i-j]*f[j]%mod*T(i-j,j)%mod*fc[i-2]%mod*inv%mod) % mod;
        }
    }
    for(int i=1;i<=10;++i) printf("%lld\n",f[i]);
}
```

用递推求 F 数组，可见时间复杂度为 $O(n^2\log n)$。观察可得 $F_n=n^{n-2}$，这样求时间复杂度为 $O(n\log n)$。

```c++
// @种花家的兔兔 https://www.acwing.com/solution/content/157472/
int main(){
    fac[0] = 1; 
    for (int i = 1; i < N; i ++ ) fac[i] = fac[i - 1] * i % mod;
    int T; scanf("%d", &T);
    while (T -- ) {
        int n; scanf("%d", &n);
        for (int i = 1; i <= n; i ++ ) scanf("%d", &p[i]);
        int cnt = 0; LL res = 1;
        memset(st, 0, sizeof st);
        for (int i = 1; i <= n; i ++ ){
            if (st[i]) continue;
            cnt ++ ; int l = 1; st[i] = true;
            for (int j = p[i]; j != i; j = p[j])
                l ++ , st[j] = true;
            if (l > 1) res = res * qmi(l, l - 2) % mod;
            res = res * qmi(fac[l - 1], mod - 2) % mod;
        }
        res = res * fac[n - cnt] % mod;
        printf("%lld\n", res);
    }
    return 0;
}
```