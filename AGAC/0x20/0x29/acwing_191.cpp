#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

const int N = 366, M = 4, T = 7, D = 9;
const int dx[D] = {0, 0, 1, 0, -1, 0, 2, 0, -2};
const int dy[D] = {0, 1, 0, -1, 0, 2, 0, -2, 0};
int g[N][M][M];  // day, x, y
bool vis[N][M][M][T][T][T][T];
int n;

struct Node {
    int d, x, y, s0, s1, s2, s3;
};

int bfs() {
    if (g[1][1][1] || g[1][1][2] || g[1][2][1] || g[1][2][2]) return 0;

    memset(vis, false, sizeof vis);
    queue<Node> q;
    q.push(Node{1, 1, 1, 1, 1, 1, 1});
    vis[1][1][1][1][1][1][1] = true;

    while (q.size()) {
        auto t = q.front();
        q.pop();
        if (t.d == n) return 1;

        for (int i = 0; i < D; i++) {
            int x = t.x + dx[i], y = t.y + dy[i];
            if (x < 0 || x >= M - 1 || y < 0 || y >= M - 1) continue;

            // 明天下雨的格子没有过节
            auto& state = g[t.d + 1];
            if (state[x][y] || state[x][y + 1] || state[x + 1][y] ||
                state[x + 1][y + 1])
                continue;

            // 四个角的格子未下雨天数不超过七天
            int s0 = t.s0, s1 = t.s1, s2 = t.s2, s3 = t.s3;
            if (x == 0 && y == 0) s0 = 0;
            else if (++s0 >= 7) continue;
            if (x == 0 && y == 2) s1 = 0;
            else if (++s1 >= 7) continue;
            if (x == 2 && y == 0) s2 = 0;
            else if (++s2 >= 7) continue;
            if (x == 2 && y == 2) s3 = 0;
            else if (++s3 >= 7) continue;

            if (vis[t.d + 1][x][y][s0][s1][s2][s3]) continue;
            vis[t.d + 1][x][y][s0][s1][s2][s3] = true;
            q.push(Node {t.d + 1, x, y, s0, s1, s2, s3});
        }
    }

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    int t = 0;
    while (cin >> n, n > 0) {
        for (int i = 1; i <= n; i++)
            for (int j = 0; j < M; j++)
                for (int k = 0; k < M; k++) cin >> g[i][j][k];

        cout << bfs() << endl;
    }

    return 0;
}