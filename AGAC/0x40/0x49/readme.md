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
    // read ...
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

int main() {
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