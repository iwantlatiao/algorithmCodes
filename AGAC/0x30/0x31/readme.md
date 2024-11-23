# 0x31 质数

## 质数的判定

### 试除法

对于整数 N ，扫描 2 到 根号 N 之间的所有整数，看能不能整除 N。如果都不能则 N 是质数，否则为合数。

```c++
bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0) return false;
    return true;
}
```

## 质数的筛选

### 埃氏筛法

思路：任意整数 x 的整数倍都不是质数。

时间复杂度为 $O(NloglogN)$

```c++
void primes(int n) {
    memset(v, 0, sizeof v);  // 合数标记
    for (int i = 2; i <= n; i++) {
        if (v[i]) continue;
        cout << i << endl;   // i 是质数
        for (int j = i; i * j <= n; j++) v[i * j] = 1;
    }
}
```

### 线性筛（欧拉筛）

虽然埃氏筛法从 `i*i` 开始标记合数，但是仍然会重复标记。例如 12 会被 2 和 3 标记，根本原因是没有确定出唯一产生 12 的方式。

线性筛通过记录每个数的最小质因子实现合数被唯一地筛出。线性筛的步骤如下：

1. 依次考虑 `2~N` 中的每个整数 i
2. 用数组 v 保存每个数的最小质因子。如果 `v[i] = 0` 说明 i 是质数，将其保存至质数数组 prime 中。
3. 扫描不大于 `v[i]` 的每个质数 p，由于 `p*i` 的最小质因子是 `p`，所以有 `v[i*p] = p`。

```c++
void primes(int n) {
    memset(v, 0, sizeof v)  // 最小质因数标记
    m = 0;  // 质数个数
    for (int i = 2; i <= n; i++) {
        if (v[i] == 0) { v[i] = i; prime[++m] = i; }  // i 是质数
        // 给当前的数 i 乘质因子 prime[j]
        for (int j = 1; j <= m; j++) {
            // prime[j] 不是 i 的最小质因子了，或者乘完超出范围
            if (prime[j] > v[i] || prime[j] * i > n) continue;
            v[prime[j] * i] = prime[j];
        }
    }
}
```

## 质因数分解

### 算数基本定理

任何一个大于 1 的正整数 N 都可以被唯一分解为有限个质数的乘积。

### 试除法

结合质数判定的试除法和埃氏筛法，可以扫描 2 到 根号 N 之间的所有整数 d，若 d 能整除 N，则从 N 中去掉所有 d。由于是从小到大扫，所以这些 d 一定都是质数。时间复杂度为 $O(sqrt(N))$

```c++
void divide(int n) {
    m = 0;  // 质因数的个数
    for (int i = 2; i <= sqrt(n); i++) 
        if (n % i == 0) {
            p[++m] = i, c[m] = 0;  // 质因数 p，质因数个数 c
            while (n % i == 0) n /= i, c[m]++;
        }
    if (n > 1) p[++m] = n, c[m] = 1;  // 剩下的也要算进去
}
```

### acwing 196 质数距离

题意：给定两个整数 L 和 U，找出闭区间 `[L, U]` 中距离最近和最远的相邻质数对。`1 < L < U < 2^31, U - L < 10^6`。

首先 L 和 U 的范围很大，所以不能直接用线性筛或试除法。但是由于区间很小，且一个合数 N 肯定有不大于 `sqrt(N)` 的质因子，所以其实只需要用筛法求 `2 ~ sqrt(N)` 的质数，然后用这些质数尝试筛掉 `[L, U]` 中的合数即可。

在尝试筛掉 `[L, U]` 中的合数时，实现方法是标记 `i * p` 是合数，其中 `ceil(L/p) < i < floor(R/p)`。我们希望将向上取整也转化为向下取整。这里介绍上下取整转换公式：

$$
\left\lceil\frac nm\right\rceil=\left\lfloor\frac{n+m-1}m\right\rfloor=\left\lfloor\frac{n-1}m\right\rfloor+1 
$$

$$
\left\lfloor\frac nm\right\rfloor=\left\lceil\frac{n-m+1}m\right\rceil=\left\lceil\frac{n+1}m\right\rceil-1
$$

[向上取整转化为向下取整的证明](https://blog.csdn.net/qq_41437512/article/details/128243628)：

两边同时减去 $\lfloor n / m \rfloor$，左边得到：

$$
\left\lceil\frac nm\right\rceil-\left\lfloor\frac nm\right\rfloor=\left\lceil\frac{n\mathrm{~mod~}m}m\right\rceil=\begin{cases}0,&\text{ 若 }n\mathrm{~mod~}m=0,\\1,&\text{ 若 }n\mathrm{~mod~}m>0.&\end{cases}
$$

右边：设 $n = mq + r$，且 $q = \lfloor n / m \rfloor$，$0 \leq r < m$，则

$$
\begin{aligned}
\left\lfloor\frac{n+m-1}{m}\right\rfloor-\left\lfloor\frac{n}{m}\right\rfloor & =\left\lfloor\frac{mq+m+r-1}m\right\rfloor-\left\lfloor\frac{mq+r}m\right\rfloor  \\
&=\left\lfloor\frac{r+m-1}m\right\rfloor-\left\lfloor\frac rm\right\rfloor \\
&=\left\lfloor\frac{r+m-1}m\right\rfloor \\
&=\left\lfloor\frac{n\mathrm{~mod~}m+m-1}m\right\rfloor \\
&=\begin{cases}0,&\text{ 若 }n\mathrm{~mod~}m=0,\\1,&\text{ 若 }n\mathrm{~mod~}m>0.&\end{cases}
\end{aligned}
$$

### acwing 197 阶乘分解

题意：给定整数 N，把阶乘 `N!` 分解质因数。`N < 1e6`。

如果将 `1~N` 每个数分别分解质因数，时间复杂度为 $O(N\sqrt N)$。

[@incra](https://www.acwing.com/solution/content/151488/)：考虑对于 `2~N` 内的每个质数 p，一次求出 `N!` 中有多少个 p。

假设要求 `9!` 中 2 的个数

```c++
1 2 3 4 5 6 7 8 9 // 8! 中 2 的个数可以分为 2^1 的 + 2^2 的 + 2^3 的
  1   1   1   1   // 2^1 的倍数个数 = floor(9 / 2)
      1       1   // 2^2 的倍数个数 = floor(9 / 2^2)
              1   // 2^3 的倍数个数 = floor(9 / 2^3)
```

可以发现，质因数 p 的数量是

$$
\lfloor \frac{N}{p} \rfloor + \lfloor \frac{N}{p^2} \rfloor + ... + \lfloor \frac{N}{p^{\lfloor log_p N \rfloor}} \rfloor = \sum_{p^k \leq N} \lfloor \frac{N}{p^k} \rfloor
$$

所以先用线性筛把 `2~N` 的素数筛出，然后对于每个素数 p 求上面的和式即可。