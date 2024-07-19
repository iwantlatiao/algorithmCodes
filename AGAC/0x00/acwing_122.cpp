#include <algorithm>
#include <iostream>
using namespace std;

#define MAXN 1000005
typedef long long LL;

int n, a[MAXN];
LL avg, ans, sum[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);

    cin >> n;
    for (int i=1; i<=n; i ++) {cin >> a[i]; avg += a[i];}
    avg /= n;

    for (int i=1; i<=n; i ++) sum[i] = sum[i-1] + a[i] - avg;

    sort(sum + 1, sum + 1 + n);
    for (int i=1; i<=n; i ++) ans += abs(sum[i] - sum[(n + 1) >> 1]);
    cout << ans;
    
    return 0;
}