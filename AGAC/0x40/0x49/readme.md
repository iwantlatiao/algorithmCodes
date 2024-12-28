# 总结与练习

## acwing 257 关押罪犯

题意：有 N 个罪犯，有些罪犯之间存在不同的仇恨值，存在仇恨值的罪犯对数为 M 。如果存在仇恨值的罪犯被关在不同监狱，则仇恨值不计入。现在有两座监狱，需要求出如何分配罪犯使得最大的仇恨值最小化。

思路：本题可以使用并查集或者二分图的方法解决。

### 方法 1. 扩展域并查集

[@秦淮岸灯火阑珊](https://www.acwing.com/solution/content/1001/)：很容易发现这道题目具有明显的贪心痕迹。即将仇恨值降序排序，优先将仇恨值大的罪犯分开。

```c++
struct node { long long a,b,c; } e[N];
int cmp(node a,node b) { return a.c>b.c; }
long long find(long long x) {
    return x==fa[x]?x:fa[x]=find(fa[x]);
}

int main() {
    // ...
    for(long long i=1; i<=(n<<1); i++) fa[i]=i;
    sort(e+1,e+m+1,cmp);
    for(int i=1; i<=m; i++) {
        int x=find(e[i].a), y=find(e[i].b);
        if(x==y)  // 在同一个集合
           { cout<<e[i].c; return 0; }
        fa[y]=find(e[i].a+n), fa[x]=find(e[i].b+n);
    }
    cout<<0; return 0;
}
```

### 方法 2. 带边权并查集

```c++
// @StkOvflow: https://www.acwing.com/solution/content/162753/
int find(int x) {
    if (x == p[x]) return x;
    int root = find(p[x]); d[x] ^= d[p[x]];
    return p[x] = root;
}

bool solve() {
    // ...
    for (int i = 1; i <= m; i ++ ) {
        int x = edge[i].u, y = edge[i].v;
        int px = find(x), py = find(y);
        if (px == py)  // 已经在一个集合内
            if (d[x] ^ d[y] == 0) return false;
        if (px != py)  // 还没有在一个集合内
            d[px] = d[x] ^ d[y] ^ 1, p[px] = py;
    }
    // ...
}
```

### 方法 3. 二分图判定

图论相关知识点在 0x60 章，这里仅对二分图进行简要介绍。

[OI Wiki 对二分图的介绍](https://oi-wiki.org/graph/bi-graph/)

如果一张无向图的 N 个节点可以分成两个非空集合 A 和 B，其中 $A \cap B = \emptyset$ 且在同一个集合内的点之间都没有边相连，那么称这张无向图为一张**二分图**，A 和 B 分别称为二分图的左部和有部。

定理：一张无向图是二分图，当且仅当图中不存在长度为奇数的环。

- 充分性证明：若是二分图，则每一条边都是从一个集合走到另一个集合，只有走偶数次才可能回到同一个集合。
- 必要性证明 [@离散数学笔记（10.3）二分图](https://zhuanlan.zhihu.com/p/388641049)：将该图拆成互补节点子集 A 和 B，其中 A 是所有与 v0 距离为偶数的点的集合，v0 可以任取。可以证明 A 中任意两点之间无边，B 同理。

根据该定理，可以用**染色法**进行二分图的判定。大致思想为用两种颜色标记图中节点。当一个节点被标记后，所有相邻节点都应该标记反色。若产生冲突，则说明存在奇环。时间复杂度为 $O(N+M)$ 。

[@yxc](https://www.acwing.com/solution/content/3042/)：将罪犯当做点，罪犯之间的仇恨关系当做点与点之间的无向边，边的权重是罪犯之间的仇恨值。那么原问题变成：将所有点分成两组，使得各组内边的权重的最大值尽可能小。

做法是使用二分枚举边权的最大值 `limit` 。判断能否将所有点分成两组，使得所有权值大于 `limit` 的边都在组间，即判断由所有点以及所有权值大于 `limit` 的边构成的新图是否是二分图。

```c++
const int N = 20010, M = 200010;
int n, m;
int h[N], e[M], w[M], ne[M], idx;
int color[N];

void add(int a, int b, int c) {
    e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx ++ ;
}

// 将节点 u 染色为 c ，仅操作权值大于 limit 的边
bool dfs(int u, int c, int limit) {
    color[u] = c;
    for (int i = h[u]; ~i; i = ne[i]) {
        if (w[i] <= limit) continue;
        int j = e[i];
        if (color[j])  // 若已染色且冲突
            if (color[j] == c) return false;
        else if (!dfs(j, 3 - c, limit)) return false;
    }
    return true;
}

bool check(int limit) {
    memset(color, 0, sizeof color);
    for (int i = 1; i <= n; i ++ )
        if (color[i] == 0)
            if (!dfs(i, 1, limit))
                return false;
    return true;
}

int main() {
    scanf("%d%d", &n, &m);
    memset(h, -1, sizeof h);
    while (m -- ) { 
        int a, b, c; scanf("%d%d%d", &a, &b, &c);
        add(a, b, c); add(b, a, c);
    }
    int l = 0, r = 1e9;
    while (l < r) {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;
        else l = mid + 1;
    }
    printf("%d\n", l);
    return 0;
}
```

也可以先对权值降序排序，然后加边，直到染色法发现冲突。

## acwing 258 石头剪子布

题目：N 个小朋友一起玩石头剪子布游戏。其中一人为裁判，其余的人被分为三个组（有可能有一些组是空的），第一个组的小朋友只能出石头，第二个组只能出剪子，第三个组只能出布，而裁判可以使用任意手势。你不知道谁是裁判，也不知道小朋友们是怎么分组的。要求通过 M 轮游戏结果推测谁是裁判，及最早找到裁判的轮数。

[@小小_88](https://www.acwing.com/solution/content/107416/)、[@YimingLi](https://www.acwing.com/solution/content/35836/) 思路：


首先可以联想到 [acwing 240 食物链](../0x41/readme.md#acwing-240-食物链) 分为三个组。但是由于存在裁判，所以不好处理。

由于裁判可以使用任意手势，所以不妨枚举每个人为裁判的情况。当枚举到某个人为裁判时，直接将这个人相关的对局忽略（裁判可以使用任意手势）。对于所有其他对局：

1. 如果这些对局都是合法的，那么这个人可能是裁判，裁判计数加一。
2. 如果存在不合法对局，说明这个人不是裁判。记录第一个不合法对局的编号，表示最早发现这个人不是裁判的位置。

最终会得出可能的裁判人数：

1. 裁判人数 > 1，可能的裁判有多个，输出不确定。
2. 裁判人数 = 1，只有一个裁判，需要输出裁判的编号和最早确定裁判的轮数，我们需要确定其他所有人不是裁判才能确定当前人是裁判。因此需要枚举其他所有不是裁判的人，从最早判断它们不是裁判的轮数中取一个最大值，就是最早能排除其他人确定当前人是裁判的位置。
3. 裁判人数 = 0，没有裁判，输出没有。

```c++
int find(int x) {
    if(x == p[x]) return x;
    int root = find(p[x]);
    d[x] = (d[x] + d[p[x]]) % 3;
    return p[x] = root;
}

bool check(int k) {  //判断第k轮对局是否合法
    int x = a[k], y = b[k]; //取出两个人
    int t = 1; //记录大小关系, x<y 1，x=y 0
    if(c[k] == '=') t = 0;
    if(c[k] == '>') swap(x, y); //保证 x < y

    int px = find(x), py = find(y);
    if(px == py) //同一集合
        if(d[x] != (d[y] + t) % 3) return false; //距离不符，对局不合法
    else //不在同一集合，合并
        p[px] = py,
        d[px] = (d[y] - d[x] + t + 3) % 3; //这里+3取模，保证正余数

    return true; //到这说明对局合法
}

int main() {
    while(cin >> n >> m) {
        for(int i = 1; i <= m; i++) 
            scanf("%d%c%d", &a[i], &c[i], &b[i]);
        memset(f, 0, sizeof f); //重置轮数
        //cnt 表示可能是裁判的人数，num 表示裁判的编号
        int cnt = 0, num = 0; 
        for(int i = 0; i < n; i++) {  //枚举所有人
            //初始化并查集
            for(int j = 0; j < n; j++) p[j] = j, d[j] = 0; 
            bool is_umpire = true; //记录当前人有没有可能是裁判
            //如果其他对局中存在矛盾，说明当前人不是裁判
            for(int j = 1; j <= m; j++)          
                if(a[j] != i && b[j] != i && !check(j)) {
                    is_umpire = false; //修改标记
                    f[i] = j; //记录最早确定当前人不是裁判的轮数
                    break; //跳出循环
                }

            if(is_umpire) //如果当前人可能是裁判
                cnt++, //裁判人数+1
                num = i; //记录裁判编号
        }

        if(!cnt) puts("Impossible"); //没有裁判
        else if(cnt > 1) puts("Can not determine"); //多个裁判
        else {
            int res = 0; //记录最早能确定裁判的轮数
            for(int i = 0; i < n; i++) //枚举所有人
                if(i != num) //如果当前人不是裁判
                    res = max(res, f[i]); //更新最早确定轮数
            printf("Player %d can be determined to be the judge after %d lines\n", num, res);
        }
    }
    return 0;
}
```

## acwing 259 真正的骗子

题意：一个岛上存在着两种居民，天神和恶魔。天神永远都不会说假话，而恶魔永远都不会说真话。岛上的每一个成员都有一个整数编号。现在有来自 n 个居民的信息，内容是其中一个居民询问另一个居民是否是天神。请你根据收集的回答判断各个居民的身份。

[@小小_88](https://www.acwing.com/solution/content/107684/)、[@垫底抽风](https://www.acwing.com/activity/content/code/content/1697652/) 思路：

首先，每次询问都会告诉我们一个信息：其中一个居民询问另一个居民是否是天神。

1. 另一个居民是天神：两个居民是同类（同时为天神，或同时为恶魔）
2. 另一个居民是恶魔：两个居民是不同类

天神和恶魔的数量已知，需要根据信息指定唯一的方案。

根据询问我们可以用带权并查集建立关系，首先会有若干个集合，每个集合中都会有同类的和异类的。

我们假设同类的节点之间的距离为 0，异类的节点之间的距离为 1 。那么每个集合都可以分成两类，一类是和根节点距离为 0 的节点，一类是和根节点距离为 1 的节点。由于每两个集合是毫不相干的，因为若是有关系就会变成一个集合。所以对于每个集合，我们都可以让两类中的任意一类是天神，另一类是恶魔。

那么现在要求的问题就变成了给定 m 个集合，从中选出 p1 个天神的方案数。

方案唯一，那么说明有解，否则说明无解。对于每个集合中只能选出一类作为天神，这就是一个简单的 01 背包求方案数。

然后如果有解，还需要输出所有天神的编号，因此在用 01 背包求方案数的同时还需要记录具体方案。

### 1. 边带权并查集写法

边带权并查集可以用边权维护与子节点和根节点是否是一类，并在合并时记录对应类别的个数。

1.  `s[0][i]`，`s[1][i]` 维护第 i 个节点所在集合中距离根节点为 0 和 1 的节点个数
2.  `v0[i]`， `v1[i]` 维护第 i 个集合中距离根节点为 0 和 1 的节点个数
3.  `f[i][j]` 表示前 i 个集合中，选取恰好 j 个天使的方案数
4.  `g[i][j]` 表示 `f[i][j]` 是选了第 i-1 个集合中距离根节点是 0 的状态还是距离根节点是 1 的状态转移过来的

```c++
// @小小_88: https://www.acwing.com/solution/content/107684/

int find(int x) {
    if(x == p[x]) return x;
    int root = find(p[x]);
    d[x] ^= d[p[x]];  // 与根节点相同为 0 不同为 1
    return p[x] = root;
}

int main() {
    while(scanf("%d%d%d", &n, &p1, &p2), n || p1 || p2) {
        for(int i = 1; i < N; i++) // 初始化并查集
            p[i] = i, d[i] = 0, s[0][i] = 1, s[1][i] = 0; 

        // 枚举所有询问 
        for(int i = 1; i <= n; i++) {  
            int a, b;
            char op[5];
            scanf("%d%d%s", &a, &b, op);
            int t = 0; //yes，说明两个居民同类，距离为0
            if(op[0] == 'n') t = 1; //否则异类，距离为1

            int pa = find(a), pb = find(b);
            if(pa != pb) {  // 不在同一集合则合并
                p[pa] = pb; d[pa] = d[a] ^ d[b] ^ t;
                s[0][pb] += s[d[pa]][pa]; //pa ^ pa = 0
                s[1][pb] += s[d[pa] ^ 1][pa]; //pa ^ pa ^ 1 = 1
            }
        }

        // 初始化所有集合中的居民数量
        memset(v0, 0, sizeof v0); memset(v1, 0, sizeof v1);
        int cnt = 0; //总集合数
        for(int i = 1; i <= p1 + p2; i++) //枚举所有居民
            if(i == find(i)) {  //如果当前居民是它的集合的根节点，说明找到一个集合
                cnt++; //集合数+1
                v0[cnt] = s[0][i]; //记录当前集合中距离根节点为0的居民数量
                v1[cnt] = s[1][i]; //记录当前集合中距离根节点为1的居民数量
                pos[cnt] = i;
            }

        //01背包求方案数
        memset(f, 0, sizeof f); memset(g, 0, sizeof g); //初始化
        f[0][0] = 1; //边界方案数是1
        for(int i = 1; i <= cnt; i++) {  //枚举所有集合
            for(int j = p1; j >= v0[i]; j--) //枚举选取距离根节点为0的居民
                if(f[i - 1][j - v0[i]]) //如果当前集合存在距离根节点为0的居民
                    f[i][j] += f[i - 1][j - v0[i]], //状态转移方程
                    g[i][j] = 0; //记录从距离为0的居民转移过来

            for(int j = p1; j >= v1[i]; j--) //枚举选取距离根节点为1的居民
                if(f[i - 1][j - v1[i]]) //如果当前集合存在距离根节点为1的居民
                    f[i][j] += f[i - 1][j - v1[i]], //状态转移方程
                    g[i][j] = 1; //记录从距离根节点为1的居民转移过来
        }

        if(f[cnt][p1] != 1) puts("no"); //方案不唯一，无解
        else {
            //01背包求具体方案
            //idx 表示天神个数，m 表示居民总个数，由于p1会变动，所以需要存起来
            int idx = 0, m = p1 + p2;
            while(cnt) {  //倒推每一个集合的选法
                //枚举所有居民，将属于当前集合，且属于该集合中选取的那一部分加入答案
                for(int i = 1; i <= m; i++) 
                    if(find(i) == pos[cnt] && d[i] == g[cnt][p1])
                        res[idx++] = i; 
                if(g[cnt][p1]) p1 -= v1[cnt]; //选取了距离根节点为1的居民，就减去这部分的数量
                else p1 -= v0[cnt]; //否则减去距离根节点为2的居民数量
                cnt--; //当前集合选完，集合数-1，回到上一个状态
            }
            sort(res, res + idx); //将所有居民编号有序输出
            for(int i = 0; i < idx; i++) printf("%d\n", res[i]);
            puts("end");
        }
    }
    return 0;
}
```

### 2. 扩展域并查集写法

扩展域并查集通过将点集扩大一倍维护不同点是否是一类。设总人数有 `n` 个，在初始化时，仅将小于等于 `n` 的点数数组 `sz` 设置为 `1` ，大于的设置为 `0` ，这样在合并时 `sz[y] += sz[x]` 就只统计了第一类的点数。

不妨将第一类设为天神，在做 01 背包时如何拿到第二类的数量呢？由于在每一次合并时实际上是合并了两次（每一次合并两个集合），对大于 `n` 的集合也做了维护（反集），所以 `sz[find(x)]` 是 `x` 的第一类点数量，而 `sz[find(x+n)]` 就是 `x` 的第二类点数量。这样实际就维护了边带权并查集中的 `s[x][i]` 信息。

```c++
// @垫底抽风: https://www.acwing.com/activity/content/code/content/1697652/

int find(int x) { return x != p[x] ? p[x] = find(p[x]) : x; }
bool check(int x, int y) { return find(x) == find(y);} 
void merge(int x, int y) {
    x = find(x), y = find(y);
    if (x == y) return;
    p[x] = y, sz[y] += sz[x];
}

bool check() {
    memset(st + 1, false, n << 1);
    memset(f, 0, sizeof f);
    k = 0, f[0][0] = 1;
    for (int x = 1; x <= n; ++x) {
        if (x == find(x) && !st[x]) {
            int y = find(x + n);
            st[x] = st[y] = true;
            ++k;
            v[k][0] = x, v[k][1] = y;
            for (int i = 0; i <= n; ++i) {
                if (i >= sz[x]) f[k][i] += f[k - 1][i - sz[x]];
                if (i >= sz[y]) f[k][i] += f[k - 1][i - sz[y]];
            }
        }
    }
    return f[k][n1] == 1;
}

int main() {
    while (scanf("%d%d%d", &m, &n1, &n2), m || n1 || n2) {
        n = n1 + n2;
        for (int i = 1; i <= n << 1; ++i) 
            p[i] = i, sz[i] = (i <= n);
        
        for (int i = 0; i < m; ++i) {
            scanf("%d%d%s", &x, &y, str);
            if (!strcmp(str, "no")) {
                merge(x, y + n), merge(x + n, y);
            } else {
                merge(x, y), merge(x + n, y + n);
            }
        }

        if (check()) {
            memset(st + 1, false, n << 1);
            int i = n1;
            while (k) {
                int cur = v[k][0];
                if (f[k - 1][i - sz[cur]] != 1) 
                    cur = v[k][1];
                st[cur] = true;
                i -= sz[cur], --k;
            }
            for (int x = 1; x <= n; ++x) 
                if (st[find(x)]) printf("%d\n", x);
            puts("end");
        } 
        else puts("no");
    }
    return 0;
}
```

## acwing 260 买票

题意：有 N 个数字依次插入初始为空的数组中，给定每个数插入时前面的数字个数，要求维护最终数组的数字顺序。

实际上和 [acwing 244 谜一样的牛](../0x42/readme.md#acwing-244-谜一样的牛) 思路相同。

## acwing 261 旅馆

题意：在长度为 N 的数列中维护两个操作。

1. 开房：查询一段连续区间，且区间全为 0 。然后将该区间所有数设置为 1 。
2. 退房：将区间所有数设置为 0 。

输出每次开房业务的第一个房间号码，如果无法安排则输出 0 。

思路 [@小小_88](https://www.acwing.com/solution/content/107776/) ：

要求区间查询、区间修改，容易想到用线段树来实现。

联想 [acwing 245 你能回答这些问题吗](../0x43/readme.md#acwing-245-你能回答这些问题吗) ，考虑维护 `[l,r]` 的最长连续空房间 `d` 需要维护哪些信息：

1. 对于连续的空房间 `tr[x].d` 可能是左子节点的连续空房 `tr[x<<1].d` 、右子节点的连续空房 `tr[x<<1+1].d` 或左子节点的最长连续右空房加右子节点的最长连续左空房 `tr[x<<1].rd+tr[x<<1+1].ld` 。
2. 对于最长连续左空房 `tr[x].ld` ，如果左子节点最长连续左空房就是整个区间，则可以加上右子节点的最长连续左空房，否则只能是左子节点的最长连续左空房。最长连续右空房同理。

```c++
struct Node {
    int l, r; int d, ld, rd, low;
}tr[N * 4];  // low 懒标记 -1 表示无懒标记，0 表示房间为空，1 表示房间有人

void build(int u, int l, int r) {  // 初始化线段树
    // 直接给 tr[u] 赋值就相当于 pushup ，只是另一种写法。
    tr[u] = {l, r, r - l + 1, r - l + 1, r - l + 1, -1};
    if(l != r) {
        int mid = l + r >> 1;
        build(u << 1, l, mid), build(u << 1 | 1, mid + 1, r);
    }
}

void pushup(int u) {  // 通过子节点的信息获取父节点的信息
    tr[u].ld = tr[u << 1].ld; //父节点的前缀就是左子区间的前缀
    //如果左子区间的前缀就是整个区间，则再加上右子区间的前缀
    if(tr[u << 1].ld == tr[u << 1].r - tr[u << 1].l + 1) 
        tr[u].ld += tr[u << 1 | 1].ld;

    tr[u].rd = tr[u << 1 | 1].rd; //父节点的后缀就是右子区间的后缀
    //如果右子区间的后缀就是整个区间，则再加上左子区间的后缀
    if(tr[u << 1 | 1].rd == tr[u << 1 | 1].r - tr[u << 1 | 1].l + 1) 
        tr[u].rd += tr[u << 1].rd;

    //父节点的最长连续空房间的长度，从三个部分中来更新
    tr[u].d = max(max(tr[u << 1].d, tr[u << 1 | 1].d), tr[u << 1].rd + tr[u << 1 | 1].ld);
}

void pushdown(int u) {  //将父节点的懒标记传递给子节点
    if(tr[u].low == -1) return; //没有懒标记，直接返回
    tr[u << 1].low = tr[u << 1 | 1].low = tr[u].low;

    if(tr[u].low) {  //房间有人
        //不存在空房间
        tr[u << 1].d = tr[u << 1].ld = tr[u << 1].rd = 0; //左子区间
        tr[u << 1 | 1].d = tr[u << 1 | 1].ld = tr[u << 1 | 1].rd = 0; //右子区间
    }
    else {  //房间为空
        //连续的空房间长度就是区间长度
        tr[u << 1].d = tr[u << 1].ld = tr[u << 1].rd = tr[u << 1].r - tr[u << 1].l + 1; 
        tr[u << 1 | 1].d = tr[u << 1 | 1].ld = tr[u << 1 | 1].rd = tr[u << 1 | 1].r - tr[u << 1 | 1].l + 1;
    }
    tr[u].low = -1; //将父节点的懒标记清空
}

// 查询最靠左的长度为d的连续空房间，并返回第一个房间的下标
// 这里没有把区间 [l,r] 传参，原因是题目只给了 d
int query(int u, int d) {  
    if(tr[u].l == tr[u].r) return tr[u].l; //如果只有一个房间，直接返回

    pushdown(u); //递归之前传递懒标记
    if(tr[u << 1].d >= d) return query(u << 1, d); //递归左区间

    int mid = tr[u].l + tr[u].r >> 1;
    //如果两个区间中间存在长度为d的连续空房间，直接最左端点
    if(tr[u << 1].rd + tr[u << 1 | 1].ld >= d) return mid - tr[u << 1].rd + 1;

    if(tr[u << 1 | 1].d >= d) return query(u << 1 | 1, d); //递归右区间

    return -1; //否则说明不存在长度为d的连续空房间，返回-1
}

//将 [l, r] 之间的所有房间标记为d，1 表示房间有人，0 表示房间为空
void modify(int u, int l, int r, int d) {
    if(tr[u].l >= l && tr[u].r <= r) {  //如果当前节点包含在查询区间中
        if(d) //设置为房间有人
            tr[u].d = tr[u].ld = tr[u].rd = 0, //不存在空房间
            tr[u].low = 1; //用懒标记表示下面所有子房间都有人
        else //设置为房间为空
            tr[u].d = tr[u].ld = tr[u].rd = tr[u].r - tr[u].l + 1, //空房间长就是区间长
            tr[u].low = 0; //用懒标记表示下面所有子房间都为空
        return;
    }

    pushdown(u); //递归之前传递懒标记
    int mid = tr[u].l + tr[u].r >> 1;
    if(l <= mid) modify(u << 1, l, r, d); //递归左子区间
    if(r > mid) modify(u << 1 | 1, l, r, d); //递归右子区间
    pushup(u); //用子节点信息更新父节点信息
}

int main() {
    scanf("%d%d", &n, &m);
    build(1, 1, n); //初始化线段树

    int op, x, d;
    while(m--) {
        scanf("%d", &op);
        if(op == 1) {
            scanf("%d", &d);

            if(tr[1].d < d) puts("0"); //不存在长度为d的连续空房间
            else {
                int res = query(1, d); //寻找最靠左的长度为d的连续空房间的第一个房间的下标
                printf("%d\n", res);
                modify(1, res, res + d - 1, 1); //将 [res, res + d - 1] 修改为有人
            }
        }
        else {
            scanf("%d%d", &x, &d);
            modify(1, x, x + d - 1, 0); //将 [x, x + d - 1] 修改为空房
        }
    }
    return 0;
}
```

## acwing 262 海报

题意：求矩形周长并

矩形面积并和周长并详见 [0x43 线段树与扫描线](../0x43/readme.md#扫描线) 。