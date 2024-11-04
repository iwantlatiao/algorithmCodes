#include <iostream>
#include <cstring>
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

bool bfs_man(PII start, PII end, PII box, vector<int> &seq) {
    return false;
}

// 对箱子做 bfs，如果能到达终点，end 保存最短到达的终点位置和方向
bool bfs_box(PII start, PII box, Point &end) {
    memset(st, false, sizeof st);
    queue<Point> q;
    
    // 起始状态插入队列
    for (int i = 0; i < 4; i++) {
        int a = box.first + dx[i], b = box.second + dy[i];  // 人要走到的位置
        int c = box.first - dx[i], d = box.second - dy[i];  // 箱子推到的位置
        if (!check(a, b) || !check(c, d)) continue;

        vector<int> seq;
        int len = bfs_man(start, PII {a, b}, box, seq);
    }
    
    return false;
}

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
        if (!bfs_box(start, box, end)) res = "Impossible.";
        else {
            //
        }
    }

    return 0;
}