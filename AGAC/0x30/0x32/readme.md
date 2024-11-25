# 0x32 约数

## 基本概念

若整数 d 能整除整数 n，则称 d 是 n 的约数，n 是 d 的倍数，记作 $d|n$。

### 算数基本定理的推论

若正整数 N 被唯一分解为 $N=p_1^{c_1}...p_m^{c_m}$，其中 c 都是正整数，p 都是指数，满足 $p_1 < p_2 < ... < p_m$，则 N 的正约数集合可以写作

$$
\{p_{1}^{b_{1}}p_{2}^{b_{2}}\cdots p_{m}^{b_{m}}\}, 0\leq b_{i}\leq c_{i}
$$

N 的正约数个数为

$$
(c_{1}+1)*(c_{2}+1)*\cdots*(c_{m}+1)=\prod_{i=1}^{m}(c_{i}+1)
$$

N 的所有正约数的和为

$$
(1+p_{1}+p_{1}^{2}+\cdots+p_{1}^{c_{1}})*\cdots*(1+p_{m}+p_{m}^{2}+\cdots+p_{m}^{c_{m}})=\prod_{i=1}^{m}\left(\sum_{j=0}^{c_{i}}(p_{i})^{j}\right)
$$

### 求 N 的正约数集合：试除法

由于约数总是成对出现（除了完全平方数），所以只需要扫描 `d=1~sqrt(N)` 尝试 d 能否整除 N，即可找出所有因数。一整数 N 的约数个数上限为 `2 * sqrt(N)`

```c++
// 试除法求N的约数集合
int factor[1600], m = 0;
for (int i = 1; i*i <= n; i++) {
    if (n % i == 0) {
        factor[++m] = i;
        if (i != n/i) factor[++m] = n/i;
    }
}
for (int i = 1; i <= m; i++)
    cout << factor[i] <<endl;
```

### 求 1~N 每个数的正约数集合：倍数法

试除法的时间复杂度为 $O(N\sqrt N)$。可以反过来考虑，对于每个数 d ，`1~N` 中以 d 为约数的数就是 d 的倍数 `d, 2*d, ..., floor(N/d)*d`。时间复杂度为 $O(N + N/2 + N/3 + ... + 1) = O(N\log N)$。`1~N` 每个数的约数个数的总和大约为 `nlogn`。

```c++
// 倍数法求1~N每个数的约数集合
vector<int> factor[500010];
for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n/i; j++)
        factor[i*j].push_back(i);
for (int i = 1; i <= n; i++) {
    for (int j = 0; j < factor[i].size(); j++)
        printf("%d ", factor[i][j]);
    puts("");
}
```

### acwing 198 反质数

题目：

对于任何正整数 x，其约数的个数记作 `g(x)`，例如 `g(1)=1`、`g(6)=4`。如果某个正整数 x 满足：对于任意的小于 x 的正整数 i，都有 `g(x)>g(i)`，则称 x 为反素数。例如，整数 1，2，4，6 等都是反素数。

现在给定一个数 N，请求出不超过 N 的最大的反素数。`N < 2e9`。

思路：通过三个引理来得出做法

1. 不超过 N 的最大反素数就是约数个数最多的数中最小的一个。（由定义可知）
2. 不超过 N 的数中，不同质因子不超过 10 个。且所有质因子的指数之和不超过 30。（最小的 10 个质数 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 乘积已经大于 2e9，最小的质数 2 的 31 次方已经大于 2e9）
3. x 为反素数的必要条件是，x 可写作 $2^{c_1} * 3^{c_2} * 5^{c_3} * ... * 23^{c_{9}}$ 且 $c_1 \geq c_2 \geq \cdots \geq c_{9} \geq 0$

引理 3 可以通过反证法证明：如果 x 有一个大于 23 的质因子 `p`，由引理 2 肯定存在一个不大于 23 的质因子 `p'` 无法整除 N。令 `N' = N / (p^k) * (p'^k) < N` 可知 `N'` 的约数个数等于 N 且更小，不符合题意。同理，如果质因子不是连续若干个最小的，或者指数不单调递减，也可以通过替换的方式得到一个更小的数。所以引理 3 得证。

综上，可以用 DFS 尝试依次确定前 10 个质数的指数，满足指数单调递减、总乘积不超过 N，同时记录约数个数。

