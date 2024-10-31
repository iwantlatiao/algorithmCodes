#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 70;

int n, sum, cnt, nowlen, maxlen;
int sticks[N];
bool vis[N];

// 正在拼第 stick 根木棍，该木棍当前长度 cab，从 start 开始枚举木棍序号 
bool dfs(int stick, int cab, int start) {
    // 全拼好了
    if (stick > cnt) return true;
    // 拼下一根
    if (cab == nowlen) return dfs(stick + 1, 0, 1);

    int fail = 0;  // 上一根失败的长度
    for (int i = start; i <= n; i++) {
        if (!vis[i] && fail != sticks[i] && cab + sticks[i] <= nowlen) {
            vis[i] = true;
            if(dfs(stick, cab + sticks[i], i + 1)) return true;
            vis[i] = false;
            fail = sticks[i];
            if (cab == 0 || cab + sticks[i] == nowlen) return false;
        }
    }

    return false;
}

int main() {
    while (cin >> n, n > 0) {
        memset(sticks, 0, sizeof sticks);
        memset(vis, 0, sizeof vis);
        sum = maxlen = 0;

        for (int i = 1; i <= n; i++) {
            cin >> sticks[i];
            sum += sticks[i];
            maxlen = max(maxlen, sticks[i]);
        }
        sort(sticks + 1, sticks + 1 + n);
        reverse(sticks + 1, sticks + 1 + n);

        for (nowlen = maxlen;; nowlen++) {
            if (sum % nowlen != 0) continue;
            cnt = sum / nowlen;
            if (dfs(1, 0, 1)) {
                cout << nowlen << endl;
                break;
            }
        }
    }

    return 0;
}