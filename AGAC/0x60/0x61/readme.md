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

