#include <iostream>
#include <cstring>
using namespace std;

const int N = 10;
const int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};
int n, maxd, g[N][N], st[N][N];
bool color[6];

// 将 (x, y) 及它附近颜色为 c 格子都加入连通块
void flood_fill(int x, int y, int c) {
    st[x][y] = 1;
    for (int i = 0; i < 4; i++) {
        int a = x + dx[i], b = y + dy[i];
        // 超出边界就跳过
        if (a < 0 || a >= n || b < 0 || b >= n) continue;
        // 之前已经和起点变成相同颜色就跳过
        if (st[a][b] == 1) continue;
        // 如果相邻格子颜色也是 c，就继续加入连通块操作
        // 否则，这个格子就是连通块的边界
        if (g[a][b] == c) flood_fill(a, b, c);
        else st[a][b] = 2;
    }
}

// 估价函数，统计不在连通块中的颜色个数
int f() {
    int s = 0;
    memset(color, false, sizeof color);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (st[i][j] != 1 && !color[g[i][j]]) {
                color[g[i][j]] = true;  // 该颜色已统计
                s += 1;
            }
        }
    return s;
}

bool dfs(int u) {
    int eval = f();
    if (u + eval > maxd) return false;
    if (eval == 0) return true;

    int bst[N][N];
    memcpy(bst, st, sizeof st);

    // 枚举下个变的颜色
    for (int c = 0; c < 6; c++) {
        bool ok = false;  // 连通块边界上是否有该颜色
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (st[i][j] == 2 && g[i][j] == c) {
                    ok = true;
                    flood_fill(i, j, c);
                }
        if (ok && dfs(u + 1)) return true;
        memcpy(st, bst, sizeof st);  // 这个方案不行，恢复状态
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    while (cin >> n, n > 0) {
        maxd = 0;
        memset(st, 0, sizeof st);

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) cin >> g[i][j];

        flood_fill(0, 0, g[0][0]);
        while (!dfs(0)) maxd += 1;
        cout << maxd << endl;
    }
    return 0;
}