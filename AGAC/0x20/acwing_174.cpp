#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int, int> PII;
const int dx[4] = {1, -1, 0, 0};  // 人对于箱子的位置
const int dy[4] = {0, 0, 1, -1};
const char ops[5] = "nswe";
const int N = 25;
const int INF = 1e9;

int n, m;
char g[N][N];  // 地图
bool st[N][N][4], vis[N][N];
PII dist[N][N][4];          // 存最短距离，first是箱子的距离，second是人的距离
int pre_man[N][N];          // 存人移动的方向，求人的移动路径
vector<int> path[N][N][4];  // 箱子当前位置，人的移动路径

bool check(int x, int y) {
    return x >= 0 && y >= 0 && x < n && y < m && g[x][y] != '#';
}

struct Point {
    int x, y, dir;
} pre[N][N][4];  // 用于求箱子和人的移动路径

int bfs_man(PII start, PII end, PII box, vector<int>& seq) {
    memset(vis, false, sizeof vis);
    memset(pre_man, -1, sizeof pre_man);
    vis[start.first][start.second] = true;
    vis[box.first][box.second] = true;  // 不走箱子的位置

    queue<PII> q;
    q.push(start);
    while (!q.empty()) {
        PII t = q.front();
        q.pop();
        int x = t.first, y = t.second;
        // cout << x << " " << y << " " << endl;

        // 如果人到达 end 点的位置，先求路径，然后返回路径长度
        if (t == end) {
            seq.clear();
            while (~pre_man[x][y]) {
                int dir = pre_man[x][y];
                seq.push_back(dir);
                x += dx[dir], y += dy[dir];
            }
            return seq.size();
        }

        // dx dy 是人对于箱子的位置，题目要求先上下后左右，所以
        // 求下个位置用的是 - dx, - dy
        for (int i = 0; i < 4; i++) {
            int a = x - dx[i], b = y - dy[i];
            if (!check(a, b) || vis[a][b]) continue;

            vis[a][b] = true, pre_man[a][b] = i;
            q.push(PII{a, b});
        }
    }

    return -1;
}

// 对箱子做 bfs，如果能到达终点，end 保存最短到达的终点位置和方向
bool bfs_box(PII start, PII box, Point& end) {
    memset(st, false, sizeof st);
    queue<Point> q;

    // 起始状态插入队列
    for (int i = 0; i < 4; i++) {
        int a = box.first + dx[i], b = box.second + dy[i];  // 人要走到的位置
        int c = box.first - dx[i], d = box.second - dy[i];  // 箱子推到的位置
        if (!check(a, b) || !check(c, d)) continue;

        vector<int> seq;
        int len = bfs_man(start, PII{a, b}, box, seq);
        // cout << len << endl;
        if (len == -1) continue;  // 这个位置人走不到，跳过

        q.push(Point{c, d, i});
        st[c][d][i] = true, path[c][d][i] = seq, dist[c][d][i] = PII{1, len};
        pre[c][d][i] = Point{box.first, box.second, -1};  // 将起点标为 -1
    }

    PII mind = {INF, INF};
    while (!q.empty()) {
        Point t = q.front();
        // cout << t.x << " " << t.y << " " << t.dir << endl;
        q.pop();
        PII nowd = dist[t.x][t.y][t.dir];

        // 这里不能遇到终点就直接返回，因为不能保证人的步数最小。
        if (g[t.x][t.y] == 'T' && nowd < mind) mind = nowd, end = t;

        for (int i = 0; i < 4; i++) {
            int a = t.x + dx[i], b = t.y + dy[i];
            int c = t.x - dx[i], d = t.y - dy[i];
            if (!check(a, b) || !check(c, d)) continue;

            vector<int> seq;
            int len = bfs_man(PII{t.x + dx[t.dir], t.y + dy[t.dir]}, PII{a, b},
                              PII{t.x, t.y}, seq);
            if (len == -1) continue;  // 这个位置人走不到，跳过

            PII newd = {nowd.first + 1, nowd.second + len};
            if (!st[c][d][i]) {
                q.push(Point{c, d, i});
                st[c][d][i] = true, path[c][d][i] = seq, pre[c][d][i] = t,
                dist[c][d][i] = newd;
            }
            // 1. 箱子路程 2. 人路程
            // 实际上箱子的路程是严格递增，所以只可能人路程大于 newd，所以只需要对
            // 人的路径替换，不需要把这个点再加入队列中。
            else if (dist[c][d][i] > newd)
                path[c][d][i] = seq, pre[c][d][i] = t, dist[c][d][i] = newd;
        }
    }

    return mind.first != INF;
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
                if (g[i][j] == 'S') start = PII{i, j};
                else if (g[i][j] == 'B') box = PII{i, j};

        Point end;   // 用 (x, y, dir) 存，便于最后倒着找路径
        string res;  // 记录最终路径答案
        if (!bfs_box(start, box, end)) res = "Impossible.";
        else {
            while (~end.dir) {
                res += ops[end.dir] - 32;  // 'a' - 32 == 'A'
                for (auto u : path[end.x][end.y][end.dir]) res += ops[u];
                end = pre[end.x][end.y][end.dir];
            }
            reverse(res.begin(), res.end());
        }
        cout << res << endl << endl;
    }

    return 0;
}