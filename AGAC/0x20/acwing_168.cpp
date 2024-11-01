#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

const int M = 25;
const int N = 10005;
const int INF = 0x3f3f3f3f;

int n, m;
int minv[M], mins[M];       // 打表
int H[M], R[M], res = INF;  // 答案

// 当前层次 u 当前体积和 v 当前面积和 s
void dfs(int u, int v, int s) {
    if (v + minv[u] > n) return;                    // 3. 体积剪枝
    if (s + 2 * (n - v) / R[u + 1] >= res) return;  // 4. 关系的剪枝
    if (s + mins[u] >= res) return;                 // 5. 表面积的剪枝

    if (u == 0) {
        if (v == n) res = s;
        return;
    }

    int rmin = u, rmax = min(R[u + 1] - 1, (int)sqrt((n - minv[u - 1] - v) / u));
    for (int r = rmax; r >= rmin; r--) {
        int hmin = u, hmax = min(H[u + 1] - 1, (n - minv[u - 1] - v) / r / r);
        for (int h = hmax; h >= hmin; h--) {
            H[u] = h, R[u] = r;
            int t = u == m ? r * r : 0;  // 最底层加上表面面积
            dfs(u - 1, v + r * r * h, s + 2 * r * h + t);
        }
    }
}

int main() {
    cin >> n >> m;

    // 从上往下数, s += 2r * h, v += h * r^2
    for (int i = 1; i <= m; i++) {
        mins[i] = mins[i - 1] + 2 * i * i;
        minv[i] = minv[i - 1] + i * i * i;
    }

    H[m + 1] = R[m + 1] = INF;

    dfs(m, 0, 0);

    if (res == INF) res = 0;
    cout << res << endl;

    return 0;
}