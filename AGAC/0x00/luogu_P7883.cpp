#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

const int MAXN = 400010;

int n;
long long mindis;
double mindis_sqrt;

struct Point {
    long long x, y;
    int id;
    Point() {}
    Point(long long x, long long y, int id) {
        this->x = x, this->y = y, this->id = id;
    }
};

Point a[MAXN], tmp[MAXN];  // 储存第二次排序的结果

bool cmp_xy(Point& a, Point& b) {
    return a.x < b.x || (a.x == b.x && a.y < b.y);
}

bool cmp_y(Point& a, Point& b) {
    return a.y < b.y;
}

// 计算两点间距离并更新答案
long long dist(Point& a, Point& b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

void update(Point& a, Point& b) {
    long long dis = dist(a, b);
    if (dis < mindis) mindis = dis, mindis_sqrt = sqrt(dis);
}

void solve(int l, int r) {
    // 点少时直接两两计算距离
    if (r - l <= 3) {
        for (int i = l + 1; i <= r; i++)
            for (int j = l; j < i; j++) update(a[i], a[j]);
        // sort(a + l, a + r + 1, cmp_y);  // nlogn 写法需要
        return;
    }

    // 1. nloglogn 写法
    int k = 0, mid = (l + r) >> 1;
    solve(l, mid), solve(mid + 1, r);
    for (int i = l; i <= r; i++)  // 不够快，更快的方法是左右各取 6 个点直接算
        if (abs(a[i].x - a[mid].x) < mindis_sqrt) tmp[k++] = a[i];
    sort(tmp, tmp + k, cmp_y);
    for (int i = 0; i < k; i++)
        for (int j = i + 1; j < k and tmp[j].y - tmp[i].y < mindis_sqrt; j++)
            update(tmp[i], tmp[j]);

    // 2. nlogn 写法 但是常数大不一定比 1 快
    // int mid = (l + r) >> 1;
    // int midx = a[mid].x;
    // solve(l, mid), solve(mid + 1, r);
    // inplace_merge(a + l, a + mid + 1, a + r + 1, cmp_y);

    // static Point t[MAXN];
    // int tsz = 0;
    // for (int i = l; i <= r; ++i)
    //     if (abs(a[i].x - midx) < mindis_sqrt) {
    //         for (int j = tsz - 1; j >= 0 && a[i].y - t[j].y < mindis_sqrt; --j)
    //             update(a[i], t[j]);
    //         t[tsz++] = a[i];
    //     }
}

int main() {
    scanf("%d", &n);
    int x, y;
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &x, &y);
        a[i].x = x, a[i].y = y;
    }
    sort(a, a + n, cmp_xy);
    mindis = 1e18;
    solve(0, n - 1);
    cout << mindis;

    return 0;
}