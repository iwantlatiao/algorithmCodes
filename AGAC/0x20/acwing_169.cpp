#include <iostream>
#include <cstring>
using namespace std;

const int N = 16;

int ones[1 << N];  // ones[x] x 在二进制下有多少个 1
int twos[1 << N];  // log2 x = twos[x] 用于 lowbit
int state[N][N];   // state[x][y] (x, y) 能填哪些数，由二进制数表示
int bstate[N * N + 1][N][N],
    bstate2[N * N + 1][N][N];  // 备份状态，用于回溯时还原
char str[N][N + 1], bstr[N * N + 1][N][N + 1];  // 地图和备份地图，+1为了存 \0

inline int lowbit(int x) {
    return ((x) & (-x));
}

// 在 (x, y) 写字母 c
void draw(int x, int y, int c) {
    str[x][y] = 'A' + c;

    // 更新行、列、方块内能填哪些数
    for (int i = 0; i < N; i++)
        state[x][i] &= ~(1 << c), state[i][y] &= ~(1 << c);

    int sx = x / 4 * 4, sy = y / 4 * 4;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) state[sx + i][sy + j] &= ~(1 << c);
    state[x][y] = 1 << c;
}

bool dfs(int cnt) {
    if (cnt == 0) return true;

    // 备份状态
    int bcnt = cnt;
    memcpy(bstate[bcnt], state, sizeof state);
    memcpy(bstr[bcnt], str, sizeof str);

    // 剪枝1. 枚举每个空格
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (str[i][j] == '-') {
                // 无法填任何一个字符
                if (state[i][j] == 0) {
                    memcpy(state, bstate[bcnt], sizeof state);
                    memcpy(str, bstr[bcnt], sizeof str);
                    return false;
                }
                // 只能填一个字符
                else if (ones[state[i][j]] == 1) {
                    draw(i, j, twos[state[i][j]]);
                    cnt -= 1;
                }
            }

    // 剪枝2. 枚举每行
    for (int i = 0; i < N; i++) {
        int sor = 0;              // 本行每个格子备选方案的并集
        int sand = (1 << N) - 1;  // 用来找只有一个位置可以填的字母
        int drawn = 0;            // 已经填上的字母

        // 对于行内的每个格子
        // sand 的模拟：开始时 sor = 0 sand = 全 1
        // 假设能填的数字是 x，第一次出现时，sor & state[i][j] 的 x 位为 0
        // 所以 sand 的 x 位为 1，在此后将 sor 的 x 位置为 1
        // 所以第二次出现时 sand 的 x 位就会为 0
        for (int j = 0; j < N; j++) {
            sand &= ~(sor & state[i][j]);
            sor |= state[i][j];
            if (str[i][j] != '-') drawn |= state[i][j];
        }

        // 一行内应该每个字母都有出现
        if (sor != (1 << N) - 1) {
            memcpy(state, bstate[bcnt], sizeof state);
            memcpy(str, bstr[bcnt], sizeof str);
            return false;
        }

        // 按照定义，sand 为 1 的位包括只有一个位置可以填的字母
        // 和没有位置可以填的字母（其实已经在上面筛掉，不会出现）
        for (int j = sand; j != 0; j -= lowbit(j)) {
            int t = lowbit(j);
            // 如果是已经填的（sand包括可以填的和已经填的）就跳过
            if (drawn & t) continue;
            for (int k = 0; k < N; k++) {
                if (state[i][k] & t) {
                    draw(i, k, twos[t]);
                    cnt -= 1;
                    break;
                }
            }
        }
    }

    // 剪枝3. 枚举每列
    for (int j = 0; j < N; j++) {
        int sor = 0;              // 本列每个格子备选方案的并集
        int sand = (1 << N) - 1;  // 用来找只有一个位置可以填的字母
        int drawn = 0;            // 已经填上的字母

        // 对于列内的每个格子
        for (int i = 0; i < N; i++) {
            sand &= ~(sor & state[i][j]);
            sor |= state[i][j];
            if (str[i][j] != '-') drawn |= state[i][j];
        }

        // 一列内应该每个字母都有出现
        if (sor != (1 << N) - 1) {
            memcpy(state, bstate[bcnt], sizeof state);
            memcpy(str, bstr[bcnt], sizeof str);
            return false;
        }

        for (int i = sand; i != 0; i -= lowbit(i)) {
            int t = lowbit(i);
            if (drawn & t) continue;
            for (int k = 0; k < N; k++) {
                if (state[k][j] & t) {
                    draw(k, j, twos[t]);
                    cnt -= 1;
                    break;
                }
            }
        }
    }

    // 剪枝4. 枚举每个 4x4 方格
    for (int i = 0; i < N; i++) {
        int sor = 0;              // 本行每个格子备选方案的并集
        int sand = (1 << N) - 1;  // 用来找只有一个位置可以填的字母
        int drawn = 0;            // 已经填上的字母

        // 对于方格的每个格子
        for (int j = 0; j < N; j++) {
            int sx = i / 4 * 4, sy = i % 4 * 4;
            int dx = j / 4, dy = j % 4;
            int s = state[sx + dx][sy + dy];
            sand &= ~(sor & s);
            sor |= s;
            if (str[sx + dx][sy + dy] != '-') drawn |= s;
        }

        // 一行内应该每个字母都有出现
        if (sor != (1 << N) - 1) {
            memcpy(state, bstate[bcnt], sizeof state);
            memcpy(str, bstr[bcnt], sizeof str);
            return false;
        }

        // 按照定义，sand 为 1 的位包括只有一个位置可以填的字母
        // 和没有位置可以填的字母（其实已经在上面筛掉，不会出现）
        for (int j = sand; j != 0; j -= lowbit(j)) {
            int t = lowbit(j);
            // 如果是已经填的（sand包括可以填的和已经填的）就跳过
            if (drawn & t) continue;
            for (int k = 0; k < N; k++) {
                int sx = i / 4 * 4, sy = i % 4 * 4;
                int dx = k / 4, dy = k % 4;
                if (state[sx + dx][sy + dy] & t) {
                    draw(sx + dx, sy + dy, twos[t]);
                    cnt -= 1;
                    break;
                }
            }
        }
    }

    if (cnt == 0) return true;

    // 剪枝5. 选择可填字母最少的格子填写
    int x, y, mincnt = N;
    for (int i = 0; i < N; i++) 
        for (int j = 0; j < N; j++)
            if (str[i][j] == '-' && ones[state[i][j]] < mincnt) {
                mincnt = ones[state[i][j]];
                x = i, y = j;
            }

    // 备份此时状态，不需要备份 str 的原因是只对 str[x][y] 操作
    memcpy(bstate2[cnt], state, sizeof state);
    for (int i = state[x][y]; i != 0; i -= lowbit(i)) {
        memcpy(state, bstate2[cnt], sizeof state);  // 还原上一个状态
        draw(x, y, twos[lowbit(i)]);  // 修改多个 state 状态和 str[x][y]
        if (dfs(cnt - 1)) return true;
    }

    // 搜索分支失败
    memcpy(state, bstate[bcnt], sizeof state);
    memcpy(str, bstr[bcnt], sizeof str);
    return false;
}

int main() {
    // 打表
    for (int i = 0; i < N; i++) twos[1 << i] = i;
    for (int i = 0; i < (1 << N); i++)
        for (int j = i; j != 0; j -= lowbit(j)) ones[i] += 1;

    while (cin >> str[0]) {
        for (int i = 1; i < N; i++) cin >> str[i];

        // 状态重置
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++) state[i][j] = (1 << N) - 1;

        // 初始化格子状态
        int cnt = 0;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (str[i][j] != '-') draw(i, j, str[i][j] - 'A');
                else cnt += 1;

        dfs(cnt);

        for (int i = 0; i < N; i++) cout << str[i] << endl;
        cout << endl;
    }
    return 0;
}