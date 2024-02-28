#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 10 + 1e6;
int num[MAXN], query[MAXN];

int main() {
    int n, m, q;
    cin >> n >> m;

    for (int i = 0; i < n; ++i)
        cin >> num[i];

    for (int i = 0; i < m; ++i){
        cin >> q;
        int it = lower_bound(num, num+n, q) - num;
        if(q!=num[it]) printf("-1 ");
        else printf("%d ", it+1);
    }

    return 0;
}