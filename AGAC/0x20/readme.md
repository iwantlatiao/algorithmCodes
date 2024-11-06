# 递归的形式

## 指数型枚举

从多个整数中选取任意多个，求可能选择方案。等价于每个数可以选或者不选，所以是 $2^n$ 种选择方案。

```c++
vector<int> chosen;  // 被选择的数
void calc(int x) {
    if (x == n + 1) {
        for (int i = 0; i < chosen.size(); i++)
            cout << chosen[i] << " ";
        return;
    }

    calc(x + 1);  // 不选 x

    chosen.push_back(x);
    calc(x + 1);  // 选 x
    chosen.pop_back();
}
```

## 组合型枚举

从多个整数中选取 m 个，求可能选择方案。只需要在开头增加一个返回的情况即可。

```c++
void calc(int x) {
    if (chosen.size() > m || chosen.size() + (n - x + 1) < m) return;
    // ...
}
```

## 排列型枚举

把多个整数排成一行后随机打乱顺序，输出所有可能顺序。等价于全排列问题。在递归中求解的问题为“把指定的 n 个整数按照任意次序排列”。

```c++
int order[N];  // 记录的顺序
bool vis[N];  // 是否已经被选中过了
void calc(int x) {
    if (x == n + 1) {
        for (int i = 0; i < chosen.size(); i++)
            cout << chosen[i] << " ";
        return;
    }

    for (int i = 1; i <= n; i++) {
        if (vis[i]) continue;
        order[x] = i; vis[i] = true;
        calc(x + 1);
        vis[i] = false;
    }
}
```

# 深搜

## acwing 166 数独

数独 是一种传统益智游戏，你需要把一个 9×9 的数独补充完整，使得数独中每行、每列、每个 3×3 的九宫格内数字 1∼9 均恰好出现一次。请编写一个程序填写数独。

### 思路

- 对于每行、每列、每个九宫格分别用一个 9 位二进制数代表哪些数还可以填（二进制的与运算，然后用 lowbit 取能填的数字）
- 填上（删去）某个数后就要对二进制数的某位改成零（一）

## acwing 171 送礼物

一共有 N （$N<46$） 个物品，每个物品重 Gi，最大举起重量 W，求一次性能搬动的最大重量。

### 思路

双向 DFS。第一次 DFS 将前一半的所有重量组合求出，然后排序去重。第二次 DFS 将后一半的所有重量组合求出，然后在前一半的可能重量中二分查找最大的。总时间复杂度为 $O(2^x + 2^{n-x}\log 2^x)$

# 剪枝

## acwing 167 木棒

乔治拿来一组等长的木棒，将它们随机地砍断，使得每一节木棍的长度都不超过 50 个长度单位。然后他又想把这些木棍恢复到为裁截前的状态，但忘记了初始时有多少木棒以及木棒的初始长度。

请你设计一个程序，帮助乔治计算木棒的可能最小长度。每一节木棍的长度都用大于零的整数表示。

### 思路

