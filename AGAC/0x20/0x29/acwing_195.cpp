#include <iostream>
#include <cstring>
using namespace std;

const int target[5][5] = {{1, 1, 1, 1, 1},
                          {-1, 1, 1, 1, 1},
                          {-1, -1, 0, 1, 1},
                          {-1, -1, -1, -1, 1},
                          {-1, -1, -1, -1, -1}};
const int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
const int dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};

int maxd, now[5][5];

int f() {
    int s = 0;
    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            if (target[i][j] != 0 && target[i][j] != now[i][j]) s += 1;
    return s;
}

bool dfs(int nowd, int x, int y, int px, int py) {
    int eval = f();
    if (nowd + eval > maxd) return false;
    if (eval == 0) return true;

    for (int i = 0; i < 8; i++) {
        int tx = x + dx[i], ty = y + dy[i];
        if (tx == px && ty == py) continue;  // 不往回走
        if (tx < 0 || tx >= 5 || ty < 0 || ty >= 5) continue;

        swap(now[tx][ty], now[x][y]);
        if (dfs(nowd + 1, tx, ty, x, y)) return true;
        swap(now[tx][ty], now[x][y]);
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    char c;
    int T;
    cin >> T;
    while (T--) {
        int x, y;
        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++) {
                cin >> c;
                if (c == '1') now[i][j] = 1;
                else if (c == '0') now[i][j] = -1;
                else now[i][j] = 0, x = i, y = j;
            }
        bool found = false;
        for (maxd = 0; maxd <= 15; maxd++)
            if (dfs(0, x, y, -1, -1)) {
                cout << maxd << endl;
                found = true;
                break;
            }
        if (!found) cout << -1 << endl;
    }

    return 0;
}