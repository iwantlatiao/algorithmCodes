#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef pair<int, int> PII;
const int N = 805;
const int INF = 0x3f3f3f3f;
const int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};

int n, m, t;
bool g[N][N];  // true 能走 false 不能走
int st[N][N];

struct Point {
    int x, y, d;
} boy, girl, ghost[2];

// 是否已经被鬼占领无法走
bool check_ghost(int x, int y, int t) {
    for (int i = 0; i < 2; i++)
        if (abs(ghost[i].x - x) + abs(ghost[i].y - y) <= (t << 1)) return false;
    return true;  // 可以走
}

// 在地图范围内
bool check_map(int x, int y) {
    if (0 <= x && x < n && 0 <= y && y < m && g[x][y]) return true;
    else return false;
}

// 由时间 t 和速度 v 组成，本次搜索不超过 t * v 的点
bool bfs_each(queue<Point>& q, int t, int v) {
    while (!q.empty() && q.front().d < t * v) {
        Point u = q.front();
        q.pop();

        if (!check_ghost(u.x, u.y, t)) continue;  // 当前点已被占领无法拓展
        for (int i = 0; i < 4; i++) {
            int a = u.x + dx[i], b = u.y + dy[i];
            if (check_ghost(a, b, t) && check_map(a, b)) 
                // 还没被遍历过 记录是谁到的
                if (!st[a][b]) {
                    st[a][b] = st[u.x][u.y];
                    q.push(Point {a, b, u.d + 1});
                }
                else if (st[a][b] != st[u.x][u.y]) return true;
        }
    }

    return false;
}

int bfs() {
    memset(st, 0, sizeof st);
    queue<Point> qb, qg;
    qb.push(boy), qg.push(girl);
    st[boy.x][boy.y] = 1, st[girl.x][girl.y] = 2;

    // 只要有一侧的搜索搜到结果，就可以返回时间
    for (int t = 1; !qb.empty() && !qg.empty(); t++)
        if (bfs_each(qb, t, 3) || bfs_each(qg, t, 1)) return t;

    return -1;
}

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &m);
        for (int i = 0, cnt = 0; i < n; i++, getchar())  // 去行尾空格
            for (int j = 0; j < m; j++) {
                char ch = getchar();
                if (ch == 'M') boy = {i, j, 0};
                else if (ch == 'G') girl = {i, j, 0};
                else if (ch == 'Z') ghost[cnt++] = {i, j, 0};
                g[i][j] = ch != 'X';  // 只要不为 X 都能走
            }
        printf("%d\n", bfs());
    }

    return 0;
}