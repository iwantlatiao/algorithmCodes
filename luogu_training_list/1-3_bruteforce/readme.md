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

题目要求格式化字符串，可以使用 `str.format()` 方法

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

## P1088	\[NOIP2004 普及组\] 火星人

## P3392	涂国旗

## P3654	First Step

## P1217	\[USACO1.5\] 回文质数 Prime Palindromes

## P1149	\[NOIP2008 提高组\] 火柴棒等式

## P3799	妖梦拼木棒

## P2392	kkksc03考前临时抱佛脚

## P2036	\[COCI2008-2009 #2\] PERKET