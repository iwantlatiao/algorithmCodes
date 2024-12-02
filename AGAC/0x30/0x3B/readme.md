# 总结与练习

## acwing 220 最大公约数

题意：给定 N 求 $1\leq x,y \leq N$ 且 $\mathrm{gcd}(x,y)$ 为素数的数对 x 和 y 有多少对。

思路 [@whsstory](https://www.acwing.com/solution/content/16737/)：$\mathrm{gcd}(x, y)=p$ 不好求。但是在 [acwing 201](../0x32/readme.md#acwing-201-可见的点) 中我们求过 $\mathrm{gcd}(x, y)=1$ ，可以转化为欧拉函数的求和。所以将公式进行变形：

$$\mathrm{gcd}(x, y)=p \Rightarrow \mathrm{gcd}(x/p, y/p)=1$$

也就变成求：

$$
\sum_{p\in P}\sum_{i=1}^n\sum_{j=1}^n[gcd(i,j)=p]
=\sum_{p\in P}\sum_{i=1}^{\lfloor\frac{n}{p}\rfloor}\sum_{j=1}^{\lfloor\frac{n}{p}\rfloor}[gcd(i,j)=1]
$$

所以只需要预处理出欧拉函数的前缀和，然后对于每一个素数都拿一个对应的欧拉函数前缀和即可。

## acwing 201 龙哥的问题

题意：给定 N 求 $\sum_{1\leq i\leq N}\mathrm{gcd}(i,N)$，$N < 2^{31}$。

思路 [@JcWing](https://www.acwing.com/solution/content/164700/)、[@这个显卡不太冷](https://www.acwing.com/solution/content/1185/)：

数论题第一时间没找到规律就先打个表。比如下面这张 N 为 50 的表：

```
1 2 1 2 5 2 1 2 1 10 1 2 1 2 5 2 1 2 1 10 1 2 1 2 25 2 1 2 1 10 1 2 1 2 5 2 1 2 1 10 1 2 1 2 5 2 1 2 1 50
```

发现有很多重复的数字。$\mathrm{gcd}(i,N)=1$ 表示 $i$ 与 $N$ 互质，个数可以用欧拉函数 $\phi(N)$ 计算。如何算 $\mathrm{gcd}(i,N)\neq 1$？考虑上一题，转化为 $\mathrm{gcd}(i,N)=1$ 的形式。

对于每一个 $\mathrm{gcd}(i,N)=d$ 的数对，都可以转化为 $\mathrm{gcd}(i/d,N/d) = 1$。所以满足 $\mathrm{gcd}(i,N)=d$ 的 $i$ 的个数可以通过 $\phi(N/d)$ 得出。

我们可以枚举 $N$ 的所有因数。对于单个因数，用定义式求解欧拉函数。还可以进一步优化，枚举时只枚举小于 $\sqrt(N)$ 的约数 $i$，就可以得到两个约数 $i$ 和 $N/i$ 。同时在预处理的时候先线性筛出 1e5 内的质数和欧拉函数。

```c++
// 线性筛
void get_primes(int n) {/*...*/}
// 求欧拉函数
int euler(int n) {
    int ans = n;
    for(int i = 0; i < cnt; i++) {
        if(primes[i] * primes[i] > n) break;
        if(n % primes[i] == 0) {
            ans = ans / primes[i] * (primes[i] - 1);
            while(n % primes[i] == 0) n /= primes[i];
        }
    }
    if(n > 1) ans = ans / n * (n - 1);
    return ans;
}
int main() {
    get_primes(N);  // N = 1e5
    ll n, ans = 0;
    cin >> n;
    for(int i = 1; (ll)i * i <= n; i++) {
        if(n % i == 0) {
            int t = n / i;
            if(t < N) ans += i * phi[t];  // 其实可以写进 int euler()
            else ans += i * euler(t);
            if(i != t) ans += t * phi[i];
        }
    }
    cout<<ans;
}
```

## acwing 222 青蛙的约会

题意：两只青蛙沿着一个圆上跳，他们的起点和速度不同，求什么时间点可以碰面。

思路 [@gongcharlie](https://www.acwing.com/solution/content/24456/)、[@JcWing](https://www.acwing.com/solution/content/165410/)：

设青蛙 A 一次跳 m 米，起点为 x，青蛙 B 一次跳 n 米，起点为 y，圆的长度为 L，公式化题意可得

$$
x + mt \equiv y + nt \pmod L \\ \Rightarrow (m-n)t \equiv y-x \pmod L \\
\Rightarrow (m-n)t +(- L)k = y - x
$$

根据拓展欧几里得算法可求解这个方程。

```c++
int mod (long long x, int y){ return (x % y + y) % y; }

int exgcd (int a, int b, int &x, int &y) {
    if (!b) {
        x = 1, y = 0;
        return a;
    }
    int g = exgcd (b, a % b, x, y), z = x;
    x = y, y = z - y * (a / b);
    return g;
}

int main () {
    scanf ("%d%d%d%d%d", &x, &y, &a, &b, &l);
    n = mod (x - y, l), m = mod (b - a, l);
    g = exgcd (m, l, qwq, awa);
    if (n % g) puts ("Impossible");
    else printf ("%d", mod ((long long) n / g * qwq, l / g));
    return 0;
}
```

## acWing 223 阿九大战朱最学

题意：中国剩余定理模板题

```c++
// @种花家的兔兔
// https://www.acwing.com/solution/content/164120/
LL exgcd(LL a, LL b, LL &x, LL &y){/*...*/}

int main() {
    int n; scanf("%d", &n);
    for (int i = 1; i <= n; i ++ ) scanf("%lld%lld", &m[i], &a[i]);
    LL M = 1, res = 0; for (int i = 1; i <= n; i ++ ) M *= m[i];
    for (int i = 1; i <= n; i ++ )
    {
        LL x, y, MM = M / m[i];
        exgcd(MM, m[i], x, y);  // Miti \eqiuv 1 \pmod mi
        res = (res + a[i] * MM % M * x) % M;
    }
    res = (res + M) % M;
    printf("%lld\n", res);
    return 0;
}
```

## acwing 230 排列计数

题意：求有多少种长度为 n 的序列 A，满足以下条件

1. 1 至 n 这 n 个数在序列中各出现了一次
2. 若第 i 个数 $A[i]$ 的值为 i，则称 i 是稳定的，序列恰好有 m 个数是稳定的。

思路 [@种花家的兔兔](https://www.acwing.com/solution/content/164343/)：首先确定哪 m 个数是 $A[i]=i$，然后剩下的数等价于错排，用[错排公式](https://www.cnblogs.com/cafu-chino/p/10109357.html)即可解决。计算公式为：

$$C_n^m * f(n-m)$$

其中错排公式 $f$ 的递推式为：

$$f(n) = (n-1)(f(n-1)+f(n-2))$$

```c++
int qmi(int a, int k) {/*...*/}

void init() {
    fac[0] = fac[1] = facinv[0] = facinv[1] = 1;
    fac[2] = 2, facinv[2] = qmi(2, mod - 2);
    f[0] = 1, f[1] = 0, f[2] = 1;
    for (int i = 3; i < N; i ++ ) {
        fac[i] = (LL)fac[i - 1] * i % mod;
        facinv[i] = qmi(fac[i], mod - 2);
        f[i] = ((LL)f[i - 1] + f[i - 2]) % mod * (i - 1) % mod;
    }
}

int c(int a, int b) {
    return (LL)fac[a] * facinv[b] % mod * facinv[a - b] % mod;
}

int main() {
    init(); int T; scanf("%d", &T);
    while (T -- ) {
        int n, m;
        scanf("%d%d", &n, &m);
        int res = (LL)c(n, m) * f[n - m] % mod;
        if (n <= m) res = 1;
        printf("%d\n", res);
    }
    return 0;
}
```

类似题目：

[HDU 2048 神、上帝以及老天爷](https://acm.hdu.edu.cn/showproblem.php?pid=2048)：计算错位排列的概率，即错位排序除所有组合数。

[HDU 2049 考新郎](http://acm.hdu.edu.cn/showproblem.php?pid=2049)：和本题类似。

