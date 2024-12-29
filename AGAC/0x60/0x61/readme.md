# 0x61 最短路

[OI Wiki 对最短路的介绍](https://oi-wiki.org/graph/shortest-path)

## 基本概念

对于一张有向图，可以使用邻接矩阵或邻接表两种方式进行存储。对于无向图，可以通过一条无向边建两条有向边转换为有向图进行存储。

邻接矩阵 A 可以表示为

$$
A[i,j] = 
\begin{cases}
    0, &i=j\\
    w(i,j), &(i,j)\in E\\
    +\infty , &(i,j)\notin E
\end{cases}
$$

邻接矩阵的空间复杂度为 $O(n^2)$ 。

邻接表可以通过数组模拟链表的形式实现。

```c++
// 邻接表：加入有向边(x, y)，权值为z
void add(int x, int y, int z) {
	ver[++tot] = y;  // 第 tot 条边的终点为 y
    edge[tot] = z; // 权值为 z
	next[tot] = head[x];  // 用头插法记录从 x 出发的边
    head[x] = tot; 
}

// 邻接表：访问从x出发的所有边
for (int i = head[x]; i; i = next[i]) {
	int y = ver[i], z = edge[i];
	// 一条有向边(x, y) 权值为z ...
}
```

## 单源最短路径

给定一个起点（设为 `1` ）和终点（设为 `x` ），要求求出从起点到终点的最短距离。

### Dijkstra 算法

Dijkstra 算法基于贪心算法，它要求该有向图所有边权值非负。它的算法流程如下：

1. 初始化 `dist[1]=0` ，其他 `dist=inf` 。
2. 找出一个未被标记的且是最小的 `dist[x]` ，然后标记节点 `x`
3. 扫描 `x` 的所有出边 `(x,y,z)` ，若 `dist[y]>dist[x]+z` 则 `dist[y]=dist[x]+z`
4. 重复 2~3 直到所有节点都被标记。

Dijkstra 的正确性：当边权都是非负数时，全局最小值不可能在被其他节点更新。故在第一步选出的节点必须是全局最小值（起点到该节点已经是最短路径）。这样不断选择全局最小值进行标记和扩展就可以得到起点 `1` 到每个节点的最短路。

以下代码实现朴素 Dijkstra ，时间瓶颈在第二步遍历寻找全局最小值，时间复杂度为 $O(N^2)$ 。

```c++
void dijkstra() {
	memset(d, 0x3f, sizeof(d)); // dist数组
	memset(v, 0, sizeof(v)); // 节点标记
	d[1] = 0;
	for (int i = 1; i < n; i++) { // 重复进行n-1次
		int x = 0;
		// 找到未标记节点中dist最小的
		for (int j = 1; j <= n; j++)
			if (!v[j] && (x == 0 || d[j] < d[x])) x = j;
		v[x] = 1;
		// 用全局最小值点x更新其它节点
		for (int y = 1; y <= n; y++)
			d[y] = min(d[y], d[x] + a[x][y]);
	}
}

int main() {
	cin >> n >> m;
	// 构建邻接矩阵
	memset(a, 0x3f, sizeof(a));
	for (int i = 1; i <= n; i++) a[i][i] = 0;
	for (int i = 1; i <= m; i++) {
		int x, y, z;
		scanf("%d%d%d", &x, &y, &z);
		a[x][y] = min(a[x][y], z);
	}
	// 求单源最短路径
	dijkstra();
	for (int i = 1; i <= n; i++)
		printf("%d\n", d[i]);
}
```

以下代码用二叉堆对 `dist` 数组进行维护，每次查询全局最小值的开销为 $O(\log N)$ ，总的时间复杂度为 $O(M\log N)$ 。

```c++
// 堆优化Dijkstra算法，O(mlogn)
// 大根堆（优先队列），pair的第二维为节点编号
// pair的第一维为dist的相反数（利用相反数变成小根堆，参见0x71节）
priority_queue< pair<int, int> > q;

void add(int x, int y, int z) {
	ver[++tot] = y, edge[tot] = z, 
    Next[tot] = head[x], head[x] = tot;
}

void dijkstra() {
	memset(d, 0x3f, sizeof(d)); // dist数组
	memset(v, 0, sizeof(v)); // 节点标记
	d[1] = 0;
	q.push(make_pair(0, 1));
	while (q.size()) {
		// 取出堆顶
		int x = q.top().second; q.pop();
		if (v[x]) continue;  // 相同节点可能出现多次
		v[x] = 1;
		// 扫描所有出边
		for (int i = head[x]; i; i = Next[i]) {
			int y = ver[i], z = edge[i];
			if (d[y] > d[x] + z) {
				// 更新，把新的二元组插入堆
				d[y] = d[x] + z;
				q.push(make_pair(-d[y], y));
			}
		}
	}
}

int main() {
	cin >> n >> m;
	// 构建邻接表
	for (int i = 1; i <= m; i++) {
		int x, y, z;
		scanf("%d%d%d", &x, &y, &z);
		add(x, y, z);
	}
	// 求单源最短路径
	dijkstra();
	for (int i = 1; i <= n; i++)
		printf("%d\n", d[i]);
}
```

### Bellman-Ford 算法和 SPFA 算法

Bellman–Ford 算法是一种基于松弛操作（其实 Dijkstra 算法也会用到松弛操作）的最短路算法，可以求出有负权的图的最短路，并可以对最短路不存在的情况进行判断。

对于边 `(u, v, w)` ，松弛操作对应着 `dis[v] = min(dis[v], dis[u] + w)` 。这么做的目的是尝试用 `S->u->v` 这条路径（其中 `S->u` 已经是最短路）去更新 `v` 点的最短路。如果这条路径更优，就进行更新。

Bellman–Ford 算法尝试对图上的每一条边进行松弛。每轮循环对所有边都进行一次松弛操作，当本次循环没有成功的松弛操作时算法停止。每次循环是 $O(m)$ 的，一轮松弛操作对最短路的贡献至少是一条边，所以最多执行 `n-1` 轮松弛操作。总的时间复杂度是 $O(nm)$ 。

但还有一种情况，如果从起点出发，抵达一个负环时，松弛操作会无休止地进行下去。注意到前面的论证中已经说明了，对于最短路存在的图，松弛操作最多只会执行 `n-1` 轮，因此如果第 `n` 轮循环时仍然存在能松弛的边，说明从起点出发能够抵达一个负环。

注意：以 S 点为源点跑 Bellman–Ford 算法时，如果没有给出存在负环的结果，只能说明从 S 点出发不能抵达一个负环，而不能说明图上不存在负环。因此如果需要判断整个图上是否存在负环，最严谨的做法是建立一个超级源点，向图上每个节点连一条权值为 0 的边，然后以超级源点为起点执行 Bellman–Ford 算法。

```c++
struct Edge {
  int u, v, w;
};
vector<Edge> edge;

int dis[MAXN], u, v, w;
constexpr int INF = 0x3f3f3f3f;

bool bellmanford(int n, int s) {
  memset(dis, 0x3f, (n + 1) * sizeof(int));
  dis[s] = 0;
  bool flag = false;  // 判断一轮循环过程中是否发生松弛操作
  for (int i = 1; i <= n; i++) {
    flag = false;
    for (int j = 0; j < edge.size(); j++) {
      u = edge[j].u, v = edge[j].v, w = edge[j].w;
      if (dis[u] == INF) continue;
      // 无穷大与常数加减仍然为无穷大
      // 因此最短路长度为 INF 的点引出的边不可能发生松弛操作
      if (dis[v] > dis[u] + w) 
        dis[v] = dis[u] + w,
        flag = true;
    }
    // 没有可以松弛的边时就停止算法
    if (!flag) break;
  }
  // 第 n 轮循环仍然可以松弛时说明 s 点可以抵达一个负环
  return flag;
}
```