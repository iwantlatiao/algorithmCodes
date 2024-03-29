# 1-7 搜索总结

## P1219	\[USACO1.5\] 八皇后 Checker Challenge

八皇后问题, 输入棋盘大小, 输出解的个数

### 思路

dfs 维护四个数组.
- 每行的棋子放在第几列 $row$
- 每列的棋子放在第几行 $col$
- 两个对角线, 对角线可以用 $x+y=a$ 和 $x-y=a$ 表示

由于 python 运行速度慢, 大数据点可以通过**打表**过.

## P2392	kkksc03考前临时抱佛脚

参考 [暴力枚举总结](../1-3_bruteforce/readme.md#p2392-kkksc03考前临时抱佛脚)

## P1443	马的遍历

有一个 $n \times m$ 的棋盘，在某个点 $(x, y)$ 上有一个马，要求你计算出马到达棋盘上任意一个点最少要走几步。

### 思路

bfs 模板题, python 可以使用 `queue.Queue()` 预置的队列.

输出格式左对齐五格 `"{:<5}".format(dis[i][j])`

更多输出格式[查询](https://docs.python.org/3/library/string.html)

## P1135	奇怪的电梯

大楼的每一层楼都可以停电梯，而且第 $i$ 层楼（$1 \le i \le N$）上有一个数字 $K_i$（$0 \le K_i \le N$）。电梯只有四个按钮：开，关，上，下。上下的层数等于当前楼层上的那个数字。当然，如果不能满足要求，相应的按钮就会失灵。例如： $3, 3, 1, 2, 5$ 代表了 $K_i$（$K_1=3$，$K_2=3$，……），从 $1$ 楼开始。在 $1$ 楼，按“上”可以到 $4$ 楼，按“下”是不起作用的，因为没有 $-2$ 楼。那么，从 $A$ 楼到 $B$ 楼至少要按几次按钮呢？

### 思路

BFS 模板题

## P2895	\[USACO08FEB\] Meteor Shower S

一共有 $M$ 颗流星 $(1\leq M\leq 50,000)$ 会坠落在农场上，其中第 $i$ 颗流星会在时刻 $T_i$（$0 \leq T _ i \leq 1000$）砸在坐标为 $(X_i,Y_i)(0\leq X_i\leq 300$，$0\leq Y_i\leq 300)$ 的格子里。流星的力量会将它所在的格子，以及周围 $4$ 个相邻的格子都化为焦土，当然贝茜也无法再在这些格子上行走。

贝茜在时刻 $0$ 开始行动，她只能在第一象限中，平行于坐标轴行动，每 $1$ 个时刻中，她能移动到相邻的（一般是 $4$ 个）格子中的任意一个，当然目标格子要没有被烧焦才行。如果一个格子在时刻 $t$ 被流星撞击或烧焦，那么贝茜只能在 $t$ 之前的时刻在这个格子里出现。 贝茜一开始在 $(0,0)$。

请你计算一下，贝茜最少需要多少时间才能到达一个安全的格子。如果不可能到达输出 $−1$。

### 思路

BFS 模板题，需要注意两个细节

1. 流星只砸在 $(300,300)$ 内，但人可以走到这个坐标外，就安全了
2. 流星输入的顺序和时间没有关系


## P1036	\[NOIP2002 普及组\] 选数

参考 [暴力枚举总结](../1-3_bruteforce/readme.md#p1036-noip2002-普及组-选数)

## P2036	\[COCI2008-2009 #2\] PERKET

参考 [暴力枚举总结](../1-3_bruteforce/readme.md#p2036-coci2008-2009-2-perket)

## P1433	吃奶酪

房间里放着 $n$ 块奶酪。一只小老鼠要把它们都吃掉，问至少要跑多少距离？距离计算为 $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$ ，老鼠一开始在 $(0,0)$ 点处。

对于全部的测试点，保证 $1\leq n\leq 15$，$|x_i|, |y_i| \leq 200$，小数点后最多有 $3$ 位数字。

### 思路



#### 方法 1 搜索

先求两两奶酪之间的距离，然后生成排列求总距离，时间复杂度 $O(n!)$

```c++
double dist[20][20],mind=0xffffff,dqd;int n,use[20];

// ... 

void dfs(int f,int x){
	if(f==n)
		mind=dqd;
	else
		for(int i=1;i<=n;i++)
			if(use[i]==0&&dqd+dist[x][i]<mind){
				use[i]=1;
				dqd+=dist[x][i];
				dfs(f+1,i);
				use[i]=0;
				dqd-=dist[x][i];
			}
}
```
#### 方法 2 状压DP

三层循环, 最外层遍历当前状态, 第二层遍历当前位置, 第三层遍历前一个位置. 时间复杂度 $O(n^2 2^n)$

```python
def DP():
    for i in range(1, 1 << n):
        for j in range(n):
            # 该状态没走过当前位置就跳过
            if i & (1 << j) == 0:
                continue
            for k in range(n):
                # 该状态没走过前一个位置 或 前一个位置和当前位置相同 就跳过
                if i & (1 << k) == 0 or j == k:
                    continue
                f[j][i] = min(f[j][i], f[k][i - (1 << j)] + dis[k][j])
```

## P1605	迷宫

给定一个 $N \times M$ 方格的迷宫，迷宫里有 $T$ 处障碍，障碍处不可通过。

在迷宫中移动有上下左右四种方式，每次只能移动一个方格。数据保证起点上没有障碍。

给定起点坐标和终点坐标，每个方格最多经过一次，问有多少种从起点坐标到终点坐标的方案。

### 思路

DFS 搜到终点就答案 + 1

## P1019	\[NOIP2000 提高组\] 单词接龙

题目要求做单词接龙，每个单词最多用两次

### 思路

首先预处理每个单词接龙能增加的长度，然后使用 DFS 即可，需要注意每个单词可以用两次。

## P1101	单词方阵

有一个 $n\times n$ 的字母方阵，要求打印特定单词的位置，这个特定单词可能沿着 8 个方向摆。

### 思路

DFS 模拟染色

## P2404	自然数的拆分问题

给定一个自然数，要求拆分成一些数字的和，打印方案

### 思路

DFS 模拟保存方案

## P1596	\[USACO10OCT\] Lake Counting S

网格地图，判断连通块的数量

### 思路

BFS DFS 模板

## P1162	填涂颜色

由数字 $0$ 组成的方阵中，有一任意形状的由数字 $1$ 构成的闭合圈。现要求把闭合圈内的所有空间都填写成 $2$。

### 思路

搜闭合圈不方便，可以从边界开始搜，搜出来的都不是闭合圈，反向染色即可。

## P1032	\[NOIP2002 提高组\] 字串变换

已知有两个字串 $A,B$ 及一组字串变换的规则（至多 $6$ 个规则），形如：

- $A_1\to B_1$。
- $A_2\to B_2$。

规则的含义为：在 $A$ 中的子串 $A_1$ 可以变换为 $ B_1$，$A_2$ 可以变换为 $B_2\cdots$。

若在 $10$ 步（包含 $10$ 步）以内能将 $A$ 变换为 $B$，则输出最少的变换步数；否则输出 `NO ANSWER!`。

### 思路

[Python 字符串匹配常用api](https://blog.csdn.net/weixin_45642918/article/details/103784164)

一些字符串的常见操作：

- 字符串查找子串 `str.find(substr, start_pos)`
- 字符串替换 `str.replace(old, new, count)`

因为已知起点和终点，所以可以使用双向 bfs 进行搜索，然后使用 `dict` 记录已经出现过的字符串。由于 bfs 可以保证队列前端最优，所以对于每个方向都维护一个 `dict`，如果该方向的 `dict` 已经有当前搜索的字符串就跳过，如果对面方向的 `dict` 已经有当前搜索的字符串就说明找到方案。由于步数在 $10$ 以内，所以两边搜索深度在 $5$ 以内即可。

```python
def bfs():
    # (str, num_of_transformation)
    qA, qB = Queue(), Queue()
    qA.put((A, 0)), qB.put((B, 0))
    # 双向 bfs, 当规则有匹配字符串 且 深度 <= 5 才继续搜索
    while qA.empty() == False or qB.empty() == False:
        if qA.empty() == False:
            strA, numA = qA.get()
            for i in range(len(rules)):
                posA = strA.find(rules[i][0])
                while posA != -1:
                    newstrA = strA[:posA] + strA[posA:].replace(rules[i][0], rules[i][1], 1)
                    if mapA.get(newstrA) == None and numA + 1 <= 5:
                        newnumA = numA + 1
                        if mapB.get(newstrA) != None:
                            return newnumA + mapB.get(newstrA)
                        mapA[newstrA] = newnumA
                        qA.put((newstrA, newnumA))
                    posA = strA.find(rules[i][0], posA + 1)

        if qB.empty() == False:
            strB, numB = qB.get()
            for i in range(len(rules)):
                posB = strB.find(rules[i][1])
                while posB != -1:
                    newstrB = strB[:posB] + strB[posB:].replace(rules[i][1], rules[i][0], 1)
                    if mapB.get(newstrB) == None and numB + 1 <= 5:
                        newnumB = numB + 1
                        if mapA.get(newstrB) != None:
                            return newnumB + mapA.get(newstrB)
                        mapB[newstrB] = newnumB
                        qB.put((newstrB, newnumB))
                    posB = strB.find(rules[i][1], posB + 1)

    return -1
```

## P1825	\[USACO11OPEN\] Corn Maze S

有一个网格地图，存在多个双向传送装置，要求从起点到终点的最短距离。

### 思路

加一个对传送门的判断即可，是传送门就瞬移坐标判断，其他与常规搜索相同。