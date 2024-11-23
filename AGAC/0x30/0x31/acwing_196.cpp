#include <iostream>
#include <cstring>
using namespace std;

typedef long long LL;
const int N = 1e6 + 10;
const int M = 5e4;  // sqrt (2^31)

int cnt, st[N], ans[N], v[M], primes[M];

// 把 2 ~ M 的素数筛至 primes 中
void get_primes() {
    memset(v, 0, sizeof v);
    cnt = 0;
    for (int i = 2; i < M; i++) {
        if (v[i] == 0) v[i] = i, primes[++cnt] = i;
        for (int j = 1; j <= cnt; j++) {
            if (primes[j] > v[i] || primes[j] * i > M) break;
            v[primes[j] * i] = primes[j];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    get_primes();

    int l, r;
    while (cin >> l >> r) {
        // 把 [l, r] 内的合数筛掉
        memset(st, 0, sizeof st);
        for (int i = 1; i <= cnt; i++) {
            LL p = primes[i];  // 小心爆 int
            // L <= j * p <= R -> j in [ceil(L/p), floor(R/p)]
            // st[l, r] -> st[l-l, r-l] 后面记得加回来
            for (LL j = max(p << 1, (l + p - 1) / p * p); j <= r; j += p)
                st[j - l] = 1;
        }

        int t = 0;
        for (int i = 0; i <= r - l; i++)
            if (st[i] == 0 && i + l > 1) ans[++t] = i + l;

        if (t < 2) cout << "There are no adjacent primes." << endl;
        else {
            int minp = 1, maxp = 1, d;
            for (int i = 1; i + 1 <= t; i++) {
                d = ans[i + 1] - ans[i];
                if (d < ans[minp + 1] - ans[minp]) minp = i;
                else if (d > ans[maxp + 1] - ans[maxp]) maxp = i;
            }
            cout << ans[minp] << "," << ans[minp + 1] << " are closest, "
                 << ans[maxp] << "," << ans[maxp + 1] << " are most distant."
                 << endl;
        }
    }

    return 0;
}