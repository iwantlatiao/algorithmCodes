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

根据该定理，可以用**染色法**进行二分图的判定。大致思想为用两种颜色标记图中节点。当一个节点被标记后，所有相邻节点都应该标记反色。若产生冲突，则说明存在奇环。

[@yxc](https://www.acwing.com/solution/content/3042/)：将罪犯当做点，罪犯之间的仇恨关系当做点与点之间的无向边，边的权重是罪犯之间的仇恨值。那么原问题变成：将所有点分成两组，使得各组内边的权重的最大值尽可能小。

做法是使用二分枚举边权的最大值 `limit` 。判断能否将所有点分成两组，使得所有权值大于 `limit` 的边都在组间，即判断由所有点以及所有权值大于 `limit` 的边构成的新图是否是二分图。

