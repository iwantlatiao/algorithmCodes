#include <iostream>
using namespace std;

const int MAXN = 7;
int p[10] = {0, 1, 3, 9, 27, 81, 243, 729};
int g[730][730];
int n;

// 
void solve(int depth, int x, int y) {
    if (depth == 1) { g[x][y] = 1; return; }
    int length = p[depth - 1];  // 上一层的长度

    solve(depth - 1, x, y);  // 左上
    solve(depth - 1, x, (length << 1) + y);  // 右上
    solve(depth - 1, length + x, length + y);  // 中间
    solve(depth - 1, (length << 1) + x, y);  // 左下
    solve(depth - 1, (length << 1) + x, (length << 1) + y);  // 右下
}

int main() {
    solve(MAXN, 0, 0);
    cin >> n;
    while (n != -1) {
        for (int i=0; i<p[n]; i++) {
            for (int j=0; j<p[n]; j++) {
                if (g[i][j] == 0) cout << " ";
                else cout << "X";
            }
            cout << endl;
        }
        cout << "-" << endl;
        cin >> n;
    }

    return 0;
}