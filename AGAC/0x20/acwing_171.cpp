#include <iostream>
#include <algorithm>
using namespace std;

const int N = 46;
long long n, w, k, g[N + 2], a[1 << 24];
long long cnt = 0, ans = 0;

void dfs1(int u, long long sum) {
    if (sum > w) return;
    if (u > k) {
        a[++cnt] = sum;
        return;
    }

    dfs1(u + 1, sum);
    dfs1(u + 1, sum + g[u]);
}

void dfs2(int u, long long sum) {
    if (sum > w) return;
    if (u > n) {
        int l = 1, r = cnt, mid;
        while (l < r) {
            mid = (l + r + 1) >> 1;
            if (a[mid] + sum <= w) l = mid;
            else r = mid - 1;
        }
        ans = max(ans, a[l] + sum);
        return;
    }

    dfs2(u + 1, sum);
    dfs2(u + 1, sum + g[u]);
}

int main() {
    cin >> w >> n;
    for (int i = 1; i <= n; i++) cin >> g[i];
    sort(g + 1, g + n + 1);

    k = n >> 1;  // 两次搜索的分界点
    dfs1(1, 0);  // 1 ~ k
    sort(a + 1, a + cnt + 1);
    cnt = unique(a + 1, a + cnt + 1) - (a + 1);
    dfs2(k + 1, 0);  // k + 1 ~ n

    cout << ans;

    return 0;
}