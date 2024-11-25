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

所以枚举 $\phi(p)$ 的因子并用快速幂 + 龟速乘验证即可。