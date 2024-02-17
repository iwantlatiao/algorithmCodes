# 1-4 递推和递归总结

## P1255	数楼梯

题目：楼梯有 N 阶，上楼可以一步上一阶，也可以一步上二阶，求不同走法的方案数。

思路： $f[n] = f[n-1] + f[n-2]$

## P1002	\[NOIP2002 普及组\] 过河卒

题目：棋盘上 A 点有一个卒要走到 B 点，只能往下或往右走，有一些点不能走，求可能的方案数。

思路： $f[x, y] = f[x-1][y] + f[x][y-1]$

## P1044	\[NOIP2003 普及组\] 栈

题目：给定 1, 2, ..., n 求经过栈的 push 和 pop 操作后能有多少种输出方案。

思路：这是一道经典题，有多种做法。

### 1. 记忆化搜索

- 设 $f[i,j]$ 表示还有 i 个数没处理、有 j 个数在栈里的方案数，起始状态为 $f[n,0]$。
- 如果数全都进栈了，那只有唯一的方案，所以边界 $f[0,j]=1$
- 对 $f[i,j]$ 有两种情况，栈此时是空的，或栈此时是非空的
  - 若栈此时是空的，则只能入栈 1 个元素，方案数 $f[i,j] = f[i-1, j+1]$
  - 若栈是非空的，则可以出栈 1 个元素，或者入栈 1 个元素，方案数 $f[i,j] = f[i, j-1] + f[i-1, j+1]$

### 2. 动态规划

- 记忆化搜索从 $f[n,0]$ 出发，把大问题划归为小问题。动态规划从 $f[0,0...N]$ 出发，从小问题的解组成大问题的解。
- 转移方程不变

```python
for i in range(1, N + 1):
    f[i][0] = f[i - 1][1]
    for j in range(1, N - i + 1):
        f[i][j] = f[i - 1][j + 1] + f[i][j - 1]
print(f[N][0])
```

### 3 卡特兰数

