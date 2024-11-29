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