[@tonngw](https://www.acwing.com/solution/content/121003/)

剪枝策略：

1. sum % length = 0
2. 木棍长度降序排序，以组合方式枚举搜索
3. 如果当前长度木棍没有搜到方案，跳过该长度
4. 如果木棒的第一根木棍就搜索失败，则一定搜不到方案。（交换可证）
5. 如果木棒的最后一根木棍搜索失败，则一定搜不到方案。（贪心可证）

```c++
// 正在拼第 stick 根木棍，该木棍当前长度 cab，从 start 开始枚举木棍序号 
bool dfs(int stick, int cab, int start) {
    if (stick > cnt) return true;  // 全拼好了
    if (cab == nowlen) return dfs(stick + 1, 0, 1);  // 拼下一根

    int fail = 0;  // 上一根失败的长度
    for (int i = start; i <= n; i++) {
        if (!vis[i] && fail != sticks[i] && cab + sticks[i] <= nowlen) {
            vis[i] = true;
            if(dfs(stick, cab + sticks[i], i + 1)) return true;
            vis[i] = false; fail = sticks[i];
            if (cab == 0 || cab + sticks[i] == nowlen) return false;
        }
    }

    return false;
}
```

## acwing 168 生日蛋糕

制作一个体积为 $N\pi$ 的 $M$ 层生日蛋糕，每层都是一个圆柱体。设从下往上数第 $i$ 层蛋糕是半径为 $Ri$，高度为 $Hi$ 的圆柱。当 $i<M$ 时，要求 $Ri>Ri+1$ 且 $Hi>Hi+1$。

我们希望蛋糕外表面（最下一层的下底面除外）的面积 $Q$ 最小。令 $Q=S\pi$ ，请编程对给出的 $N$ 和 $M$，找出蛋糕的制作方案（适当的 $Ri$ 和 $Hi$ 的值），使 $S$ 最小。除 $Q$ 外，以上所有数据皆为正整数。

### 剪枝思路

[@random_srand](https://www.acwing.com/solution/content/31876/)

记最底层为 $m$，则有表面积和体积公式：

$$
S_{total} = \sum_{i=1}^{m}(2\pi R_i H_i) \\
V_{total} = \sum_{i=1}^{m}(\pi R_i^2 H_i)
$$

优化搜索顺序：层间从下到上；层内先枚举半径再枚举高，从大到小

可行性剪枝：记总体积为 $n$，总层数为 $m$，当前层 $u$，第 $u$ 层的体积为 $V_u$，半径 $R_u$，体积 $V_u$，第 $m$ 层到第 $u+1$ 层的体积和为 $V$，面积和为 $S$。

1. 半径限制：最小取值应该是当前层号，最大取值取决于下一层半径减一或当前层体积最大值除高度最小值。

$$u\leq R_u\leq min\{R_{u+1}-1,\sqrt{\frac{n-min\sum_{i=1}^{u-1}V_i-V}u}\}$$

2. 高度限制：最小取值应该是当前层号，最大取值取决于下一层高度减一或当前层体积最大值除底面积最小值。

$$u\leq H_u\leq min\{H_{u+1}-1,\frac{n-min\sum_{i=1}^{u-1}V_i-V}{R_u^2}\}$$

3. 体积剪枝：已搜索体积加剩下的最小体积应该小于等于 $n$

$$V+min\sum_{i=1}^{u-1}V_i\leq n$$

4. 表面积和体积之间的关系

第一层到第 $u$ 层的表面积有（以下均省去 $\pi$）

$$S_{1-u}=2\sum_{i=1}^uR_iH_i=\frac2{R_{u+1}}\sum_{i=1}^uR_{u+1}R_iH_i>\frac2{R_{u+1}}\sum_{i=1}^uR_i^2H_i$$

第一层到第 $u$ 层体积有

$$n-V=\sum_{i=1}^uR_i^2H_i$$

所以有

$$S_{1-u}>\frac{2(n-V)}{R_{u+1}}$$

由于当前答案 $S_{now} = S + S_{1-u}$，已记录最佳答案 $S_{ans}$，如果 $S_{1-u}$ 的下界加 $S$ 都比最佳答案 $S_{ans}$ 大，就可以剪枝掉，即剪枝条件为

$$S+\frac{2(n-V)}{R_{u+1}}>=S_{ans}$$

5. 表面积剪枝：显然当前答案应该小于最佳答案

$$\sum_{i=u}^m S_i + \min{\sum_{i=1}^{u-1} S_i} < S_{ans}$$

### 搜索思路

```c++
// 当前层次 u 当前体积和 v 当前面积和 s
void dfs(int u, int v, int s) {
    if (...) return;                    // 剪枝

    if (u == 0) {
        if (v == n) res = s;
        return;
    }

    for (int r = rmax; r >= rmin; r--) {
        for (int h = hmax; h >= hmin; h--) {
            H[u] = h, R[u] = r;
            int t = u == m ? r * r : 0;  // 最底层加上表面面积
            dfs(u - 1, v + r * r * h, s + 2 * r * h + t);
        }
    }
}
```

## acwing 169 数独2

请你将一个 16×16 的数独填写完整，使得每行、每列、每个 4×4 十六宫格内字母 A∼P 均恰好出现一次。保证每个输入只有唯一解决方案。

### 思路

[@Lee2004](https://www.acwing.com/solution/content/4271/)

总体思路：每次找到一个空格，枚举空格选择哪个字母，然后往下递归。直到所有空格都填完。

对每个位置保存一个 16 位的二进制数，存储可以填的数字。每次递归之前，把这 256 个二进制数的状态进行保存，还原时直接恢复即可。

然后有很多剪枝：

1. 对于每个空格，如果不能填任何一个字母，则无解；如果只能填一个字母，那么直接填上;
2. 对于每一行，如果某个字母不能出现在任何一个位置，则无解；如果某个字母只有一个位置可以填，则直接填上；
3. 对于每一列，同2；
4. 对于每个16宫格，同2；
5. 每次选择空格时，选择备选方案(能填的字母数量)最少的格子来填。

## acwing 170 加成序列

满足如下条件的序列 X（序列中元素被标号为 1~m）被称为“加成序列”：

1. $X[1] = 1$，$X[m] = n$
2. $X[1]<X[2]<...<X[m]$
3. 对于每个 $k$ $(2\leq k\leq m)$ 都存在两个整数 $i$ 和 $j$ $(1\leq i, j \leq k-1)$ $i$ 和 $j$ 可相等，使得 $X[k]=X[i]+X[j]$。

### 思路

采用bfs的话，queue会迅速变大，是几何级增长的，代码会MLE。之所以使用dfs+限制深度来模拟bfs（迭代加深搜索），就是怕空间不足。（@糖豆）

```c++
// 用 maxu 限制最大搜索深度
bool dfs(int u, int maxu) {
    if (u == maxu) return ans[u] == n;

    bool vis[N] = {false};
    for (int i = u; i >= 1; i--)
        for (int j = i; j >= 1; j--) {
            int s = ans[i] + ans[j];
            if (vis[s] || s <= ans[u] || s > n) continue;

            vis[s] = true;
            ans[u + 1] = s;

            if (dfs(u + 1, maxu)) return true;
        }
    return false;
}
```

对于大测试样例（$n < 10000$），还需要增加一个剪枝。由于 $ans[i] <= ans[i-1] * 2$，如果当前已知 $ans[u]$，则后面最多还有 $maxu - u$ 项。若 $ans[u] * 2 ^ (maxu - u) < n$ 则说明肯定找不到答案。

ex：还有一个典型题 [P1763 埃及分数](https://www.luogu.com.cn/problem/P1763) 但是因为有太多 hack 数据所以实际变成了一道数学题。

# 广搜

## acwing 172 立体推箱子

操作一个 1×1×2 的长方体，从起点运到终点。典型的走地图问题。

### 思路

广搜是逐层遍历搜索树的算法，所有状态按照入队的先后顺序具有层次单调性。如果每一次扩展对应着一步，那么当一个状态第一次入队（被访问）时，就得到了从起始状态到该状态的最小步数。

在写广搜时，有一些常用的小技巧。

1. 使用常数数组保存沿着不同方向运动的变化情况，减少 if 语句的使用
2. 队列可以用头文件的 queue 实现，queue 也支持结构体，在入队时可以直接 `q.push( (...){...} )`。

```c++
struct State {int x, y, lie;};
bool check(int x, int y) {...}
int bfs(State start, State end) {
    queue<State> q;
    memset(dist, -1, sizeof dist);
    dist[start.x][start.y][start.lie] = 0;
    q.push(start);

    int d[3][4][3] = {...};

    while (q.size()) {
        auto t = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            State next = {t.x + d[t.lie][i][0], t.y + d[t.lie][i][1], d[t.lie][i][2]};

            int x = next.x, y = next.y;
            if (!check(x, y)) continue;
            if (next.lie == 0)
                if (g[x][y] == 'E') continue;
            else if (next.lie == 1)
                if (!check(x, y + 1)) continue;
            else
                if (!check(x + 1, y)) continue;

            if (dist[next.x][next.y][next.lie] == -1) {
                dist[next.x][next.y][next.lie] = dist[t.x][t.y][t.lie] + 1;
                q.push(next);
                if (next.x == end.x && next.y == end.y && next.lie == end.lie)
                    return dist[end.x][end.y][end.lie];
            }
        }
    }

    return -1;
}
```

## acwing 173 矩阵距离

算一个矩阵的有多个起始状态的 FloodFill。对于多个起始状态，在 BFS 初始化时将这些起始状态都插入到队列中即可。

## acwing 174 推箱子

推箱子游戏相信大家都不陌生，在本题中，你将控制一个人把 1 个箱子到目的地。

给定一张 N 行 M 列的地图，用字符 . 表示空地，字符 # 表示墙，字符 S 表示人的起始位置，字符 B 表示箱子的起始位置，字符 T 表示箱子的目标位置。

求一种移动方案，使箱子移动的次数最少，在此基础上再让人移动的总步数最少。

方案中使用大写的 EWSN（东西南北）表示箱子的移动，使用小写的 ewsn（东西南北）表示人的移动。

![acwing 174 pic](https://cdn.acwing.com/media/article/image/2019/01/16/19_8c8e5b0a19-%E6%8E%A8%E7%AE%B1%E5%AD%90.jpg)

### 思路

如果把箱子的步数和人的步数看做整体更新状态，在对每个状态进行扩展时，不能保证步数二元组的单调性。在队列不满足单调性时，有其他的解决方案（多次更新一个状态 / 优先队列），时间复杂度至少增加一个 log。

进一步分析可知，每次箱子移动后，人一定位于箱子之前在的位置上。所以可以分两步 BFS，第一次 BFS 求箱子到终点的路径，第二次 BFS 求人到箱子的路径。

# 广搜变形

## acwing 175 电路维修

![acwing 175 pic](https://cdn.acwing.com/media/article/image/2019/01/16/19_be6ff7a219-%E7%94%B5%E8%B7%AF.png)

从左上往右下走，只能斜着走，求至少需要旋转多少个方格才能到达右下。

### 思路

[@小呆呆](https://www.acwing.com/solution/content/21775/)

可以看成边权只有 0 和 1 的图。踩过格子到达想去的点时，需要判断是否需要旋转电线，若旋转电线表示从 当前点 到 想去的点 的边权是 1，若不旋转电线则边权是 0