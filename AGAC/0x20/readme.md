# 1. 递归的形式

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

# 2. 深搜

## acwing 166 数独

数独 是一种传统益智游戏，你需要把一个 9×9 的数独补充完整，使得数独中每行、每列、每个 3×3 的九宫格内数字 1∼9 均恰好出现一次。请编写一个程序填写数独。

### 思路

- 对于每行、每列、每个九宫格分别用一个 9 位二进制数代表哪些数还可以填（二进制的与运算，然后用 lowbit 取能填的数字）
- 填上（删去）某个数后就要对二进制数的某位改成零（一）

## acwing 171 送礼物

一共有 N （$N<46$） 个物品，每个物品重 Gi，最大举起重量 W，求一次性能搬动的最大重量。

### 思路

双向 DFS。第一次 DFS 将前一半的所有重量组合求出，然后排序去重。第二次 DFS 将后一半的所有重量组合求出，然后在前一半的可能重量中二分查找最大的。总时间复杂度为 $O(2^x + 2^{n-x}\log 2^x)$

# 3. 剪枝

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

# 4. 广搜

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

# 5. 广搜变形

## acwing 175 电路维修

![acwing 175 pic](https://cdn.acwing.com/media/article/image/2019/01/16/19_be6ff7a219-%E7%94%B5%E8%B7%AF.png)

从左上往右下走，只能斜着走，求至少需要旋转多少个方格才能到达右下。

### 思路

[@小呆呆](https://www.acwing.com/solution/content/21775/)

可以看成边权只有 0 和 1 的图。踩过格子到达想去的点时，需要判断是否需要旋转电线，若旋转电线表示从 当前点 到 想去的点 的边权是 1，若不旋转电线则边权是 0

### Debug

在写代码的时候模仿 acwing 174 风格写了如下错误的搜索代码。分析错误原因，174 是正常的 bfs，元素仅从队尾进入，但 175 是双端队列，可能从队头进入。如下的写法不能保证单调性（应该插到队头的元素在插到队尾后就被置为真，无法插入队头），所以可能会搜索错误。

```c++
int bfs() {
    // ...
    while (!q.empty()) {
        auto t = q.front();
        q.pop_front();

        int x = t.first, y = t.second;
        for (int i = 0; i < 4; i++) {
            int a = x + dx[i], b = y + dy[i];  // 格点下一步的位置
            int j = x + ix[i], k = y + iy[i];  // 下一步要经过的大格

            if (0 <= a && a <= n && 0 <= b && b <= m) {
                int w = 0;
                if (g[j][k] != cs[i]) w = 1;

                if (!st[a][b]) { // 不能这样写
                    st[a][b] = true;
                    d[a][b] = d[x][y] + w;
                    if (w == 1) q.push_back(PII{a, b});
                    else q.push_front(PII{a, b});
                } else if (d[a][b] > d[x][y] + w) d[a][b] = d[x][y] + w;
            }
        }
    }
    // ...
}
```

正确的写法应该如下。也就是说，在双端队列、优先队列等情况，在从队列中取出元素时才判断是否已访问过，才能满足队列的单调性。

```c++
int bfs() {
    if (((n + m) & 1) == 1)
        return -1;

    memset(st, 0, sizeof st);
    memset(d, 0x3f, sizeof d);

    deque<PII> q;
    q.push_back(PII{0, 0});
    d[0][0] = 0;

    // 为了保证队列单调性, 权值为 0 的边从队头入,
    // 权值为 1 的边从队尾入, 取队头.
    while (!q.empty()) {
        auto t = q.front();
        q.pop_front();

        int x = t.first, y = t.second;
        // cout << x << " " << y << endl;
        if (st[x][y]) continue;
        st[x][y] = true;  // 没有负权边, 一个点不会经过两遍

        for (int i = 0; i < 4; i++) {
            int a = x + dx[i], b = y + dy[i];  // 格点下一步的位置
            int j = x + ix[i], k = y + iy[i];  // 下一步要经过的大格

            if (0 <= a && a <= n && 0 <= b && b <= m) {
                int w = 0;
                if (g[j][k] != cs[i]) w = 1;
                if (d[a][b] > d[x][y] + w) {
                    d[a][b] = d[x][y] + w;
                    if (w == 1) q.push_back(PII{a, b});
                    else q.push_front(PII{a, b});
                }
            }
        }
    }

    if (d[n][m] == INF) return -1;
    return d[n][m];
}
```

## acwing 176 装满的油箱

有 N 个城市和 M 条道路，构成一张无向图。在每个城市里边都有一个加油站，不同的加油站的单位油价不一样。

现在你需要回答不超过 100 个问题，在每个问题中，请计算出一架油箱容量为 C 的车子，从起点城市 S 开到终点城市 E 至少要花多少油钱？假定车子初始时油箱是空的。

### 思路

[@垫底抽风](https://www.acwing.com/solution/content/16438/)

如果不需要维护油箱容量，那么直接 Floyd 即可。现在需要在每个点上维护油箱容量，可以使用拆点的方法。

将第 i 个点拆成 pi 个点，每个点有两个属性，编号和剩余油量。然后正常做最短路即可。扩展结点的两种情况如下：

- 如果当前油箱容量没满，可以在当前点加一升油
- 遍历从该点出发的边，如果油箱里的油足够到下一个点，就插入下一个点的状态

### Debug

记得无向图建边是双向的，所以边矩阵大小要开两倍。

## acwing 177 噩梦

给定一张的地图，地图中有 1 个男孩，1 个女孩和 2 个鬼。

男孩每秒可以移动 3 个单位距离，女孩每秒可以移动 1 个单位距离，男孩和女孩只能朝上下左右四个方向移动。

每个鬼占据的区域每秒可以向四周扩张 2 个单位距离，并且无视墙的阻挡，也就是在第 k 秒后所有与鬼的曼哈顿距离不超过 2k 的位置都会被鬼占领。每一秒鬼会先扩展，扩展完毕后男孩和女孩才可以移动。

求在不进入鬼的占领区的前提下，男孩和女孩能否会合，若能会合，求出最短会合时间。

### 思路

双向 BFS。主要在于代码实现的细节。

# 6. A星

## acwing 178 第K短路

给定一个有 n 个结点，m 条边的有向图，求从 s 到 t 的所有不同路径中的第 k 短路径的长度。

### 算法介绍

[oi-wiki k短路](https://oi-wiki.org/graph/kth-path/)

A星算法定义了一个对当前状态 x 的估价函数 f(x)=g(x)+h(x)，其中 g(x) 为从初始状态到达当前状态的实际代价，h(x) 为从当前状态到达目标状态的最佳路径的估计代价。每次取出 f(x) 最优的状态 x，扩展其所有子状态，可以用 优先队列 来维护这个值。

在求解 k 短路问题时，令 h(x) 为从当前结点到达终点 t 的最短路径长度。可以通过在反向图上对结点 t 跑单源最短路预处理出对每个结点的这个值。

由于设计的距离函数和估价函数，对于每个状态需要记录两个值，为当前到达的结点 x 和已经走过的距离 g(x)，将这种状态记为 (x,g(x))。开始我们将初始状态 (s,0) 加入优先队列。每次我们取出估价函数 f(x)=g(x)+h(x) 最小的一个状态，枚举该状态到达的结点 x 的所有出边，将对应的子状态加入优先队列。当我们访问到一个结点第 k 次时，对应的状态的 g(x) 就是从 x 到该结点的第 k 短路。

优化：由于只需要求出从初始结点到目标结点的第 k 短路，所以已经取出的状态到达一个结点的次数大于 k 次时，可以不扩展其子状态。因为之前 k 次已经形成了 k 条合法路径，当前状态不会影响到最后的答案。

当图的形态是一个 n 元环的时候，该算法最坏是 O(nklogn) 的。但是这种算法可以在相同的复杂度内求出从起始点 s 到每个结点的前 k 短路。

## acwing 179 八数码

求解八数码问题的解决方案。

### 思路

[@E.lena](https://www.acwing.com/solution/content/35528/)

首先可以确认，逆序对数量为奇数肯定无解（每次移动逆序对变化数量为偶数，最终状态为偶数）。然后本题的搜索可以用双向 BFS 或 A 星（估价函数为曼哈顿距离）完成。

# 7. IDA星

估价函数和优先队列 BFS 结合，可以产生 A 星算法。那么估价函数和 DFS 结合，就可产生 IDA 星算法。

## acwing 180 Booksort

给定 n 本书，编号为 1 到 n。在初始状态下，书是任意排列的。在每一次操作中，可以抽取其中连续的一段，再把这段插入到其他某个位置。

我们的目标状态是把书按照 1 到 n 的顺序依次排列。求最少需要多少次操作。

### 思路

[你好世界wxx](https://www.acwing.com/solution/content/42928/)

分析复杂度：当抽取长度为 $i$ 时，有 $n-i+1$ 种选择方法，有 $n-i$ 个可插入的位置，并且抽前面插到后面等价于抽后面插到前面，所以还要除 2。最后可得复杂度为 $O(560^4)$。朴素 DFS 会超时，可以采用双向 BFS 或 IDA 星。

如果使用 IDA 星，则需考虑估价函数的设计。每次操作我们最多更改 3 个元素的后继关系，每次迭代前，我们可以计算出当前有多少个后继关系是不正确的，然后估计修复这些后继需要的最少步数。如果总步数大于题目要求步数，就可以直接回溯。

另外还有个小技巧，如果需要向上取整，可以通过转换为向下取整来实现。本题中的形式为 

$$\lceil\frac{tot}3\rceil=\lfloor\frac{tot+2}3\rfloor$$

## acwing 181 回转游戏

有一个 \# 形的棋盘，上面有三种数字各 8 个。棋盘可以沿着 \# 的直线进行操作，给定一个初始状态，请使用最少的操作次数，使 \# 形棋盘最中间的 8 个格子里的数字相同。

### 思路

[@chlchl](https://www.luogu.com.cn/problem/solution/UVA1343)

设计估计函数：如果中间的数中最多有 $m$ 个数字相同，那么我们最少只需要移动 $8 - m$ 次就可以得到结果。

实现细节：

- 读入不要构造矩阵，用一维数组存，每个位置就是其读入顺序的编号；
- 写一个矩阵，意思是每次循环移位会涉及到哪几个位置，注意按一定顺序写；
- 记录每个操作的逆操作，方便回溯时回复矩阵；

## acwing 182 破坏正方形

给定一个（完整或不完整）正方形网格，网格的边长小于等于 5，求至少再去掉多少根火柴棒，可以使得网格内不再含有任何尺寸的正方形。

![acwing182pic](https://cdn.acwing.com/media/article/image/2019/01/16/19_2af90edc19-%E7%81%AB%E6%9F%B4%E5%9B%BE.jpg)

### 思路

[@垫底抽风](https://www.acwing.com/solution/content/16644/)

设计估计函数：枚举所有未被删掉的正方形，将其所有边全部删掉，只记删除一条边。这样估计出的值一定不大于真实值，满足 IDA 星对估价函数的要求。其实这也是 Dancing Links 求解重复覆盖问题时的估价函数。

实现细节：

- 首先要处理出每个正方形的所有边编号。对于所有横着的火柴，我们将其坐标定义为其左端点坐标；对于所有竖着的火柴，我们将其坐标定义为其上端点坐标。求出坐标和火柴序号的对应关系后，就可以求出每个正方形所包含的所有火柴。
- 初始化时，预处理出每个正方形边的所有火柴序号并保存，使用一个 bool 数组记录删边情况。
- 找出最小的未被删除的正方形，依次枚举删除每条边。

# 8. 总结

## AcWing 183. 靶形数独

[@Junounly](https://www.acwing.com/solution/content/126788/)

数独等于 DFS 加 剪枝 加 位运算。剪枝策略是优先选分支少的格子。

## AcWing 184. 虫食算

[@西伯利亚挖番茄](https://www.acwing.com/solution/content/83532/)

实现细节：

- 将读入的字符数组转化为数字数组可以用 `ch - 'A'` 的方式实现
- 递归实现排列型枚举。手动做加法竖式时按照从右到左的顺序，因此我们也按照从右到左出现的次序枚举每个字母的选法。
- 对于每一列都有两种情况。一列的三个字母都确定（上一列全确定与未全确定），和一列三个字母未全确定。然后讨论加法的和与进位进行判断。

```c++
bool check()
{
    for (int i = n - 1, t = 0; i >= 0; i -- )  // t 表示进位，i 表示从后往前枚举列
    {
        int a = e[0][i] - 'A', b = e[1][i] - 'A', c = e[2][i] - 'A';    //转化 
        if (path[a] != -1 && path[b] != -1 && path[c] != -1)    //判断一列的三个字母是否都确定 
        {
            a = path[a], b = path[b], c = path[c];
            if (t != -1)    //上一列字母全部确定 
            {
                if ((a + b + t) % n != c) return false;
                if (!i && a + b + t >= n) return false;     //第一列特判 
                t = (a + b + t) / n; 
            }
            else    //上一列字母中有没有确定的
            {
                if ((a + b + 0) % n != c && (a + b + 1) % n != c) return false;     //若进位是0或1的两种情况取膜后均无法得到c则返回false 
                if (!i && a + b >= n) return false;     //第一列特判 
            }
        }
        else t = -1;
    }

    return true;    //历经百般磨难都没有false说明满足题意，成功返回true 
}

bool dfs(int u)
{
    if (u == n) return true;     

    for (int i = 0; i < n; i ++ )
        if (!st[i])
        {
            st[i] = true;   //某字母出现过 
            path[q[u]] = i;     //选择编号q[u](某字母)可能的数字i
            if (check() && dfs(u + 1)) return true;   //每次确定一个字母都进行check判断 
            st[i] = false;      //回溯 
            path[q[u]] = -1;
        }

    return false;   //已经判断过该组合无法满足题意，因此false 
}

int main()
{
    scanf("%d", &n);
    for (int i = 0; i < 3; i ++) scanf("%s", e[i]); 
    for (int i = n - 1, k = 0; i >= 0; i --)    
        for (int j = 0; j < 3; j ++)
        {
            int t = e[j][i] - 'A';
            if (!st[t])
            {
                st[t] = true;
                q[k ++ ] = t;   // 储存各字母第一次出现的顺序，便于枚举剪枝
            }
        }

    memset(st, 0, sizeof st);
    memset(path, -1, sizeof path);
    dfs(0);

    for (int i = 0; i < n; i ++ ) printf("%d ", path[i]);   //下标即为A,B,C... 

    return 0;
}
```

## AcWing 185. 玛雅游戏

## AcWing 186. 巴士

## AcWing 187. 导弹防御系统

## AcWing 188. 武士风度的牛

## AcWing 189. 乳草的入侵

## AcWing 190. 字串变换

## AcWing 191. 天气预报

## AcWing 192. 立体推箱子

## AcWing 193. 算乘方的牛

## AcWing 194. 涂满它

## AcWing 195. 骑士精神