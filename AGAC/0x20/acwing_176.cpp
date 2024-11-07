#include <queue>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int N = 1005;
const int M = 20005;
const int C = 105;
const int INF = 0x3f3f3f3f;

int n, m, q;
int p[N];                          // 每个点的油价
int h[N], w[M], e[M], ne[M], idx;  // 存图
int dist[N][C];                    // 存最短路
bool st[N][C];

struct Point {
    int d, u, c;  // d 到这个点花的油钱 u 点的编号 c 当前油量
    // pq 默认是大根堆，把小于号的逻辑反过来变成小根堆
    bool operator<(const Point& t) const { return d > t.d; }
};

void add(int a, int b, int c) {
    e[++idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx;
}

int dijkstra(int start, int end, int c) {
    memset(st, false, sizeof st);
    memset(dist, 0x3f, sizeof dist);

    priority_queue<Point> pq;
    pq.push(Point{0, start, 0});
    dist[start][0] = 0;

    while(!pq.empty()) {
        Point t = pq.top();
        pq.pop();

        if (t.u == end) return t.d;
        if (st[t.u][t.c]) continue;
        st[t.u][t.c] = true;

        // 1. 油箱没满，且加油后油钱更少，可以加油
        if (t.c < c && t.d + p[t.u] < dist[t.u][t.c + 1]) {
            dist[t.u][t.c + 1] = t.d + p[t.u];
            pq.push(Point {dist[t.u][t.c + 1], t.u, t.c + 1});
        }

        // 2. 可以到下一个点 e[i]
        for (int i = h[t.u]; i != 0; i = ne[i]) {
            if (t.c >= w[i] && t.d < dist[e[i]][t.c - w[i]]){
                dist[e[i]][t.c - w[i]] = t.d;
                pq.push(Point {dist[e[i]][t.c - w[i]], e[i], t.c - w[i]});
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> p[i];

    int a, b, c;
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        add(a, b, c), add(b, a, c);
    }

    int start, end, ans;
    cin >> q;
    while (q--) {
        cin >> c >> start >> end;
        ans = dijkstra(start, end, c);
        if (ans == -1) cout << "impossible" << endl;
        else cout << ans << endl;
    }

    return 0;
}