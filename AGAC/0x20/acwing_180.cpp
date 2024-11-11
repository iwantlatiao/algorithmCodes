#include <iostream>
#include <cstring>
using namespace std;

const int N = 16;

int n;
int q[N];     // 书的顺序
int w[5][N];  // 恢复现场

int f() {
    int cnt = 0;
    for (int i = 0; i + 1 < n; i++)
        if (q[i + 1] - q[i] != 1) cnt += 1;
    return (cnt + 2) / 3;
}

bool dfs(int d, int maxd) {
    if (d + f() > maxd) return false;  // 剪枝
    if (f() == 0) return true;         // 顺序正确

    // 用 x 表示书本 x [x x x x] x () x () x ()
    // 遍历顺序 长度 len -> 左端点 i -> 移动到位置 k 后
    for (int len = 1; len <= n; len++)
        for (int i = 0; i + len - 1 < n; i++) {
            int j = i + len - 1, x, y;
            for (int k = j + 1; k < n; k++) {
                memcpy(w[d], q, sizeof q);
                // 将方括号之后圆括号之前的部分拷贝到左方括号后
                for (x = j + 1, y = i; x <= k; x++, y++) q[y] = w[d][x];
                // 将方括号内继续拷贝到后面
                for (x = i; x <= j; x++, y++) q[y] = w[d][x];
                if (dfs(d + 1, maxd)) return true;
                memcpy(q, w[d], sizeof q);
            }
        }
    
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    int T;
    cin >> T;
    while (T--) {
        cin >> n;
        for (int i = 0; i < n; i++) cin >> q[i];
        int depth = 0;  // 最大操作次数
        while (depth < 5 && !dfs(0, depth)) depth += 1;
        if (depth == 5) cout << "5 or more" << endl;
        else cout << depth << endl;
    }
}