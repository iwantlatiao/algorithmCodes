#include <iostream>
#include <cstring>
using namespace std;

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
    memset(st, 0, sizeof st);
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) cin >> g[i];
    }
    return 0;
}