[@一只野生彩色铅笔](https://www.acwing.com/solution/content/47849/)

```c++
int n, s; //s记录当前最大约数个数的数
int maxd; //maxd记录当前最大约数个数的数的约数个数
int primes[9] = {2, 3, 5, 7, 11, 13, 17, 19, 23};

//u是当前枚举到第u个素数, last是前一个素数所枚举的次数
//p就是当前的数, sum是当前数的所有约数个数之和
void dfs(int u, int last, int p, int sum) {
    if (sum > maxd || sum == maxd && p < s) 
        maxd = sum, s = p;
    if (u == 9) return;
    for (int i = 1; i <= last; ++ i) {
        if ((LL)p * primes[u] > n) return;
        p *= primes[u];
        dfs(u + 1, i, p, sum * (i + 1));
    }
}

int main() {
    cin >> n; dfs(0, 30, 1, 1); cout << s << endl; return 0;
}
```

### acwing 199 余数之和

题意：给出正整数 n 和 k，计算 `j(n,k) = k % 1 + k % 2 + ... + k % n` 的值。n 和 k 小于 1e9。

[@cnnf](https://www.acwing.com/solution/content/1333/)：首先取余计算可以转化 $k \bmod i = k - \lfloor k/i \rfloor * i$，所以

$$
j(n, k) = n * k - \sum_{i=1}^n \lfloor k/i \rfloor * i
$$

所以需要快速地求出后面和式。经过观察可知 $\lfloor k/i \rfloor$ 是一个分段函数，且最多有 $2\sqrt n$ 段（将 $i$ 对 $\sqrt n$ 讨论可得）。这样就可以用多个等差数列求和的方法得到后面和式的值。

我们还需要知道每个等差数列中 $i$ 的起点和终点。也就是说对于每个 $i$ 找到最大的 $g(i)$ 使得 $\lfloor k/i \rfloor = \lfloor k/g(i) \rfloor$。因此 $g(i) = \frac{k}{\lfloor k/i \rfloor}$，同时也要让 $g(i) \leq n$。这样就找到了每个等差数列的起点和终点，并且下一个等差数列的起点是 $g(i) + 1$。

```c++
int main() {
    scanf("%d%d", &n, &k);
    ans = (LL)n * k;
    for (l = 1; l <= n; l = r + 1) {
        if(k / l == 0) break;
        r = min(k / (k / l), n);
        ans -= (LL)(k / l) * (l + r) * (r - l + 1) / 2;
    }
    printf("%lld\n", ans);
    return 0;
}
```

拓展：[数论分块的性质](https://oi-wiki.org/math/number-theory/sqrt-decomposition/)

## 最大公约数

两个非负整数的最大公约数和最小公倍数的乘积等于两个整数的乘积。

```c++
int a, b >= 0 : gcd(a, b) * lcm(a, b) = a * b
```

更相减损术（常用于高精度）

```c++
int a > int b : gcd(a, b) = gcd(b, a - b) = gcd(a, a - b)
int a, b >= 0 : gcd(2 * a, 2 * b) = 2 * gcd(a, b)
```

欧几里得算法

```c++
// int a, b; b != 0 : gcd(a, b) = gcd(b, a % b)
int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}
```

### acwing 200 Hankson的趣味题

题意：有 n 个询问，每个询问给出 a、b、c、d 四个自然数，求有多少个 x 满足 `gcd(a,x) = c` 且 `lcm(b,x) = d`。其中 `n < 2000, a,b,c,d < 2e9`。

朴素做法：从 `lcm(b,x) = d` 可知 `d % x == 0`。于是可以先用试除法求出 d 的所有约数，然后检查是否满足题目等式。时间复杂度为 $n\sqrt{d} \log{d}$。

[@小小_88](https://www.acwing.com/solution/content/141953/)：在朴素做法中，主要的时间消耗在试除法中，因为大部分数的约数并不多。试除法中大部分的数都是无法整除 d 的。

为了避免试除法消耗过多时间，可以通过预处理质数 + 搜索的方法得到 d 的所有约数，再判断是否满足题目等式。

```c++
void dfs(int u, int p) //dfs 用质因子拼凑所有约数
{
    if(u == cntf) { divider[cntd++] = p; return; }

    for(int i = 0; i <= factor[u].second; i++)
    {
        dfs(u + 1, p);
        p *= factor[u].first;
    }
}

int main()
{
    get_primes(50000); //预处理出 1 ~ sqrt(2 * 1e9) 之间的所有质数

    scanf("%d", &n);
    while(n--)
    {
        int a0, a1, b0, b1;
        scanf("%d%d%d%d", &a0, &a1, &b0, &b1);

        //将 b1 分解质因子并存入 factor
        int d = b1; cntf = 0;
        for(int i = 0; primes[i] <= d / primes[i]; i++)
        {
            int p = primes[i];
            if(d % p == 0)
            {
                int s = 0;
                while(d % p == 0) s++, d /= p;
                factor[cntf++] = {p, s};
            }
        }
        if(d > 1) factor[cntf++] = {d, 1};

        //用 d1 的所有质因子拼凑出 d1 的所有约数
        cntd = 0; dfs(0, 1);

        //枚举所有约数，记录满足条件的数的个数
        int res = 0;
        for(int i = 0; i < cntd; i++)
        {
            int x = divider[i];
            if(gcd(x, a0) == a1 && (LL)x * b0 / gcd(x, b0) == b1) res++;
        }
        printf("%d\n", res);
    }
    return 0;
}
```

## 欧拉函数

互质：如果 $\forall{a, b} \in \mathbb{N}, \mathrm{gcd}(a, b) = 1$ ，则称 a 和 b 互质。对于多个数的情况，则分为互质和两两互质（条件更强）。

[欧拉函数 wiki](https://oi-wiki.org/math/number-theory/euler-totient)

欧拉函数 $\phi(n)$ 表示小于等于 n 的正整数中，与 n 互质的数的个数。若 n 为质数，则 $\phi(n) = n - 1$。

若在算数基本定理中 $N = \prod_{i=1}^m p_1^{c_1}\cdots p_m^{c_m}$，则有欧拉函数计算式如下：

$$
\phi(n) = N * \frac{p_1 - 1}{p_1} * \cdots * \frac{p_m - 1}{p_m} = N * \prod (1 - \frac{1}{p})
$$

上式可以通过容斥原理证明。根据欧拉函数计算式，只需要分解质因数，就可以顺便求出欧拉函数：

```c++
// 计算欧拉函数
int phi(int n) {
    int ans = n;
    for (int i = 2; i*i <= n; i++) {
        if (n % i == 0) { // i是质数
            ans = ans / i * (i-1);
            while (n % i == 0) n /= i;
        }
    }
    if (n > 1) // n是质数
        ans = ans / n * (n-1);
    return ans;
}
```

欧拉函数性质 1：对于大于 1 的自然数 n，1 到 n 中与 n 互质的数的和为 $n * \phi(n) / 2$。

欧拉函数性质 2：若 a 与 b 互质，则 $\phi(ab) = \phi(a)\phi(b)$。将该性质推广到一般函数，可以得到积性函数的概念。

积性函数：若 a 与 b 互质时有 $f(ab) = f(a)f(b)$ 则称 $f$ 为积性函数。

积性函数性质 1：若 $f$ 是积性函数，且在算数基本定理中 $n = \prod_{i=1}^m p_1^{c_1}\cdots p_m^{c_m}$，则 $f(n) = \prod_{i=1}^m f(p_i^{c_i})$

欧拉函数性质 3：若 p 为质数，p 能整除 n 且 p^2 能整除 n，则 $\phi(n) = \phi(n/p) * p$。由该性质可得 $\phi(p^k) = p^k - p^{k-1}$ 。

欧拉函数性质 4：若 p 为质数，p 能整除 n 且 p^2 不能整除 n，则 $\phi(n) = \phi(n/p) * (p - 1)$

欧拉函数性质 5：n 的所有因子的欧拉函数和为 n，即 $\sum_{d|n} \phi(d) = n$。

## acwing 201 可见的点

题意：在一个平面直角坐标系的第一象限内，如果一个点 `(x,y)` 与原点 `(0,0)` 的连线中没有通过其他任何点，则称该点在原点处是可见的。编写一个程序，计算给定整数 N 的情况下，满足 `0 <= x, y <= N` 的可见点 `(x，y)` 的数量（可见点不包括原点）。

![acwing 201](https://cdn.acwing.com/media/article/image/2019/01/18/19_a68c1a281a-3090_1.png)

分析题目可以发现，除了 `(1, 0)`、`(0, 1)`、`(1, 1)` 这三个点以外，其他的点能被看到，当且仅当 `1 <= x <= y` 且 `x != y` 且 `gcd(x, y) = 1`。
且可见点关于直线 `y = x` 对称。所以答案为：

$$ 3 + 2 * \sum_{i=2}^N \phi(i) $$

我们可以用埃氏筛法的思想在 $O(NlogN)$ 的时间内求出 N 以内每个数的欧拉函数。

```c++
void euler(int n) {
	for (int i = 2; i <= n; i++) phi[i] = i;  // 初始化 phi(N) = N
    // 如果 i 是质数，就在 phi(i), phi(2i), ... 中乘一项 (i-1) / i
	for (int i = 2; i <= n; i++)
		if (phi[i] == i) 
			for (int j = i; j <= n; j += i)
				phi[j] = phi[j] / i * (i - 1);
}
```

也可以使用线性筛的思想，利用性质 3（`i%prime[j] = 0` 说明 `i*prime[j]` 与 `i` 有相同质因子）和性质 4（`i%prime[j] > 0` 说明 `i` 与 `prime[j]` 互质）在 $O(N)$ 内求。

```c++
void euler(int n) {
	memset(v, 0, sizeof(v)); // 最小质因子
	m = 0; // 质数数量
	for (int i = 2; i <= n; i++) {
		if (v[i] == 0)  // i是质数
			v[i] = i, prime[++m] = i, phi[i] = i - 1;
		
        // 给当前的数i乘上一个质因子
		for (int j = 1; j <= m; j++) {
			// i有比prime[j]更小的质因子，或者超出n的范围
			if (prime[j] > v[i] || prime[j] > n / i) break;
			// prime[j]是合数i*prime[j]的最小质因子
			v[i*prime[j]] = prime[j];
			phi[i*prime[j]] = phi[i] * (i%prime[j] ? prime[j]-1 : prime[j]);
		}
	}
	for (int i = 2; i <= n; i++)
		cout << i << ' ' << phi[i] << endl;
}
```