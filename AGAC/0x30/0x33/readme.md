# 0x33 同余

## 基本概念

### 定义

若整数 a 和 b 除以正整数 m 的余数相等，则称 a 和 b 模 m 同余，记作 $a \equiv b \pmod m$。

[同余类和剩余系](https://oi-wiki.org/math/number-theory/basic/#%E5%90%8C%E4%BD%99%E7%B1%BB%E4%B8%8E%E5%89%A9%E4%BD%99%E7%B3%BB)

[欧拉定理及证明](https://zhuanlan.zhihu.com/p/452185813)

欧拉定理的作用：求逆元、降幂（若 a 和 n 互质，则有 $a^b\equiv a^{b \bmod \phi(n)} \pmod n$ ）。

### acwing 202 最幸运的数字

题意：给定整数 L，求至少多少个 8 连起来组成的正整数是 L 的倍数。L 小于 2e9。

根据题意，需要求一个最小的 $x$ 满足 $L \mid 8(10^x-1) / 9$ 。对该式进行变形：

$$
L \mid \frac{8(10^x-1)}{9} \Leftrightarrow 9L \mid 8(10^x-1) \xLeftrightarrow{d = \mathrm{gcd}(L, 8)} \frac{9L}{d} \mid \frac{8(10^x-1)}{d} \\ \Leftrightarrow \frac{9L}{d} \mid (10^x-1) \Leftrightarrow 10^x \equiv 1 \pmod {\frac{9L}{d}}
$$

在欧拉公式中，要求底数和模数互质。下面证明**当底数和模数不互质时无解**。

若底数和模数不互质，则 $\mathrm{gcd}(10,\frac{9L}{d}) = k \neq 1$，则可分为两种情况：$k=2$ 或 $k=5$。令 $p=\frac{9L}{d}$。

若 $k=2$ 则 $p$ 是偶数，则有 $10^x\equiv{1}\pmod{p} \Leftrightarrow 10^x=tp+1 \Leftrightarrow 10^x - 1=tp$ 左边是奇数，右边由于 $p$ 是偶数所以是偶数，显然不成立；

若 $k=5$ 则有 $10^x\equiv{1}\pmod{p} \Leftrightarrow 10^x - 1=tp$。而 $5 \mid p \Leftrightarrow 5 \mid tp$，但 $10^x - 1$ 不能被 5 整除，所以也不成立。

综上所述，$10$ 和 $p$ 一定互质。由欧拉公式可知 $\phi(p)$ 是一个满足等式的解，但不一定是最小的。下面通过反证法证明最小的解一定是 $\phi(p)$ 的约数。

若该最小正整数 $x_0$ 不是 $\phi(p)$ 的约数，则可设 $\phi(p) = qx_0+r$，$0<r<x_0$。因为 $a^{x_0}\equiv 1\pmod p$ 所以 $a^{qx_0}\equiv 1\pmod p$。由欧拉定理有 $a^{\phi(p)}\equiv 1 \pmod p$ ，所以 $a^r \equiv 1 \pmod p$，与最小正整数是 $x_0$ 矛盾。

所以枚举 $\phi(p)$ 的因子并用快速幂 + [龟速乘](https://blog.csdn.net/Cyan_rose/article/details/83065026)验证即可。

```c++

//欧几里得算法
int gcd(LL a, int b) {return b ? gcd(b, a % b) : a;}

//试除法求欧拉函数
LL get_euler(LL c) {
    LL res = c;
    for (int i = 2; i <= c / i; ++ i) {
        if (c % i == 0) {
            int s = 0;
            while (c % i == 0) ++ s, c /= i;
            res = res / i * (i - 1);
        }
    }
    if (c > 1) res = res / c * (c - 1);
    return res;
}

//龟速乘
LL qmul(LL a, LL b, LL c) {
    LL res = 0;
    while (b) {
        if (b & 1) res = (res + a) % c;
        a = (a + a) % c;
        b >>= 1;
    }
    return res;
}

//快速幂
LL qmi(LL a, LL b, LL c) {
    LL res = 1;
    while (b) {
        if (b & 1) res = qmul(res, a, c);
        a = qmul(a, a, c);
        b >>= 1;
    }
    return res;
}

int main() {
    int T = 1; LL L;
    while (cin >> L, L) {
        int d = gcd(L, 8);
        LL c = 9 * L / d;
        LL phi = get_euler(c);
        LL res = 1e18;
        if (c % 2 == 0 || c % 5 == 0) res = 0; //判断c和10是否互质(10必须模c余1)
        else 
            for (LL i = 1; i <= phi / i; ++ i) {
                if (phi % i == 0) {
                    if (qmi(10, i, c) == 1) res = min(res, i);
                    if (qmi(10, phi / i, c) == 1) res = min(res, phi / i);
                }
            }
        printf("Case %d: %lld\n", T ++ , res);
    }
    return 0;
}
```

## 扩展欧几里得算法

[扩展欧几里得算法](https://oi-wiki.org/math/number-theory/gcd/#%E6%89%A9%E5%B1%95%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E7%AE%97%E6%B3%95)

```c++
// 扩展欧几里得算法
int exgcd(int a, int b, int &x, int &y) {
    if (b == 0) { x = 1, y = 0; return a; }
    int d = exgcd(b, a%b, x, y);
    int z = x; x = y; y = z - y * (a / b);
    return d;
}
```

[乘法逆元](https://oi-wiki.org/math/number-theory/inverse/)

### acwing 97 约数之和

题意：假设现在有两个自然数 A 和 B，S 是 $A^B$ 的所有约数之和，求 `S mod 9901` 的值。A 和 B 小于 5e7。

[@random_srand](https://www.acwing.com/solution/content/30343/)

将 A 分解质因数，表示为 $p_1^{c_1}*p_2^{c_2}*\cdots *p_n^{c_n}$。所以 $A^B$ 的约数之和为

$$
(1+p_1+p_1^2+\cdots+p_1^{B*c_1})*(1+p_2+p_2^2+\cdots+p_2^{B*c_2})*\cdots*(1+p_n+p_n^2+\cdots+p_n^{B*c_n})
$$

上式的每一项都是一个等比数列，有两种方法可以进行求解。

#### 思路一：分治

实现一个 `sum(p, k)` 函数，表示 $p^0 + p^1 + \cdots + p ^ {k-1}$。当 k 为偶数时，`sum(p, k)` 可以拆成

$$
\begin{aligned}
\mathrm{sum(p, k)} &= p^0 + p^1 + \cdots + p ^ {k/2-1} + p^{k/2} + p^{k/2+1} + \cdots + p^{k-1} \\
&= p^0 + p^1 + \cdots + p ^ {k/2-1} + p^{k/2} * (p^0 + p^1 + \cdots + p ^ {k/2-1}) \\
&= \mathrm{sum(p, k/2)} + p^{k/2} * \mathrm{sum(p, k/2)} = (p^{k/2} + 1) * \mathrm{sum(p, k/2)}
\end{aligned}
$$

当 k 为奇数时可以单独拿出最后一项，把前面的转化为偶数项，即 `sum(p, k) = sum(p, k-1) + p^{k-1}` 。

```c++
#include<iostream>
#include<unordered_map>
using namespace std;
typedef long long LL;

const int mod = 9901; int A, B;

//保存质因子以及出现的次数
unordered_map<int, int> primes;

//试除法质因子分解
void divide(int n) {
    for(int i = 2; i <= n / i; i++) 
        if(n % i == 0) 
            while(n % i == 0) { primes[i]++; n /= i; }
    if(n > 1) primes[n]++;
}

//快速幂
int qmid(int a, int b) {
    int res = 1;
    while(b) {
        if(b & 1) res = (LL)res * a % mod;
        a = (LL)a * a % mod; b >>= 1;
    }
    return res;
}

//p0 + .. + pk-1
int sum(int p, int k) {
    if(k == 1) return 1;  //边界
    if(k % 2 == 0) 
        return (LL)(qmid(p, k / 2) + 1) * sum(p, k / 2) % mod;
    return (qmid(p, k - 1) + sum(p, k - 1)) % mod;
}

int main(){
    cin >> A >> B; divide(A); //对A分解质因子

    int res = 1;
    for(auto it : primes) {
        //p是质因子，k是质因子的次数
        int p = it.first, k = it.second * B;
        // res要乘上每一项, 注意这里是k + 1
        res = (LL)res * sum(p, k + 1) % mod;
    }

    cout << res << endl;

    return 0;
}
```

### 思路二：等比数列求和公式 + 求逆元

以上式的第一项为例

$$
1+p_1+p_1^2+\cdots+p_1^{B*c_1} = \frac{p_1^{B*c_1+1}-1}{p_1-1}
$$