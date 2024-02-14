# 1-3 暴力枚举总结

## P2241	统计方形（数据加强版）

题目：有一个 n×m 方格的棋盘，求其方格包含多少正方形、长方形（不包含正方形）。

思路：

1. 两层循环左上角坐标，两层循环右下角坐标：
```python
for x in range(N):
    for y in range(M):
        for i in range(x + 1, N + 1):
            for j in range(y + 1, M + 1):
                if i - x == j - y:
                    ansSquare += 1
                else:
                    ansRectangle += 1
```

2. 直接计算大小为 (n, m) 的矩形有多少个长方形和正方形

对于一个 (n, m) 的矩形，它的正方形和长方形个数为

$$
(1+2+...+n)\times(1+2+...+m)=nm(n+1)(m+1)/4
$$

也可以用排列组合的思想

$$
C^2_{N+1}C^2_{M+1}
$$

然后单独考虑正方形。边长为 1 有 $nm$ 个，边长为 2 有 $(n-1)(m-1)$ 个，边长为 3 有 $(n-2)(m-2)$ 个，一直到边长为 $min(n,m)$ 时有 $(m-min(n,m)+1)*(n-min(n,m)+1)$ 个，两式相减即可

## P2089	烤鸡

题目：给定一个正整数 n，要求 $a_1 + ... + a_{10} = n$，其中 $a_i \in  \lbrace a,b,c \rbrace$，求不同的方案数。

思路：深度优先搜索 `def search(k, w, total)` 维护层数、当前选择重量和总重量。

在保存方案的时候进行浅拷贝 `ansSolution.append(solution.copy())`

## P1618	三连击（升级版）

题目：将 1,2,…,9 共 9 个数分成三组，分别组成三个三位数，且使这三个三位数的比例是 A:B:C。求出所有满足条件的三个三位数。

思路：首先把 A B C 除以它们的最大公约数。然后把第一个三位数从 123 枚举到 987，判断能否被 A 整除。最后直接生成第二个和第三个数并判断各数位是否重复。

找最大公约数的方法 `math.gcd(A, B)` 如果需要最小公倍数，则记住：$gcd(x,y)\times lcm(x,y) = xy$

也可以使用 Dfs 搜索全排列

## P1036	\[NOIP2002 普及组\] 选数

题目：从 n 个给定的整数中任选 k 个，计数这 k 个数的和为素数的情况。

思路：深度优先搜索 `dfs(depth, choose, curSum):` 维护深度、总选择个数及数字之和

判断素数的方法

```python
def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, 1 + int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True
```

## P1157	组合的输出

题目：输出组合 $C_n^r$ 的方案，比如 $n=5$ $r=3$ 时为 123, 124, 125, 134, 135, 145, 234, 235, 245, 345，每个元素占三个字符的位置。

思路：Python `itertools` 库中自带排列组合迭代器：

- `product('ABCD', repeat=2)`：笛卡尔积

AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

- `permutations('ABCD', 2)`：长度 2 元组所有可能的排列，无重复元素

AB AC AD BA BC BD CA CB CD DA DB DC

- `combinations('ABCD', 2)`：长度 2 元组，有序，无重复元素

AB AC AD BC BD CD

- `combinations_with_replacement('ABCD', 2)`：长度 2 元组，有序，元素可重复

AA AB AC AD BB BC BD CC CD DD

