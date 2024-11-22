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

[@小小蒟蒻](https://www.acwing.com/solution/content/11131/)

实现细节：

- 时间复杂度为 $O((nm)^5)$。搜索的方法是逐行列枚举该位置是否有小方块，如果有则向左或向右移动一格，查看是否可消去（可以用一个while循环，先处理悬空方块，然后查找可消去的方块并消去方块，直到没有可消去的方块为止。），然后继续递归。
- 搜索时需要保存和还原地图和颜色方块数量的状态。
- 有一些剪枝策略：如果方块左边有方块，则不向左移动（字典序）；如果某种颜色的方块只有一个或两个，则直接剪去该分支。

```c++
void hang() {  // 处理悬空的小方块
    for(int i = 0; i < 5; i++) {  // 枚举地图的每个位置，处理悬空的方块
        int y = 0;  // 查找从地面开始，按照纵向处理，完成后到下一列继续处理悬空小方格
        for(int j = 0; j < 7; j++) // (i, j)处有小方块悬空，依次移动到(i, y)处
            if(g[i][j]) g[i][y++] = g[i][j];  
        while(y < 7) g[i][y++] = 0; // 按纵向清理原来悬空处的小方格
    }
}

// f 告知地图更新的标记变量，false表示无需更新 (i, j) 查找位置的起始坐标
void same(bool& f, int i, int j) { // 寻找行或列上的同色相邻的小方块
    // d, u是一行同色小方块的起始，结束的横坐标
    int d = i, u = i;  // 起止初始化为0
    // 向左查找首个同色相邻小方块的行坐标
    while(d - 1 >= 0 && g[d - 1][j] == g[i][j]) d--; 
    // 向右查找末尾同色相邻小方块的行坐标
    while(u + 1 <  5 && g[u + 1][j] == g[i][j]) u++; 
    if(u - d + 1 >= 3) { // 横向存在至少有3个方格相邻的情况
        f = true;     // 告知要更新地图
        st[i][j] = true; // 标记地图将要更新的位置(i, j)
    }
    else { // 在纵向上查看是否存在至少3个同色的方块相邻
        // d, u是一行同色小方块的起始，结束的横坐标
        d = u = j; // 起止初始化为0
        // 向下查找首个同色相邻小方块的列坐标
        while(d - 1 >= 0 && g[i][d - 1] == g[i][j]) d--; 
        // 向上查找末尾同色相邻小方块的列坐标
        while(u + 1 <  7 && g[i][u + 1] == g[i][j]) u++; 
        if(u - d + 1 >= 3) { // 纵向存在至少有3个方格相邻的情况
            f = true;     // 告知要更新地图
            st[i][j] = true; // 标记地图将要更新的位置(x, y)
        }
    }
}

void update() {  // 更新地图
    for(int i = 0; i < 5; i++)
        for(int j = 0; j < 7; j++) {
            if(!st[i][j]) continue;  // 根据更新位置标记的bool值来过滤哪些坐标不用更新
            cnt[0]--;                // 更新方块的总数
            cnt[g[i][j]]--;          // 更新每种颜色的方块的总个数
            g[i][j] = 0;             // 地图上消除当前小方块
    }
}
// (a, b)小方块原来的位置，c小方块将要或右或左移动一次的目标位置的横坐标
void clear(int a, int b, int c) {  // 消除同色相邻的小方块
    swap(g[a][b], g[c][b]); // 交换两个相邻方格的位置
    while(true) {  // 尝试消除地图上的小方块
        memset(st, false, sizeof st); // 初始化状态数组
        bool flag = false; // 表示地图是否更新，false表示不更新地图
        hang();            // 处理悬空的小方块
        for(int i = 0; i < 5; i++)
            for(int j = 0; j < 7; j++) {
                if(!g[i][j]) continue; // 地图上的当前位置(x, y)处无小方格
                // 分别在横纵方向上查看是否存在至少3个同色的方块相邻
                same(flag, i, j);
            }
        if(!flag) break;  // 无需更新地图上的小方块
        update(); // 消除同色相邻的小方块
    }
}

bool dfs(int u) {  // 查找符合规定的小方块，并且按照要求消除它们
    if(u == n) return !cnt[0];  // 已经搜索完毕，返回方块总数的非值，总数为0返回真
    for(int i = 1; i <= 10; i++) // 搜索树剪枝，同色方块的个数为1或2，显然无法消除
        if(cnt[i] == 1 || cnt[i] == 2) return false; // 该搜索分支不用搜索
    memcpy(bg[u], g, sizeof g);   // 备份地图以及每种颜色小方块的总数
    memcpy(bcnt[u], cnt, sizeof cnt);
    for(int i = 0; i < 5; i++)     // 按照字典序枚举坐标值
        for(int j = 0; j < 7; j++) {
            if(!g[i][j]) continue;  // 地图中被枚举的位置不存在小方块，进入下一轮循环
            // 第一选择，小方块向右移一格
            if(i + 1 < 5) { // 小方格向右移动一格后的位置合法
               path[u] = { i, j, 1 };  // 保存当前状态下的操作
               clear(i, j, i + 1);  // 移动方块并且消除可以消除的小方块
               if(dfs(u + 1)) return true; // 继续搜索下一状态
               memcpy(g, bg[u], sizeof g);  // 恢复之前的状态，便于回溯
               memcpy(cnt, bcnt[u], sizeof cnt);
            }
            // 第二选择，小方块向左移一格
            if(i - 1 >= 0 && !g[i - 1][j]) { // 位置合法且该位置为空
               path[u] = { i, j, -1 };
               clear(i, j, i - 1);
               if(dfs(u + 1)) return true;
               memcpy(g, bg[u], sizeof g);
               memcpy(cnt, bcnt[u], sizeof cnt);
            }
        }
    return false;
}
```

## AcWing 186. 巴士

给定巴士到达时刻，求出巴士线路的最小总数量。

[@yxc](https://www.acwing.com/solution/content/4221/)

实现细节：

- 在读入时已有升序排序的巴士到达时刻，直接预处理出所有可能的线路（通过枚举起点和公差拿到所有等差数列，起点和公差需要满足两个条件：公差至少是起点加一；起点加公差一定小于六十）。
- 由于总路线数量较多，最多从中选出 17 条，但实现我们并不知道该选多少条，因此可以采用迭代加深搜索。
- 由于是枚举组合数，并不是排列数，为了避免重复在DFS时传入当前枚举的起点。将所有等差数列按长度降序排序，优先枚举长度较长的等差数列。这样在搜索树中前几层的分支少，可以更快地发现矛盾然后回溯。（如果不处理等差数列，直接用起点和标记进行枚举，此处就无法剪枝）
- 由于优先枚举长度较长的等差数列，当前路线覆盖的点数是最多的，如果 当前路线能覆盖的点数 乘 剩余可选的路径条数 加 当前已经覆盖的点数 小于 总点数，说明当前方案一定非法，直接回溯即可。

```c++
int n;
vector<pair<int, PII>> routes;
int bus[M];

bool is_route(int a, int d) {
    for (int i = a; i < 60; i += d)
        if (!bus[i]) return false;
    return true;
}

bool dfs(int depth, int u, int sum, int start) {
    if (u == depth) return sum == n;
    if (routes[start].first * (depth - u) + sum < n) return false;

    for (int i = start; i < routes.size(); i ++ ) {
        auto r = routes[i];
        int a = r.second.first, d = r.second.second;
        if (!is_route(a, d)) continue;
        for (int j = a; j < 60; j += d) bus[j] -- ;
        if (dfs(depth, u + 1, sum + r.first, i)) return true;
        for (int j = a; j < 60; j += d) bus[j] ++ ;
    }
    return false;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ) {
        int t; scanf("%d", &t); bus[t] ++ ;
    }

    for (int i = 0; i < 60; i ++ )
        for (int j = i + 1; i + j < 60; j ++ )
            if (is_route(i, j))
                routes.push_back({(59 - i) / j + 1, {i, j}});

    sort(routes.begin(), routes.end(), greater<pair<int, PII>>());

    int depth = 0; while (!dfs(depth, 0, 0, 0)) depth ++ ;
    printf("%d\n", depth); return 0;
}
```

## AcWing 187. 导弹防御系统

拓展：最长递增子序列的长度、数量；二维、三维最长递增子序列；最长非严格递增、有限递增子序列；与最长公共子序列的关系。

[最长递增子序列（nlogn 二分法、DAG 模型 和 延伸问题）](https://writings.sh/post/longest-increasing-subsequence-revisited)

[算法学习笔记(27): 最长上升子序列](https://zhuanlan.zhihu.com/p/121032448)

[用耐心排序证明 LIS 的 nlogn 做法](https://zhuanlan.zhihu.com/p/670544975)

[@yxc](https://www.acwing.com/solution/content/4258/)

一套防御系统的导弹拦截高度要么一直 严格单调 上升要么一直 严格单调 下降。给定即将袭来的一系列导弹的高度，请你求出至少需要多少套防御系统，就可以将它们全部击落。

实现细节：

- 搜索顺序：先从前往后枚举每颗导弹属于某个上升子序列还是下降子序列；然后如果属于上升子序列，则枚举属于哪个上升子序列（包括新开一个上升子序列），下降子序列同理。
- 可以通过记录每个上升、下降子序列的末尾数来快速判断当前数字能否接在某个序列的后面。（LIS 的 nlogn 做法记录的是每种长度子序列的末尾最小值）
- 在第二阶段的枚举中，如果枚举每一个上升子序列，则复杂度过高。对于上升序列，将当前的数字接在最大的数后面。（证明类似耐心排序）
- 最后还需要考虑如何求最小值。因为DFS和BFS不同，第一次搜索到的节点，不一定是步数最短的节点，所以需要进行额外处理。一般有两种处理方式：迭代加深；或者记录全局最小值，不断更新

```c++
bool dfs(int depth, int u, int su, int sd)
{
    // 如果上升序列个数 + 下降序列个数 > 总个数上限，则回溯
    if (su + sd > depth) return false;
    if (u == n) return true;

    // 枚举放到上升子序列中的情况
    bool flag = false;
    for (int i = 1; i <= su; i ++ )
        if (up[i] < h[u])
        {
            int t = up[i];
            up[i] = h[u];
            if (dfs(depth, u + 1, su, sd)) return true;
            up[i] = t;
            flag = true;
            break;  // 注意由上述证明的贪心原理，只要找到第一个可以放的序列，就可以结束循环了
        }
    if (!flag)  // 如果不能放到任意一个序列后面，则单开一个新的序列
    {
        up[su + 1] = h[u];
        if (dfs(depth, u + 1, su + 1, sd)) return true;
    }

    // 枚举放到下降子序列中的情况
    flag = false;
    for (int i = 1; i <= sd; i ++ )
        if (down[i] > h[u])
        {
            int t = down[i];
            down[i] = h[u];
            if (dfs(depth, u + 1, su, sd)) return true;
            down[i] = t;
            flag = true;
            break;  // 注意由上述证明的贪心原理，只要找到第一个可以放的序列，就可以结束循环了
        }
    if (!flag)  // 如果不能放到任意一个序列后面，则单开一个新的序列
    {
        down[sd + 1] = h[u];
        if (dfs(depth, u + 1, su, sd + 1)) return true;
    }

    return false;
}

int main()
{
    while (cin >> n, n)
    {
        for (int i = 0; i < n; i ++ ) cin >> h[i];

        int depth = 0;
        while (!dfs(depth, 0, 0, 0)) depth ++ ;     // 迭代加深搜索

        cout << depth << endl;
    }

    return 0;
}
```

## AcWing 188. 武士风度的牛

地图 BFS

## AcWing 189. 乳草的入侵

地图 Floodfill

## AcWing 190. 字串变换

已知有两个字串及一组字串变换的规则，求最小变换步数。

可以通过双向 BFS 减少时间复杂度。

```c++
int bfs() {
    unordered_map<string, int> da, db;  // 保存双向搜索时的变换步数
    queue<string> qa, qb;
    int step = 0;

    qa.push(A), qb.push(B);
    da[A] = 0, db[B] = 0;

    // 只要其中一个队列空，就说明无法变换到目标
    while (qa.size() && qb.size()) {
        int t;
        // 双向搜索，选择队列少的搜
        if (qa.size() < qb.size()) t = extend(qa, da, db, a, b);
        else t = extend(qb, db, da, b, a);
        if (t <= 10) return t;
        if (++step > 10) return -1;
    }

    return -1;
}
```

## AcWing 191. 天气预报

你负责掌控一个村子的天气状况，这个村子呈 4×4 的网格状分布，你拥有一片 2×2 大小的云，这片云不能到村子以外的地方。

你将获得一段时间内村子每个区域的赶集和过节时间表，希望土地在平时可以有足够的雨水，在赶集和过节能够充满阳光。判断整个时间段内，是否可以做到该下雨的地方下雨，不该下的地方不下。

一道很有趣的搜索题。如果直接搜索，由于需要让每个地方不下雨的时间不超过七天，存储并检查整个地图不好实现。但是其实可以把存整个地图转化为[存地图的四个角](https://www.acwing.com/solution/content/7518/)，这样 BFS 或 DFS 起来也方便。搜索时，保存一个 `vis[day][x][y][s0][s1][s2][s3]` 用于记录是否已经搜过这个点，其中 s 分别表示四个角的未降雨天数。

## AcWing 192. 立体推箱子 2

与立体推箱子一样，是一个 1x2 的方块，需要从 `(x, y)` 推到原点。不过地图中没有不能踩的点。数据范围是 `1e10` 。

[@chinaxjh](https://www.acwing.com/solution/content/5035/)：

首先这么大的数据范围肯定不能直接搜索，应该是有数学规律在里面。可以先用朴素 BFS 看下小范围数据的规律，然后写出各行各列的通项。

[@Z同学](https://www.acwing.com/solution/content/8587/)：

对于最小步数，可以发现只有横着横向滚动和竖着竖向滚动时，两步就能走三格，这是最快的。仔细观察可以发现，所有横纵坐标模 3 为 0，且是立着的状态到终点的最小步数我们能直接计算得出，对于这些状态假设叫做合适点，那么我们只要让起点状态用最小步数走到合适点上，那么从起点到终点的距离就可以相加得出。

```c++
struct node{int x,y,dir;};
int dist[7][7][4];  // 箱子的相对坐标到合适点的距离
bool check(int a,int b){return a>=0&&a<=6&&b>=0&&b<=6;}

// 在 7x7 的格子中搜，目标是到达 9 个可能的合适点
// 取模后原本应该是 (0,0) ~ (3,3) 4x4 格子，但由于箱子在翻时
// 坐标可能为负数所以把 (0, 0) -> (3, 3), (3, 3) -> (6, 6) ，即为 7x7 格子
int bfs(node start,int pastx,int pasty){
    int res = 2e9, d[3][4][3] = {/*...*/};
    queue<node> q; q.push(start);
    memset(dist,0x3f,sizeof dist);
    dist[start.x][start.y][start.dir] = 0;

    while(q.size()){
        auto t = q.front();
        q.pop();

        // 如果到了合适点
        if((t.x)%3==0&&(t.y)%3==0&&(t.dir)==0){
            // 计算合适点到终点的距离，平行坐标轴翻两下最多走 3 格
            // 这里的 continue 是剪枝，不选择负半轴的合适点
            // 但是没想到证明的方法（到负半轴再折返可能耗费更多），
            // 去掉该剪枝，并将距离做 abs 实际也能通过
            int bnsx = ((t.x-3)+pastx)/3*2, bnsy = ((t.y-3)+pasty)/3*2;
            if(bnsx<0||bnsy<0) continue;
            res = min(res,dist[t.x][t.y][0]+bnsx+bnsy);
        }
        for(int i=0;i<4;++i){
            int x = (t.x)+d[t.dir][i][0];
            int y = (t.y)+d[t.dir][i][1];
            int dir = d[t.dir][i][2];

            if(!check(x,y)) continue;
            if(dir==1&&!check(x,y+1)) continue;
            if(dir==2&&!check(x+1,y)) continue;

            if(dist[x][y][dir]==0x3f3f3f3f){
                dist[x][y][dir] = dist[t.x][t.y][t.dir]+1;
                q.push({x,y,dir});
            }
        }

    }
    return res;
}

int main(){
    char ch; int x,y;
    while(cin>>ch>>x>>y){
        int dir;
        if(ch=='H') dir = 1;
        else if(ch=='U') dir = 0;
        else dir = 2;
        node start = {x%3+3,y%3+3,dir};
        x-=x%3; y-=y%3;
        printf("%d\n",bfs(start,x,y));
    }
    return 0;
}
```

## AcWing 193. 算乘方的牛

有两个工作变量 0 和 1，希望通过这两个工作变量的反复加减凑出数字 P。所有中间结果都需要保存在中间变量中。计算最小操作次数。P 小于 2e4。

本题可以用 [A 星](https://www.acwing.com/solution/content/130270/)或 [IDA 星](https://www.acwing.com/solution/content/5039/)做。如果用 A 星，可以把估价函数写作 `log (P / max {varA, varB})` ，表示距离终点的最小操作次数。

本题有三个剪枝策略：

1. 首先容易考虑到：负数和零是不够优秀的。加减负数等效于减加正数，这样可以避免讨论多余的状态；而除了初始状态外，出现零是没有用的，因为这样相当于只有一个数可供操作。这样一定不会比这个非零的数与另一个非零的数合起来更优。因此，减法总是用大的减小的，不自己减自己。加法不保留 0。
2. 在当前深度限制下，如果剩下的步骤全部都把较大的数扩大为两倍还是比目标状态小，即 `(maxVar << (maxd - d)) < P`，显然剪枝。
3. 对于当前存储器中次数 `(a, b)`，设 `gcd(a, b) = d` ，两个工作变量的加或减一次的结果都是 d 的倍数，所以如果 `P % gcd(a, b) != 0` 则可以剪枝。

## AcWing 194. 涂满它

有一个 NxN 的方形区域，每个格子都属于六种颜色中的一种。玩家每次选择一种颜色并将与左上角连通的所有格子（包括左上角）都变成该种颜色。求最少要多少步才能把所有格子的颜色变成一样的。

![acwing 194](https://cdn.acwing.com/media/article/image/2019/01/17/19_c741618419-2.png)

[@fangzichang](https://www.acwing.com/solution/content/161264/) & [@小小_88](https://www.acwing.com/solution/content/104838/)

1. 不要修改原图中的颜色，而是用一个数组表示一个格子的三种状态：和起点已经相连 1；下一步可以被染色 2（即和某个状态为1的点相连，但是颜色不同）；没搜到 0。这样通过状态求连通块写的简单，只需要对 2 做拓展即可。
2. 若当前染色无效就跳过

```c++
// 将 (x, y) 及它附近颜色为 c 格子都加入连通块
void flood_fill(int x, int y, int c) {
    st[x][y] = 1;
    for (int i = 0; i < 4; i++) {
        int a = x + dx[i], b = y + dy[i];
        // 超出边界就跳过
        if (a < 0 || a >= n || b < 0 || b >= n) continue;
        // 之前已经和起点变成相同颜色就跳过
        if (st[a][b] == 1) continue;
        // 如果相邻格子颜色也是 c，就继续加入连通块操作
        // 否则，这个格子就是连通块的边界
        if (g[a][b] == c) flood_fill(a, b, c);
        else st[a][b] = 2;
    }
}

// 估价函数，统计不在连通块中的颜色个数
int f() {/*...*/}

bool dfs(int u) {
    int eval = f();
    if (u + eval > maxd) return false;
    if (eval == 0) return true;

    int bst[N][N];
    memcpy(bst, st, sizeof st);

    // 枚举下个变的颜色
    for (int c = 0; c < 6; c++) {
        bool ok = false;  // 连通块边界上是否有该颜色
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (st[i][j] == 2 && g[i][j] == c) {
                    ok = true;
                    flood_fill(i, j, c);
                }
        if (ok && dfs(u + 1)) return true;
        memcpy(st, bst, sizeof st);  // 这个方案不行，恢复状态
    }

    return false;
}
```

## AcWing 195. 骑士精神

给你一个 5x5 的棋盘，按照“马走日”的方式移动棋子，用最少的步骤把输入的棋盘恢复成原样

IDA 星：[@1e9+7](https://www.acwing.com/solution/content/8733/)

估价函数设计为：当前局面（除了空格）还有多少个棋子未归位

双向 BFS：[@墨染空](https://www.acwing.com/solution/content/4075/)