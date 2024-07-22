#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

typedef pair<int, int> PII;  // time, difficulty
const int N = 100010;
int n, m, cnt;
long long ans;
PII machine[N], task[N];
multiset<int> s;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);

    while (cin >> n >> m) {
        for (int i=1; i<=n; i ++) 
            cin >> machine[i].first >> machine[i].second;
        for (int i=1; i<=m; i ++) 
            cin >> task[i].first >> task[i].second;

        sort(machine + 1, machine + 1 + n);
        sort(task + 1, task + 1 + m);
        s.clear();

        // 从时间长的任务开始，到时间短的任务
        for (int i=m, j=n; i>=1; i--) {
            // 把满足时间条件的机器 的难度 加入 multiset
            while (j>=1 && machine[j].first >= task[i].first) 
                s.insert(machine[j--].second);
            auto iter = s.lower_bound(task[i].second);
            if (iter != s.end()) {
                cnt++, ans += 500 * task[i].first + 2 * task[i].second;
                s.erase(iter);
            }
        }

        cout << cnt << " " << ans;
    }

    return 0;
}