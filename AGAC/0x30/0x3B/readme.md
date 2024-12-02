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
int main() {}
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