题目要求[格式化字符串](https://docs.python.org/zh-cn/3/library/string.html#formatstrings)，可以使用 `str.format()` 方法

```python
import itertools
N, R = map(int, input().split())
iter = itertools.combinations(range(N), R)
for it in iter:
    for j in range(R):
        print("{:3d}".format(int(it[j]) + 1), end="")
    print()
```

## P1706	全排列问题

题目：输出排列 $A_n^n$ 的方案

思路：同上题

## P1088	\[NOIP2004 普及组\] 火星人

题目：给定 1 到 N 的其中一个排列，要求求出接下来第 M 个排列

思路：Python 中没有 `next_permulation` 方法，所以需要自行实现。对于一个给定的排列 S，可以通过以下四步生成它的下一个字典序排列

1. 找最靠后的升序使得 $a[j] < a[j+1]$
2. 从第 j+1 个数往后中找比它大的最小数 $a[k]$
3. 交换 $a[j]$ 和 $a[k]$ 此时实际上 $a[j+1]...a[N-1]$ 是降序的。
4. 从第 j+1 个数往后升序排序。

## P3392	涂国旗

题目：输入一个 $N\times M (N,M\leq 50)$ 的矩阵，矩阵中只有三种元素 W B R，分别代表三种颜色。要求把这个矩阵变成若干行 W 接若干行 B 接若干行 R，求最小染色步骤。

思路：本体数据范围小，直接记录每行颜色个数，然后枚举 W 的行数 和 B 的行数，依次计算需要的染色步骤即可。也可以使用 DP 求解。

## P3654	First Step

题目：输入一个 $R\times C$ 的矩阵，矩阵元素为 空地 . 和 障碍 #，求横或竖连续 K 空地的方案个数。

思路：很容易可以想到 $O(R\times C\times K)$ 对每个点搜索一次是否符合，还可以 $O(R\times C)$ 分别对行和列搜索连续个数。若扫描有 t 个空地，且 t 大于 k，则方案数为 $t - k + 1$。

## P1217	\[USACO1.5\] 回文质数 Prime Palindromes

题目：找出 $[a,b], 5\leq a\leq b\leq 100,000,000$ 间的所有回文质数

思路：本题可以有两种处理方法。

### 方法 1 先枚举回文，再判断素数

题目最大的回文数是 1e8，所以枚举到 1e4 然后翻转处理即可

```python
l = []

# 输入 x 生成一个或多个回文数
def generator(x):
    # 例如 x = 123
    num, tmp, mul = 0, x, 1
    while tmp > 0:
        num = num * 10 + tmp % 10
        tmp //= 10
        mul *= 10

    # 此时 num = 321 tmp = 0 mul = 1000
    # 接下来处理 32123 的情况
    global l
    tmp = (num // 10) * mul + x
    if tmp <= b:
        l.append(tmp)

    # 接下来处理 321123 3210123 ...
    tmp = num * mul + x
    while tmp <= b:
        l.append(tmp)
        mul *= 10
        tmp = num * mul + x
```
然后对每个生成的回文数判断素数即可，总共生成的回文数数量在 1e4 左右

### 方法 2 先筛素数，然后判断回文

由于最大数到 1e8 ，直接筛素数会 TLE，但是有两个加速的方法。首先，素数只为偶数。其次，打表可发现偶数位的回文数不可能是质数。这样数量级就到了 1e7，可以通过。

## P1149	\[NOIP2008 提高组\] 火柴棒等式

题目：给 n 根火柴棍，求恰好拼出 A + B = C 的方案数

思路：分析可知，加数最多 3 位数。所以枚举 0 到 2000 所需要用的火柴，然后枚举 A 和 B 即可。

## P3799	妖梦拼木棒

题目：有 n 根木棒，从中选 4 根组成一个正三角形，求方案数。

思路：方案形如 x y z z，其中 x 小于等于 y 且 y 小于 z。所以将木棒用桶排维护，然后先枚举 z 再枚举 x，y 等于 z-x，检查对应的桶的木棒数量，然后维护方案数即可。

由于输入是一行一个数字，Python 使用 `input()` 读入会超时，卡常可以过。

## P2392	kkksc03考前临时抱佛脚

题目：有若干题目，每道题目需要消耗一定时间，可以同时处理两道题目，求处理完成最短时间

思路：本题可以用 枚举子集 或 01 背包 (时间是体积和价值，n 个题目就是 n 个物品，总体积为 m/2) 完成。

```python
for i in range(n):
    for j in(m//2, a[i] - 1, -1):
        f[j] = max(f[j], f[j-a[i]]+a[i])
return max(f[m//2], m-f[m//2])
```

## P2036	\[COCI2008-2009 #2\] PERKET

题目：一共有 n 种调料，每种调料有酸度和苦度，至少添加一种调料，使得总酸度 (酸度相乘) 和总苦度 (苦度相加) 的绝对差最小，并求绝对差的值。

思路：枚举子集