[Leetcode 对卡特兰数的介绍](https://leetcode.cn/circle/discuss/lWYCzv/)

[math173 对卡特兰数的介绍](http://lanqi.org/skills/10939/)

[wiki 对卡特兰数的介绍](https://en.wikipedia.org/wiki/Catalan_number)

首先，每一种出栈序列都与一一对应进出栈的顺序。不妨用 +1 表示进栈，-1 表示出栈，那么出栈序列 (2, 4, 3, 1) 与进出栈顺序 (+1, +1, -1, +1, +1, -1, -1, -1) 是对应的。

![出栈序列示意图](./image/catalan_stack_seq.png)

那么对 n 个数的序列，总的进出栈顺序是给 2n 个 1 前面挑 n 个添加 $+$ 号，其他的添加 $-$ 号，共 $C^n_{2n}$ 种吗？

答案是否定的，这是因为出栈的前提是有进栈动作，于是要求每个排列中的前若干项和均不为负数，也就是说排列

1, -1, -1, 1, 1, -1, -1, 1

是无效的。那么无效的排列到底有多少呢？设 M 是所有无效的排列构成的集合，直接求 M 的数量不好求。

考虑其中第一次发现排列无效的时候，也就是第一次发现其前若干项和为 -1 的时候，此时我们将包含使得前若干项和为 -1 的这一项开始的之前的所有项全都取相反数，那么就会得到一个新的排列，这个排列包含 n+1 个 +1 以及 n-1 个 -1，设所有这样的排列构成集合 N．

可证明 $M \to N$ 的映射是双射 (N 中的每一个排列从第一项往后累积求和的时候必然会出现和为 +1 的情形，此时将排列中使得和为 +1 的这一项连同之前的所有项全部取相反数，那么就会得到 M 中的一个排列)．

这样，无效的排列可以通过 N 求出，共有 $C_{2n}^{n-1}$ 个，总的出栈序列方案数为 

$$C_{2n}^{n}-C_{2n}^{n-1}=\frac{C_{2n}^{n}}{n+1}$$

进出栈问题还有很多变形，如

1. 匹配的括号序列种数
2. n+1 个叶子节点能够构成多少种形状不同的国际满二叉树
3. 不跨越对角线，只能向右和向下的方格地图移动方案数
4. 电影购票找零方案数
5. 圆内连弦方案数
6. 节点值从 1 到 n 互不相同的二叉搜索树有多少种
7. 使用 n 个矩形拼成 n 阶梯形

详见

[卡特兰数问题集 1](https://zhuanlan.zhihu.com/p/31317307)

[卡特兰数问题集 2](https://zhuanlan.zhihu.com/p/31526354)

[卡特兰数问题集 3](https://zhuanlan.zhihu.com/p/31585260)

卡特兰数问题中都会存在一种匹配关系，如进出栈匹配，括号匹配等，一旦计数问题中存在这种关系，那我们就需要去考虑这是否是卡特兰数问题。此外，我们还可以记住序列前四项：1, 1, 2, 5，这些将有利于我们联想到卡特兰数。

卡特兰数有多种定义方式

- 递归定义
 
$$
\begin{cases}
  C_0 = C_1 =1 \\
  C_n = \sum_{k=0}^{n-1} C_kC_{n-1-k} = C_0C_{n-1}+C_1C_{n-2}+\ldots+C_{n-1}C_0, n\geq 2
\end{cases}
$$

- 递推公式

$$C_n=\frac{4n-2}{n+1}C_{n-1}$$

- 通项公式

$$C_n=\frac{1}{n+1}C_{2n}^n=C_{2n}^n-C_{2n}^{n-1}$$

$$C_n=\frac{1}{n+1}\sum_{i=0}^n\left(C_n^i\right)^2$$

- 增长速度

$$\Delta C_n\sim\frac{4^n}{n^{\frac32}\sqrt{\pi}}$$


## P1028	\[NOIP2001 普及组\] 数的计算

题目：构造数列，求合法数列方案数

思路： $f[num]=f[1\ldots num//2] + 1$

## P1464	Function

题目：给定递归方式，求解答案

思路：记忆化搜索

## P1928	外星密码

要求对字符串解压缩，如 AC[3FUN] 解压为 ACFUNFUNFUN，可能有多重压缩。

思路1. 纯模拟: 

我们需要操作的对象是方括号内的部分, 对于方括号外面的内容不需要进行任何的操作. 因此要找到最内层的括号并进行处理.

怎么找最内层的括号呢? 方法是从字符串末尾开始找第一个左括号, 然后从此往右找第一个右括号. 确定最内层括号后, 使用 `string.replace()` 把字符串进行替换, 这样一直重复直到没有括号为止, 就得到了最终的答案。

```python
def unzip(s):
    s = s.strip("[]")
    digit = 0
    for t in s:
        if "0" <= t and t <= "9":
            digit += 1
        else:
            break
    num = int(s[:digit])
    residualS = s[digit:]
    return residualS * num

str = input()
while True:
    try:
        left = str.rindex("[")
        right = str.index("]", left)
    except:
        break
    zipString = str[left : right + 1]
    str = str.replace(zipString, unzip(zipString))
print(str)
```

思路2. 递归: 

对于 C++ 语言, 递归比较方便, 因为读入数据是按字符读入.

```C++
string read(){
	int n; char c; string s="", s1;
	
  //一直读入字符，直到Ctrl+z
	while (cin>>c){
		if (c=='['){
			cin>>n;//读入D
			s1=read();//读入X
			while (n--) s+=s1;//重复D次X
		}
		else{
			if (c==']') return s;//返回X
		  else s+=c;//如果不是'['和']'，那就是X的一个字符，所以加进X
		}
	}
  return s;
}
int main() {cout<<read(); return 0;}
```

python 由于按行读入, 所以可以先读入整行, 然后把 `cin()` 实现为 `return s[i++]` , 对数字的读入也需要单独处理, 其他思路与 C++ 相同.

```python
str = input()
index, strLen = 0, len(str)

def getInput():
    global index
    if index < strLen:
        t = str[index]
        index += 1
        return t
    else:
        return "-1"

def getNumber():
    global index
    num = 0
    while "0" <= str[index] and str[index] <= "9" and index < strLen:
        num = (num << 3) + (num << 1) + int(str[index])
        index += 1
    return num

def unzip():
    ch = getInput()
    s = ""
    while ch != "-1":
        if ch == "]":
            return s
        elif ch == "[":
            mul = getNumber()
            tmpStr = unzip()
            s += tmpStr * mul
        else:
            s += ch
        ch = getInput()
    return s

print(unzip())
```
经测试两种方法速度差不多

## P2437	蜜蜂路线

![image of P2437](./image/P2437.png)

思路: 数 n-m+1 个楼梯

## P1164	小A点菜

口袋里有 M 元, 有 N 种菜, 每种菜 ai 元, 求刚好花完钱的点菜方法

思路: 01背包. 设 $f[i][j]$ 表示前 i 种菜花了 j 元的点菜方法, 转移方程如下.

$$
f[i][j] = 
\begin{cases}
  f[i-1][j], j < cost[i] \\
  f[i-1][j]+1, j = cost[i] \\
  f[i-1][j]+f[i-1][j-cost[i]], j > cost[i]
\end{cases}
$$

如果边界条件设为 $f[i][0] = 1$, 那么 $j \geq cost[i]$ 可以合并为一种情况.

## P1036	\[NOIP2002 普及组\] 选数

在 1-3 中已经解决

## P1990	覆盖墙壁

## P3612	\[USACO17JAN\] Secret Cow Code S

## P1259	黑白棋子的移动

## P1010	\[NOIP1998 普及组\] 幂次方

## P1228	地毯填补问题

## P1498	南蛮图腾