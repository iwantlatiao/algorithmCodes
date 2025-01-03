# 0x41 并查集

## 概念

[OI-Wiki 并查集介绍](https://oi-wiki.org/ds/dsu/)

[@Pecco 对并查集的介绍](https://zhuanlan.zhihu.com/p/93647900)

[先前做过部分有关并查集的题目](../../../luogu_training_list/2-3_set/readme.md)

并查集支持两种操作：

1. 合并（Union）：合并两个元素所属集合（合并对应的树）
2. 查询（Find）：查询某个元素所属集合（查询对应的树的根节点），这可以用于判断两个元素是否属于同一集合

并查集在经过修改后可以支持单个元素的**删除**（[HDU 2473](http://acm.hdu.edu.cn/showproblem.php?pid=2473)）、移动；使用动态开点线段树还可以实现可持久化并查集。

并查集常用两种优化方法：路径压缩与按秩合并。

1. 路径压缩：查询过程中经过的每个元素都属于该集合，我们可以将其直接连到根节点以加快后续查询。
2. 按秩合并：合并时，选择哪棵树的根节点作为新树的根节点会影响未来操作的复杂度。我们可以将节点较少或深度较小的树连到另一棵，以免发生退化。（注意，秩不是准确的子树高，而是子树高的上界，因为路径压缩可能改变子树高。还可以将秩定义成子树节点数，因为节点多的树倾向更高。无论将秩定义成子树高上界，还是子树节点数，按秩合并都是尝试合出最矮的树，并不保证一定最矮。）

如果只使用路径压缩的最坏时间复杂度是 $O(m\log n)$，平均情况下是 $O(m\alpha(m,n))$。只使用启发式合并，而不使用路径压缩，时间复杂度为 $O(m\log n)$。由于路径压缩单次合并可能造成大量修改，有时路径压缩并不适合使用。例如，在可持久化并查集、线段树分治 + 并查集中，一般使用只启发式合并的并查集。

```c++
void init(int n) { for(int i = 1; i <= n; ++i) fa[i] = i; }
void merge(int i, int j) { fa[find(i)] = find(j); }

// 路径压缩
int find(int x) { return x == fa[x] ? x : (fa[x] = find(fa[x])); }  

// 按秩合并
void init(int n) { for(int i = 1; i <= n; ++i) fa[i] = i, rank[i] = 1; }
void merge(int i, int j) {
    int x = find(i), y = find(j);  // 先找到两个根节点
    if (rank[x] <= rank[y]) fa[x] = y;
    else fa[y] = x;
    // 如果深度相同且根节点不同，则新的根节点的深度 + 1
    if (rank[x] == rank[y] && x != y) rank[y]++;                   
}
```

### acwing 237 程序自动分析

题意：给定多个 $x_i=x_j$ 和 $x_i\neq x_j$ 的条件，判断能否同时满足。

思路：每个相等的条件可以看成无向图中的一条边，每个 $x$ 看成图的一个节点。两个变量相等当且仅当它们联通。于是可以把变量分成若干个集合，每个集合都对应无向图中的一个连通块。

有两种方法求出这些集合。第一种是建出该无向图，用 DFS 划分出每个连通块。第二种是用并查集动态维护。起初所有变量各自是一个集合，对于每个相等的条件，合并两个集合。扫描完所有相等条件后，判断不等条件中两个变量是否有处在同一个集合中的情况。如果处在同一个集合，则无解。

### acwing 145 超市

题意：超市里有 N 件商品，每件商品都有利润 pi 和过期时间 di，每天只能卖一件商品，过期商品不能再卖。求合理安排每天卖的商品的情况下，可以得到的最大收益是多少。

#### 思路一：贪心 + 小根堆

贪心思路是在不卖出过期物品的情况下，尽量卖贵的。

将物品按照过期时间升序排序。同时建立一个初始为空的小根堆，堆的关键字为物品价值。堆中的所有元素即为需要卖的物品。依次扫描每个物品。

1. 如果当前物品的过期天数大于当前堆中的元素个数，则直接加入。
2. 如果当前物品的过期天数等于当前堆中的元素个数，比较堆顶和当前物品的价值。如果当前物品更贵，则替换掉堆顶。
3. 由于物品按照过期时间升序排序，所以不会出现小于的情况。

#### 思路二：贪心 + 并查集

贪心思路是先卖最贵的，同时尽量晚卖（占用更晚的时间，对其他商品更好）。

将物品按照价值降序排序。同时建立一个关于“天数”的并查集。起初每一天各自构成一个集合，对于每个物品，如果它在第 d 天后过期，就在并查集中查询 d 的树根 r。若 r 不为 0，则说明可以在第 r 天卖，并把 r 的树根设为 r-1。若 r 为 0 则说明前 r 天卖的方案已经最优。

这个并查集实际上维护了位置（天数）的占用情况。每个位置所在集合的根就代表从它往前数第一个空闲的位置（包括自身）。当一个位置被占用，就把该位置往前指。利用并查集的路径压缩，就可以快速找到最晚能卖出的时间。

## 扩展域、边带权的并查集

并查集实际上是由若干棵树构成的森林，我们可以在树中的每条边上记录一个权值，即维护一个数组 d，用 `d[x]` 保存节点 x 到父节点 `fa[x]` 之间的边权。在每次路径压缩后，每个访问过的节点都会直接指向树根，如果我们同时更新这些节点的 d 值，就可以利用路径压缩过程来统计每个节点到树根之间的路径上的一些信息。这就是所谓“边带权”的并查集。

### acwing 238 银河英雄传说

有一个划分为 N 列的星际战场，各列依次编号。有 N 艘战舰，也依次编号，其中第 i 号战舰处于第 i 列。现在需要处理一系列的指令。每条指令格式为以下两种之一：

1. 让第 i 号战舰所在列的全部战舰保持原有顺序，接在第 j 号战舰所在列的尾部。
2. 询问第 i 号战舰与第 j 号战舰当前是否处于同一列中，如果在同一列中，它们之间间隔了多少艘战舰。

#### 思路

一条“链”也是一棵树，只不过是树的特殊形态。因此可以把每一列战舰看作一个集合，用并查集维护。最初，N 个战舰构成 N 个独立的集合。

在没有路径压缩的情况下，`fa[x]` 就表示排在第 x 号战舰前面的那个战舰的编号，一个集合的代表就是位于最前边的战舰。另外，让树上每条边带权值 1，这样树上两点之间的距离减 1 就是二者之间间隔的战舰数量。

在考虑路径压缩的情况下，我们额外建立一个数组 d，`d[x]` 记录战舰 x 与 `fa[x]` 之间的边的权值。在路径压缩把 x 直接指向树根的同时，我们把 `d[x]` 更新为从 x 到树根的路径上的所有边权之和。对 get 函数稍加修改，即可实现对 `d[x]` 数组的维护。（注：`d[x]` 在所有情况下都是到父节点的权值，没更新的时候也是。）

```c++
// @秦淮岸灯火阑珊 https://www.acwing.com/solution/content/1005/
int get(int x) {
    if (x==fa[x]) return x;
    int root=get(fa[x]);  // 递归计算集合代表
    d[x]+=d[fa[x]];  // 通过上一行的 get 递归维护 d 数组；起始为 0
    return fa[x]=root;  // 路径压缩
}
void merge(int x,int y) {
    // 由于不知道并查集的末尾，所以需要一个 size 数组记录集合大小
    x=get(x), y=get(y); fa[x]=y, d[x]=size[y]; size[y]+=size[x];  
}
int main() {
    scanf("%d\n",&t);
    for(i=1;i<=30000;i++) fa[i]=i,size[i]=1;
    while(t--) {
        char ch=getchar();
        scanf("%d %d\n",&i,&j);
        if (ch=='M') merge(i,j);
        else if (get(i)==get(j)) cout<<abs(d[i]-d[j])-1;
        else cout<<"-1";
        cout<<endl;
    }
    return 0;
}
```

### acwing 239 奇偶游戏

题意：有一个由 0 和 1 组成的长度为 N 的序列 S。给定 M 个问题，每个问题指定区间 `S[l, r]` 中有奇数个 1 或偶数个 1。求第一个出现矛盾的位置。

思路：

如果用 `sum` 表示 S 的前缀和，那么如果 `S[l, r]` 有偶数个 1，则等价于 `sum[l-1]` 和 `sum[r]` 的奇偶性相同。如果 `S[l, r]` 有奇数个 1，则等价于 `sum[l-1]` 和 `sum[r]` 的奇偶性不同。

本题的传递关系分为三种：

1. x1 与 x2 奇偶性相同，x2 与 x3 奇偶性相同，则 x1 与 x3 奇偶性相同（等于关系）
2. x1 与 x2 奇偶性相同，x2 与 x3 奇偶性不同，则 x1 与 x3 奇偶性不同
3. x1 与 x2 奇偶性不同，x2 与 x3 奇偶性不同，则 x1 与 x3 奇偶性相同

另外，序列长度远大于问题数，所以需要使用离散化。

```c++
void read_discrete() { // 读入、离散化
	cin >> n >> m;
	for (int i = 1; i <= m; i++) {
		char str[5];
		scanf("%d%d%s", &query[i].l, &query[i].r, str);
		query[i].ans = (str[0] == 'o' ? 1 : 0);
		a[++t] = query[i].l - 1;
		a[++t] = query[i].r;
	}
	sort(a + 1, a + t + 1);
	n = unique(a + 1, a + t + 1) - a - 1;
}
```

对于每个问题，设在离散化后 `l-1` 和 `r` 的值分别为 x 和 y，设 ans 表示该问题的奇偶性。

#### 1. 边带权

发现本题的传递关系可以用异或的方式表示。设边权为 `d[x]`，初始值为 0：

1. 若 `d[x]=0` 则说明 `fa[x] <- x` 的奇偶性相同。
2. 若 `d[x]=1` 则说明 `fa[x] <- x` 的奇偶性不同。

先检查 x 和 y 是否在同一个集合内（奇偶关系是否已知）。若在一个集合内（get 执行完边权就更新了），`d[x]^d[y]` 即为区间的奇偶性。若这个值不等于 ans 则说明出现矛盾。

若不在同一个集合内，则合并两个集合。首先已经通过 get 拿到了 x 和 y 的根节点，并更新完边权。此时肯定不会有矛盾，令这句话是真的，则 `d[x] ^ d[x->y] ^ d[y] = ans`，即合并两集合并更新边权 `d[x->y] = d[x] ^ d[y] ^ ans`。

```c++
int get(int x) {
	if (x == fa[x]) return x;
	int root = get(fa[x]);
	d[x] ^= d[fa[x]];
	return fa[x] = root;
}
int main() {
	read_discrete();
	for (int i = 1; i <= n; i++) fa[i] = i;
	for (int i = 1; i <= m; i++) {
		// 求出l-1和r离散化之后的值
		int x = lower_bound(a + 1, a + n + 1, query[i].l - 1) - a;
		int y = lower_bound(a + 1, a + n + 1, query[i].r) - a;
		// 执行get函数，得到树根，并进行路径压缩
		int p = get(x), q = get(y);
		if (p == q)  // 已经在同一集合内
			if ((d[x] ^ d[y]) != query[i].ans) { // 矛盾，输出
				cout << i - 1 << endl; return 0;
			}
		else { // 不在同一集合，合并
			fa[p] = q; d[p] = d[x] ^ d[y] ^ query[i].ans;
		}
	}
	cout << m << endl; // 没有矛盾
}
```

#### 2. 扩展域

把每个变量 x 拆成两个节点 `x_odd` （`sum[x]` 是偶数）和 `x_even`（`sum[x]` 是奇数）可以把这两个节点称为 x 的偶数域和奇数域。

1. 若 ans 为 0，则合并 `x_odd->y_odd` 和 `x_even->y_even`，这表示 x 为奇数和 y 为奇数可以相互推出，x 为偶数和 y 为偶数可以相互推出。
2. 若 ans 为 1，则合并 `x_even->y_odd` 和 `x_odd->y_even`，这表示 x 为奇数和 y 为偶数可以相互推出，x 为偶数和 y 为奇数可以相互推出。

实际上，这种做法相当于在无向图上维护节点之间的联通情况，只是扩展了多个域来应对多种传递关系。

在处理每个问题的时候先检查是否与 ans 矛盾。若 x 和 y 对应的 `x_odd` 和 `y_odd` 在同一个集合内，则说明 x 和 y 已知奇偶性相同。若 x 和 y 对应的 `x_odd` 和 `y_even` 在同一个集合内，则说明 x 和 y 已知奇偶性不同。

```c++
int get(int x) {
	if (x == fa[x]) return x;
	return fa[x] = get(fa[x]);
}
int main() {
	read_discrete();
	for (int i = 1; i <= 2 * n; i++) fa[i] = i;
	for (int i = 1; i <= m; i++) {
		// 求出l-1和r离散化之后的值
		int x = lower_bound(a + 1, a + n + 1, query[i].l - 1) - a;
		int y = lower_bound(a + 1, a + n + 1, query[i].r) - a;
		int x_odd = x, x_even = x + n;
		int y_odd = y, y_even = y + n;
		if (query[i].ans == 0) { // 回答奇偶性相同
			if (get(x_odd) == get(y_even)) { // 与已知情况矛盾
				cout << i - 1 << endl; return 0;
			}
			fa[get(x_odd)] = get(y_odd);  // 合并
			fa[get(x_even)] = get(y_even);
		}
		else { // 回答奇偶性不同
			if (get(x_odd) == get(y_odd)) { // 与已知情况矛盾
				cout << i - 1 << endl; return 0;
			}
			fa[get(x_odd)] = get(y_even);  // 合并
			fa[get(x_even)] = get(y_odd);
		}
	}
	cout << m << endl; return 0;// 没有矛盾
}
```

### acwing 240 食物链

动物王国中有三类动物 A,B,C，这三类动物的食物链构成了有趣的环形。A 吃 B，B 吃 C，C 吃 A。

现有 N 个动物，以 1∼N 编号。每个动物都是 A,B,C 中的一种，但是我们并不知道它到底是哪一种。

给两个说法：X 和 Y 是同类或 X 吃 Y。判断有几次当前的话与前面的某些真的话冲突。

#### 思路 1. 边带权

```c++
// @sunznx：https://www.acwing.com/solution/content/6109/
// 设 d[x] % 3 为 x -> parent[x] 的边权，其中 0 则 x 和 parent[x] 同类；
// 1 则 x 吃 parent[x]，2 则 parent[x] 吃 x。
void init() { for (int i = 0; i <= n; i++) parent[i] = i, d[i] = 0; }

int find(int x) {
	if (x == parent[x]) return x;
	int root = get(parent[x]);
	d[x] += d[parent[x]];
	return parent[x] = root;
}

bool D1(int x, int y) {
    int p1 = find(x), p2 = find(y);
    if (p1 == p2) return d[x] % M == d[y] % M;  // 在一个集合内
    // x -> ... -> p1, y -> ... -> p2
    // x 和 y 的关系为 x -> ... -> p1 -> p2 -> ... -> y
    // = d[x] - d[p2 -> p1] - d[y] = 0
    parent[p2] = p1; d[p2] = ((d[x] - d[y]) + M) % M;
    return true;
}

bool D2(int x, int y) {
    int p1 = find(x), p2 = find(y);
    if (p1 == p2) return d[x] % M == (d[y]+1) % M;
    // 同上 = d[x] - d[p2 -> p1] - d[y] = 1
    parent[p2] = p1; d[p2] = ((d[x]-d[y]-1) + M) % M;
    return true;
}

int main(void) {
    int res = 0; cin >> n >> k; init();
    while (k--) {
        cin >> D >> x >> y;
        if (x > n || y > n) res += 1;
        else if (D == 1 && D1(x, y) == false) res += 1;
        else if (D == 2 && D2(x, y) == false) res += 1;
    }
    cout << res << endl; return 0;
}
```

#### 思路 2. 扩展域

```c++
// @目目目：https://www.acwing.com/solution/content/113385/
int find(int x) { /*...*/ }

int main() {
    cin >> n >> m; for (int i = 1; i < M; i++) p[i] = i;
    while (m--) {
        int d, a, b; scanf("%d%d%d", &d, &a, &b);
        if (a > n || b > n) { res ++; continue; }
        if (a == b) { if (d == 2) res ++; continue; }
        if (d == 1) {
            // 如果 a 吃 b 或者 b 吃 a ，则 a 与 b 是同类是假话
            if (find(a) == find(b + N) || find(a + N) == find(b)) 
                { res++; continue; }

            p[find(a)] = find(b); p[find(a + N)] = find(b + N);
            p[find(a + N * 2)] = find(b + N * 2);
        }
        else {
            // 如果 b 吃 a 或者 a 与 b 是同类 ，则 a 吃 b 是假话
            if (find(a + N) == find(b) || find(a) == find(b))
                { res++; continue; }

            p[find(a)] = find(b + N); p[find(a + N)] = find(b + N * 2);
            p[find(a + N * 2)] = find(b);
        }
    }
    cout << res; return 0;
}
```

## 扩展

### luogu P3183 食物链

题目：给 n 个物种和 m 个能量流动关系，求其中完整的食物链条数。其中不会有环，单独的一种孤立生物不算食物链。

思路：只是名字叫食物链，和并查集没什么关系。这题拓扑排序即可（更新入度时累加方案数）。

```c++
int toposort() {
	queue <int> q; int ans=0;
	for(int i=1; i<=n; i++) // 单个点不算方案
	    if(!rd[i] && e[i].size()) q.push(i), f[i]=1; 
	while(!q.empty()) {
		int x=q.front(); q.pop();
		if(!e[x].size()) ans+=f[x];
		for(auto t : e[x]) {
			f[t]+=f[x], rd[t]--; // f来统计方案
			if(!rd[t]) q.push(t);
		}
	}
	return ans;
}
```

### UVA 11987 Almost Union-Find

题目：有 n 个元素，要求支持三种操作：合并两个元素的集合，把元素移动到另一个元素的集合，查询集合元素个数及元素之和。操作数量小于 1e5。

思路 [@Mr_think](https://www.luogu.com.cn/article/sbawem6r)：操作一和操作三都可以用并查集实现，难点在于第二个操作。容易想到一种错误实现方式，即把需要移动的元素 `x` 的 `fa[x]` 直接设为另一个元素集合的根节点。错误原因是 `x` 可能还有子节点。

如果 `x` 是叶子节点，就可以直接修改 `fa[x]`。实际上，使用虚点可以保证 `x` 在叶子上。

![虚点](https://cdn.luogu.com.cn/upload/image_hosting/gvw2eccx.png)

```c++
int find(int x) { /*...*/ }
int main(){
	while(scanf("%d%d",&n,&m)!=EOF){
		for(int i=1;i<=n;i++) fa[i]=i+n;  // i+n 即为虚点
		for(int i=n+1;i<=n+n;i++)
			fa[i]=i,sz[i]=1,sum[i]=i-n;  // 虚点的父节点设为自身
		
		for(int i=1;i<=m;i++){
			scanf("%d",&opt);
			if(opt==1){  // 合并操作与无虚点相同
				scanf("%d%d",&p,&q);
				int u=find(p),v=find(q);
				if(u==v)continue;
				fa[u]=v;
				sz[v]+=sz[u];
				sum[v]+=sum[u]; 
			}else if(opt==2){  // 移动操作更改父节点的记录
				scanf("%d%d",&p,&q);
				int u=find(p),v=find(q);
				if(u==v)continue;
				fa[p]=v;  // v 也是虚点
				sz[u]--;sz[v]++;
				sum[u]-=p;sum[v]+=p;
			}else{
				scanf("%d",&p);
				printf("%d %lld\n",sz[find(p)],sum[find(p)]);
			}
		}
	}
	return 0;
}
```

类似题目：

[SP5150 Junk-Mail Filter](https://www.luogu.com.cn/problem/SP5150)：维护合并和删除操作，记录最后还剩多少个集合。