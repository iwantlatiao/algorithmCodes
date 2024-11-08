#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef pair<int, int> PII;
const int N = 805;
const int INF = 0x3f3f3f3f;

int n, m, t;
bool g[N][N];  // true 能走 false 不能走
int st[N][N];

struct Point {
    int x, y, d;
} boy, girl, ghost[2];

int bfs() {
    memset(st, 0, sizeof st);
    queue<Point> qb, qg;
    qb.push(boy), qg.push(girl);
    st[boy.x][boy.y] = 1, st[girl.x][girl.y] = 2;
    return -1;
}

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &m);
        for (int i = 0, cnt = 0; i < n; i++, getchar())  // 去行尾空格
            for (int j = 0; j < n; j++) {
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