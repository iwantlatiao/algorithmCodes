#include <iostream>
using namespace std;

const int N = 10005;
int n, ans[N];

bool dfs(int u, int maxu) {
    if (u == maxu) return ans[u] == n;
    if (ans[u] * (1 << (maxu - u)) < n) return false;

    bool vis[N] = {false};
    for (int i = u; i >= 1; i--)
        for (int j = i; j >= 1; j--) {
            int s = ans[i] + ans[j];
            if (vis[s] || s <= ans[u] || s > n) continue;

            vis[s] = true;
            ans[u + 1] = s;

            if (dfs(u + 1, maxu)) return true;
        }
    return false;
}

int main() {
    ans[1] = 1;
    while (cin >> n, n != 0) {
        for (int i = 1; i <= N; i++) {
            if (dfs(1, i)) {
                for (int j = 1; j <= i; j++) cout << ans[j] << " ";
                cout << endl;
                break;
            }
        }
    }

    return 0;
}