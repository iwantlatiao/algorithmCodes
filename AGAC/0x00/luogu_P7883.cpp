#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Point {
    long long x, y;
    int id;
    Point(long long x, long long y, int id) {
        this->x = x, this->y = y, this->id = id;
    }
};

bool cmp_xy(const Point& a, const Point& b) {
    return a.x < b.x || (a.x == b.x && a.y < b.y);
}

bool cmp_y(const Point& a, const Point& b) {
    return a.y < b.y;
}

int n;
vector<Point> a;

void solve(long long l, long long r) {
    
}

int main() {
    cin >> n;
    long long x, y;
    for (int i=0; i<n; i++) {
        cin >> x >> y;
        a.push_back(Point(x, y, i));
    }
    sort(a.begin(), a.end(), cmp_xy);

    return 0;
}