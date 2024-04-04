#include <set>
#include <cstdio>
#include <algorithm>
using namespace std;

int n, x;
long long ans = 0;
const int MAXNUM = 1e7, MINNUM = -1e7;
set<int> s;
set<int>::iterator pos, pre;

int main(){
    scanf("%d", &n);
    for (int i=1; i<=n; i++) {
        scanf("%d", &x);
        if (i == 1) {
            s.insert(x), s.insert(MAXNUM), s.insert(MINNUM);
            ans += x;
        }
        else {
            pos = s.lower_bound(x);
            if (*pos != x) {
                pre = pos;
                pre--;
                ans += min(abs(x-*pre), abs(x-*pos));
                s.insert(x);
            }
        }
    }
    printf("%d", ans);
}