#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Point {
    int x, y;
    int id;
    Point(int x, int y, int id) {
        this->x = x, this->y = y, this->id = id;
    }
};

bool cmp_xy(const Point& a, const Point& b) {
    return a.x < b.x || (a.x == b.x && a.y < b.y);
}

bool cmp_y(const Point& a, const Point& b) {
    return a.y < b.y;
}

// 计算两点间距离并更新答案
void update(const Point& a, const Point &b) {
    long long dis = (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
    if (dis < mindis) mindis = dis, ans.x = a.id, ans.y = b.id;
}

int n;
long long curdis, mindis;
vector<Point> a;
Point ans;  // ans.x, ans.y 为答案的两个点

void solve(int l, int r) {
    
}

int main() {
    cin >> n;
    int x, y;
    for (int i=0; i<n; i++) {
        cin >> x >> y;
        a.push_back(Point(x, y, i));
    }
    sort(a.begin(), a.end(), cmp_xy);
    mindis = 1e18;
    solve(0, n-1);

    return 0;
}