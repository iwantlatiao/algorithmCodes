#include <iostream>
#include <algorithm>
using namespace std;

#define lowbit(x) ((x) & (-x))

const int MAXL = 100;  // 每行读入数据最大长度
const int MAXN = 9;    // 九宫格长度
const int MAXM = 1 << MAXN;

int ones[MAXM];  // ones[x] 表示 x 的二进制中有多少个 1
int twos[MAXM];  // log2 x = twos[x] 用于 lowbit
int rows[MAXN], cols[MAXN], cells[3][3];  // 行列、大格能填的数
char s[MAXL];

// 如果 is_set = true, 则在 (x,y) 填上 t, 否则在 (x,y) 删去 t
// t in [0, 8]
void draw(int x, int y, int t, int is_set) {
    if (is_set) s[x * MAXN + y] = '1' + t;
    else s[x * MAXN + y] = '.';

    // cout << s << endl;

    int v = 1 << t;
    if (!is_set) v = -v;  // 如果需要删去, 则负负得正
    rows[x] -= v, cols[y] -= v, cells[x / 3][y / 3] -= v;
}

// 初始化每行列和大格能填的数, 返回空的格子数
int init() {
    int cnt = 0, state = (1 << MAXN) - 1;

    fill(rows, rows + MAXN, state);
    fill(cols, cols + MAXN, state);
    fill(cells[0], cells[0] + 9, state);

    for (int i = 0, k = 0; i < MAXN; i++) {
        for (int j = 0; j < MAXN; j++, k++)
            if (s[k] != '.') draw(i, j, s[k] - '1', true);
            else cnt++;
    }

    return cnt;
}

// 拿到 (x, y) 能填的数字, 以二进制数表示
int get_num(int x, int y) {
    return rows[x] & cols[y] & cells[x / 3][y / 3];
}

bool dfs(int cnt) {
    if (!cnt) return true;

    // 选一个能填数字最少的格子开始搜索
    int minv = 10, x = 0, y = 0;
    for (int i = 0; i < MAXN; i++)
        for (int j = 0; j < MAXN; j++)
            if (s[i * MAXN + j] == '.') {
                int num = ones[get_num(i, j)];
                if (num < minv) minv = num, x = i, y = j;
            }

    for (int i = get_num(x, y); i != 0; i -= lowbit(i)) {
        int t = twos[lowbit(i)];  // 准备填的数字
        draw(x, y, t, true);
        if (dfs(cnt - 1))
            return true;  // 若本次填充成功则返回 true, 否则继续搜索
        draw(x, y, t, false);
    }

    return false;  // 没有能填的格子了
}

int main() {
    // 打表: twos[x] = log2(x)
    for (int i = 0; i < MAXN; i++) twos[1 << i] = i;
    // 打表: ones[x] 表示 x 的二进制中有多少个 1
    for (int i = 0; i < MAXM; i++)
        for (int j = i; j != 0; j -= lowbit(j)) ones[i] += 1;
    while (cin >> s, s[0] != 'e') {
        int k = init();
        dfs(k);
        cout << s << endl;
    }
    return 0;
}