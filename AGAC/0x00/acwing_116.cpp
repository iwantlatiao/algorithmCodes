#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

struct Node {
    int x, y;
    Node(int x, int y) { this->x = x, this->y = y; }
};

const int N = 5;
char g[N][N];    // 原始地图
char tmp[N][N];  // 用于备份原始地图

// 坐标 (x,y) 对应的数码 0~15
int getNum(int x, int y) {
    return (x << 2) + y;
}

// 把坐标 (x,y) 的反转
void turnOne(int x, int y) {
    if (g[x][y] == '+') g[x][y] = '-';
    else g[x][y] = '+';
}

// 把 x 行 y 列 的反转
void turn(int x, int y) {
    for (int i = 0; i < 4; i++) turnOne(x, i), turnOne(i, y);
    turnOne(x, y);
}

bool allOpen() {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (g[i][j] == '+') return false;
    return true;
}

int main() {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) cin >> g[i][j];

    vector<Node> res;  // 最终方案

    for (int op = 0; op < 1 << 16; op++) {
        vector<Node> now;  // 当前方案
        memcpy(tmp, g, sizeof(g));

        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (op & 1 << getNum(i, j))
                    turn(i, j), now.push_back(Node(i, j));

        if (allOpen() && (res.empty() || res.size() > now.size())) res = now;

        memcpy(g, tmp, sizeof(tmp));
    }

    cout << res.size() << endl;
    for (auto op : res) cout << op.x + 1 << " " << op.y + 1 << endl;
}