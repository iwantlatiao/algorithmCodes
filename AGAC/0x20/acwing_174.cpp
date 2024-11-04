#include <iostream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

typedef pair<int, int> PII;
const int dx[4] = {1, -1, 0, 1};
const int dy[4] = {0, 0, 1, -1};
const char ops[5] = "nswe";
const int N = 25;

int n, m;
char g[N][N];  // 地图
bool st[N][N], vis[N][N];
PII dist[N][N][4];  // 存最短距离，first是箱子的距离，second是人的距离
int pre_man[N][N];  // 存人移动的方向，求人的移动路径
vector<int> path[N][N][4];  // 箱子当前位置，人的移动路径

bool check(int x, int y) {
    return x >= 0 && y >= 0 && x < n && y < m && g[x][y] != '#';
}

struct Point {
    int x, y, dir;
} pre[N][N][4];  // 用于求箱子和人的移动路径

int main() {
    int T = 0;
    while (cin >> n >> m && n > 0 && m > 0) {
        cout << "Maze #" << ++T << endl;
        for (int i = 0; i < n; i++) cin >> g[i];  // 读入地图
        
        // 找人和箱子的位置
        PII start, box;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (g[i][j] == 'S') start = PII {i, j};
                else if (g[i][j] == 'B') box = PII {i, j};
        
        Point end;   // 用 (x, y, dir) 存，便于最后倒着找路径
        string res;  // 记录最终路径答案
        
    }

    return 0;
}