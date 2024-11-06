#include <iostream>
#include <cstring>
#include <deque>
using namespace std;

typedef pair<int, int> PII;

const int N = 505;
// 格点往左上、右上、左下、右下移动的相对坐标
const int dx[4] = {-1, -1, 1, 1}, dy[4] = {-1, 1, 1, -1};
// 格点移动时需要经过的方格的相对坐标
const int ix[4] = {-1, -1, 0, 0}, iy[4] = {-1, 0, 0, -1};
// 左上、右上、左下、右下的方格如果是这样就不需要旋转
const char cs[4] = {'\\', '/', '\\', '/'};
const int INF = 0x3f3f3f3f;

char g[N][N];
bool st[N][N];
int d[N][N];
int n, m;

int bfs() {
    if (((n + m) & 1) == 1)
        return -1;

    memset(st, 0, sizeof st);
    memset(d, 0x3f, sizeof d);

    deque<PII> q;
    q.push_back(PII{0, 0});
    d[0][0] = 0;

    // 为了保证队列单调性, 权值为 0 的边从队头入,
    // 权值为 1 的边从队尾入, 取队头.
    while (!q.empty()) {
        auto t = q.front();
        q.pop_front();

        int x = t.first, y = t.second;
        // cout << x << " " << y << endl;
        if (st[x][y]) continue;
        st[x][y] = true;  // 没有负权边, 一个点不会经过两遍

        for (int i = 0; i < 4; i++) {
            int a = x + dx[i], b = y + dy[i];  // 格点下一步的位置
            int j = x + ix[i], k = y + iy[i];  // 下一步要经过的大格

            if (0 <= a && a <= n && 0 <= b && b <= m) {
                int w = 0;
                if (g[j][k] != cs[i]) w = 1;
                if (d[a][b] > d[x][y] + w) {
                    d[a][b] = d[x][y] + w;
                    if (w == 1) q.push_back(PII{a, b});
                    else q.push_front(PII{a, b});
                }
            }
        }
    }

    if (d[n][m] == INF) return -1;
    return d[n][m];
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        cin >> n >> m;

        for (int i = 0; i < n; i++) cin >> g[i];
        int ans = bfs();
        if (ans == -1) cout << "NO SOLUTION" << endl;
        else cout << ans << endl;
    }
    return 0;
}