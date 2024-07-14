#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 200010;
const int INF = 0x3f3f3f3f;
int t, n;
int minx = INF, maxx = 0;

struct num {
    int s, e, d;
} a[MAXN];

int getSum(int x) {
    int res = 0;
    for (int i = 1; i <= n; i++)
        if (a[i].s <= x) res += (min(a[i].e, x) - a[i].s) / a[i].d + 1;
    return res;
}

bool check(int l, int r) {
    return (getSum(r) - getSum(l - 1)) & 1;
}

int main() {
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> a[i].s >> a[i].e >> a[i].d;
            minx = min(minx, a[i].s), maxx = max(maxx, a[i].e);
        }

        if ((getSum(maxx) & 1) == 0) cout << "There's no weakness." << endl;
        else {
            int l = minx, r = maxx;
            while (l < r) {
                int mid = (l + r) >> 1;
                if (check(l, mid)) r = mid;
                else l = mid + 1;
            }
            cout << l << " " << getSum(l) - getSum(l - 1) << endl;
        }
    }
    return 0;
}