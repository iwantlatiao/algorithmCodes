#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;

typedef pair<int, int> PII;
const int N = 1005, M = 20010, INF = 0x3f3f3f3f;
int h[N], rh[N], to[M], w[M], ne[M], tot;
int n, m, s, t, k;
int f[N], st[N], cnt[N];

struct Node {
    int s, v, d;  // s 估价函数 v 点序号 d 当前距离
    bool operator<(const Node& t) const { return s > t.s; }
};

void add(int h[], int a, int b, int c) {
    to[++tot] = b, w[tot] = c, ne[tot] = h[a], h[a] = tot;
}

// 对反图求最短路，目的是得到正图的估价函数 f
void dijkstra() {
    memset(f, 0x3f, sizeof f);
    f[t] = 0;

    priority_queue<PII> pq;  // (dist, index)
    pq.push(PII{0, t});
    while (!pq.empty()) {
        PII u = pq.top();
        pq.pop();

        if (st[u.second]) continue;
        st[u.second] = true;

        int v;
        for (int i = rh[u.second]; i != 0; i = ne[i]) {
            v = to[i];
            if (f[v] > f[u.second] + w[i]) {
                f[v] = f[u.second] + w[i];
                pq.push(PII{-f[v], v});
            }
        }
    }
}

int astar() {
    priority_queue<Node> pq;
    pq.push(Node{f[s], s, 0});
    while (!pq.empty()) {
        Node u = pq.top();
        pq.pop();

        cnt[u.v] += 1;
        if (cnt[t] == k) return u.d;

        int v, d;
        for (int i = h[u.v]; i != 0; i = ne[i]) {
            v = to[i], d = u.d + w[i];
            // 由于求 k 短路，已经经过这个点 k 次就已经拿到了这个点
            // 的 k 短路，不需要求更大的路径。并且由于估价函数等于真实距离，
            // 保证每次拿的都是除了已经取出点的最短路。
            if (cnt[v] < k) pq.push(Node{d + f[v], v, d});
        }
    }

    return -1;
}

int main() {
    scanf("%d%d", &n, &m);

    int a, b, c;
    for (int i = 0; i < m; i++) {
        scanf("%d%d%d", &a, &b, &c);
        add(h, a, b, c), add(rh, b, a, c);
    }

    scanf("%d%d%d", &s, &t, &k);
    if (s == t) k += 1;
    dijkstra();
    printf("%d", astar());
}