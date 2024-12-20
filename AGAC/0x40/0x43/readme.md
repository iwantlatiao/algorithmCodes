# 0x43 线段树

[@lfool 线段树详解](https://leetcode.cn/problems/range-module/solutions/1612955/by-lfool-eo50/)

[OI wiki 对线段树的介绍](https://oi-wiki.org/ds/seg/)

## 基本概念

线段树是算法竞赛中常用的用来维护 **区间信息** 的数据结构。与按照二的次幂进行区间划分的树状数组相比，线段树是一种更加通用的结构。

线段树可以在 $O(\log N)$ 的时间复杂度内实现单点修改、区间修改、区间查询（区间求和、最值、GCD）等操作。

线段树具有以下几个性质：

1. 线段树的每个节点都代表一个区间。
2. 线段树具有唯一的根节点，代表整个统计区间。
3. 线段树的叶节点是长度为 1 的元区间。
4. 对于每个内部节点 `[l,r]` ，它的左子节点是 `[l,mid]` ，右子节点是 `[mid+1,r]` ，其中 `mid=(l+r)>>1` 。

可以发现，除了树的最后一层，整棵线段树是完全二叉树，树的深度为 $O(\log N)$ ，因此可以按照与二叉堆类似的 “父子二倍” 编号方法：

1. 根节点编号为 1
2. 编号为 `x` 的节点，左子节点的编号为 `x<<1` ，右子节点的编号为 `(x<<1)+1`

这样就可以用一个简单的 `struct` 来保存线段树了。由于最后一层不连续，所以用于保存线段树的数组长度要开到 `4*N` 才能保证不会越界。

### 建树

线段树的二叉树结构可以很方便地从下往上传递信息。建树时采用递归建树，如果根节点管辖的区间长度已经是 1，则可以直接根据相应位置的值初始化该节点。否则我们将该区间从中点处分割为两个子区间，分别进入左右子节点递归建树，最后合并两个子节点的信息。

```c++
struct SegmentTree {
    int l, r;
    int dat;
} t[SIZE * 4]; // struct数组存储线段树

// 以维护区间最大值为例建树
// 当前节点 t[p] 维护区间为 [1,n]
void build(int p, int l, int r) {
    t[p].l = l, t[p].r = r; // 节点p代表区间[l,r]
    if (l == r) { t[p].dat = a[l]; return; } // 叶节点
    int mid = (l + r) / 2; // 折半
    build(p*2, l, mid); // 左子节点[l,mid]，编号p*2
    build(p*2+1, mid+1, r); // 右子节点[mid+1,r]，编号p*2+1
    t[p].dat = max(t[p*2].dat, t[p*2+1].dat); // 从下往上传递信息
}
build(1, 1, n); // 调用入口
```

### 单点修改

修改是从下往上的。需要先从根节点出发，找到目标叶子节点，然后再从下往上更新所有父节点信息。

```c++
// 当前节点为 p，目标把 A[x] 修改为 v
void change(int p, int x, int v) {
	if (t[p].l == t[p].r) { t[p].dat = v; return; } // 找到叶节点
	int mid = (t[p].l + t[p].r) / 2;
	if (x <= mid) change(p*2, x, v); // x属于左半区间
	else change(p*2+1, x, v); // x属于右半区间
	t[p].dat = max(t[p*2].dat, t[p*2+1].dat); // 从下往上更新信息
}
change(1, x, v); // 调用入口，都是从根节点开始往下找再往上更新
```

### 区间查询

对区间 `[l,r]` 的查询可以分为三种情况：

1. 区间 `[l,r]` 完全覆盖了当前节点的区间，则当前节点是候选答案，立即回溯。
2. 左子节点与 `[l,r]` 有重叠部分，则递归访问左子节点
3. 右子节点与 `[l,r]` 有重叠部分，则递归访问右子节点

```c++
int ask(int p, int l, int r) {
	if (l <= t[p].l && r >= t[p].r) return t[p].dat; // 完全包含，直接返回
	int mid = (t[p].l + t[p].r) / 2;
	int val = 0;
	if (l <= mid) val = max(val, ask(p*2, l, r)); // 左子节点有重叠
	if (r > mid) val = max(val, ask(p*2+1, l, r)); // 右子节点有重叠
	return val;
}
cout << ask(1, l, r) << endl; // 调用入口
```

该查询过程会把询问区间 [l,r] 在线段树上分成 $O(\log N)$ 个节点。

### 简单应用

#### acwing 245 你能回答这些问题吗

题意：要求维护长度为 `N` 的数列 `A` ，支持两种指令：修改 `A[x]=y` ； 查询区间 `[l,r]` 的最大子段和。

[@Payxtl](https://www.acwing.com/solution/content/110854/) 思路：

考虑维护区间 `[l,r]` 的最大子段和需要维护哪些信息：

1. 首先需要一个 `tmax` 存储当前区间 `[l,r]` 的最大子段和。
2. `tmax` 可以是左子节点的最大连续子段和，可以是右子节点的最大连续子段和，也可以是跨越两个子节点的最大连续子段和。在跨越两个子节点时，需要从左子节点的最大后缀和 `rmax` 加右子节点的最大前缀和 `lmax` 转移而来。
3. `lmax` 可以是左子节点的最大前缀和，也可以是左子节点的总和加右子节点的最大前缀和； `rmax` 同理。所以还需要维护节点元素和 `sum` 。

所以需要维护四个信息，即节点元素和、最大前缀和、最大后缀和、最大子段和。

```c++
struct node {
    int l, r;
    int sum, lmax, rmax, tmax;
} tr[N * 4];
```

从下往上传递四个信息。

```c++
void pushup(node &u, node &l, node &r) {
    u.sum = l.sum + r.sum;
    u.lmax = max(l.lmax, l.sum + r.lmax);
    u.rmax = max(r.rmax, r.sum + l.rmax);
    u.tmax = max(l.rmax + r.lmax, max(l.tmax, r.tmax));
}

void pushup(int u) {
    pushup(tr[u], tr[u << 1], tr[u << 1 | 1]);
}
```

建树操作，找到叶子节点的赋值给到四个对应信息，然后从下往上传递。

```c++
void build(int u, int l, int r) {
    if (l == r) tr[u] = {l, r, w[r], w[r], w[r], w[r]}; // 找到叶子节点
    else {
        tr[u] = {l, r};                 // 设当前节点区间为[l, r]
        int mid = l + r >> 1;
        build(u << 1, l, mid);          // 建立左子树
        build(u << 1 | 1, mid + 1, r);  // 建立右子树
        pushup(u);                      // 修改父节点
    }
}
```

修改操作，找到叶子节点修改信息，然后从下往上传递。

```c++
void modify(int u, int x, int v) {
    if (tr[u].l == x && tr[u].r == x) tr[u] = {x, x, v, v, v, v};   // 找到了
    else {
        int mid = tr[u].l + tr[u].r >> 1;
        if (x <= mid) modify(u << 1, x, v); // x位于当前区间的左半子区间
        else modify(u << 1 | 1, x, v);      // x位于当前区间的右半子区间
        pushup(u);                          // 修改父节点的相关信息
    }
}
```

查询操作会遇到四种情况，比模板多一种情况：

1. 区间 `[l,r]` 完全覆盖了当前节点的区间，则返回当前节点的信息。
2. 只有左子节点与 `[l,r]` 有重叠部分，则递归访问左子节点
3. 只有右子节点与 `[l,r]` 有重叠部分，则递归访问右子节点
4. 左右节点都与与 `[l,r]` 有重叠部分，则递归访问左子节点和右子节点，然后合并这两个子节点的信息，得到一个新节点，将新节点向上返回

```c++
node query(int u, int l, int r) {   // 从节点u开始，查找区间[l, r]的信息
    // 1. 包含在区间内
    //      Tl-----Tr
    //   L-------------R  
    if (tr[u].l >= l && tr[u].r <= r) return tr[u];

    int mid = tr[u].l + tr[u].r >> 1;

    // 2. 在当前的左半区间
    //    Tl-----m-----Tr
    //      L---R
    if (r <= mid) return query(u << 1, l, r);

    // 3. 在当前的右半区间
    //    Tl-----m-----Tr
    //              L-----R
    else if (l > mid) return query(u << 1 | 1, l, r);

    // 4. 两边都有，都查询
    //     Tl----m----Tr
    //        L-----R 
    else {
        auto left = query(u << 1, l, r);
        auto right = query(u << 1 | 1, l, r);
        node res;
        // 合并答案
        pushup(res, left, right);
        return res;
    }
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) cin >> w[i];

    build(1, 1, n);
    int op, x, y;
    while (m--) {
        cin >> op >> x >> y;
        if (op == 1) {
            if (x > y) swap(x, y);
            cout << query(1, x, y).tmax << endl;
        } else {
            modify(1, x, y);
        }
    }

    return 0;
}
```

#### acwing 246 区间 GCD

题意：要求维护长度为 `N` 的数列 `A` ，支持两种指令：修改 `A[l~r]=y` ； 查询区间 `[l,r]` 的 GCD 。

[@bigstone](https://www.acwing.com/solution/content/42739/)、[@这个显卡不太冷](https://www.acwing.com/solution/content/1047/) 思路：

先考虑要维护哪些信息。首先肯定需要维护区间的 GCD。对于 `pushup` 操作中维护 GCD 一项，可以把两个子节点的 GCD 再一起求一次 GCD 。

最大公约数不仅可以用辗转相除法，也可以用更相减损术，即 `gcd(x, y) = gcd(x, y-x)` 。对于任意多整数也成立，即 `gcd(x, y, z) = gcd(x, y-x, z-y)` 。所以对于区间修改操作，受到更相减损术的启发，可以在原始数列 `A` 之外，维护一个差分序列 `B[i] = A[i] - A[i-1]` 。需要求 `gcd(a1, a2, a3, ..., an)` ，也就是求 `gcd(a1, a2-a1, a3-a2, ..., an-a(n-1))` ，即 `gcd(a1, gcd(b2, b3, ..., bn))` 。

这样就确定了我们需要维护的两个信息：GCD 和 差分。

```c++
struct Node {
    int l, r;
    LL sum, d;
}tr[4 * N];

void pushup(Node &u, Node &l, Node &r) { //由子区间信息更新父区间信息
    u.sum = l.sum + r.sum;
    u.d = gcd(l.d, r.d);
}

void pushup(int u) {
    pushup(tr[u], tr[u << 1], tr[u << 1 | 1]);
}

void build(int u, int l, int r) {        //建树
    tr[u].l = l, tr[u].r = r;
    if ( l == r ) 
        tr[u].d = w[l] - w[l - 1], tr[u].sum = w[l] - w[l - 1];
    else {
        int mid = l + r >> 1;
        build(u << 1, l, mid);
        build(u << 1 | 1, mid + 1, r);
        pushup(u);
    }
}

void modify(int u, int x, LL v) {        //修改
    if ( tr[u]. r == x && tr[u].l == x ) 
        tr[u].d = tr[u].sum + v, tr[u].sum += v;    
    else {
        int mid = tr[u].l + tr[u].r >> 1;
        if ( mid >= x ) modify(u << 1, x, v);
        else modify(u << 1 | 1, x, v);
        pushup(u);
    }
}

Node query(int u, int l, int r) {
    if ( tr[u].l >= l && tr[u].r <= r ) return tr[u];
    else {
        int mid = tr[u].l + tr[u].r >> 1;
        if ( mid >= r ) return query(u << 1, l, r);
        else if ( mid < l ) return query(u << 1 | 1, l, r);
        else {
            Node left = query(u << 1, l, r);        //如果当前访问区间的子区间横跨询问区间
            Node right = query(u << 1 | 1, l, r);   //则递归两个子区间
            Node res;                               //res相当于left和right的父区间
            pushup(res, left, right);               //相当于求right和left区间合并后的结果
            return res;
        }
    }
}

int main() {
    cin >> n >> m;
    for ( int i = 1; i <= n; i ++ ) scanf("%lld", &w[i]);
    build(1, 1, n);
    int l, r; LL d; char op[2];
    while ( m -- ) {
        scanf("%s%d%d", op, &l, &r);
        if ( * op == 'C' ) {
            scanf("%lld", &d);
            modify(1, l, d);                            //差分操作l处加d，r+1处减d
            if ( r + 1 <= n ) modify(1, r + 1, -d);     //注意判断r+1与n的关系
        }
        else {
            Node left = query(1, 1, l);                 //gcd(a[l])
            Node right = {0, 0, 0, 0};                  //若l+1>r
            if ( l + 1 <= r ) right = query(1, l + 1, r);   //gcd(b[l+1]~b[r])
            printf("%lld\n", abs(gcd(left.sum, right.d)));  //输出正数
        }
    }
    return 0;
}
```

## 区间修改的延迟标记

在线段树的区间查询中，若查询区间完全覆盖当前节点区间，可以将当前节点上的信息直接返回。可以证明，被询问区间在线段树上会分成 $O(\log N)$ 个小区间。但在区间修改中，如果修改区间完全覆盖当前节点区间，那么以该节点为根的所有节点的信息都将发生变化。如果逐一进行修改，就会达到 $O(N)$ 的复杂度。

如果我们对完全覆盖节点的所有子节点逐一修改，且后续查询没有经过该节点，那么这些修改对答案是没有任何作用的。所以考虑给每个节点增加一个延迟标记，表示 `该节点曾经被修改，但其子节点暂未被更新` 。

延迟标记的作用是，除了在修改指令直接划分成的 $O(\log N)$ 个节点之外，对任意节点的修改都延迟到 `后续操作到达该节点的父节点` 时再执行。

## 扫描线

## 动态开点和线段树合并