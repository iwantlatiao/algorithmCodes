#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define MAXN 1005
typedef pair<int, int> PII;

int C, N, x, y;
int sum[MAXN][MAXN];
vector<int> numbers;  // 离散化
vector<PII> points;   // 坐标

// 输入原始大小，输出离散后的索引
int get(int n) {
    return lower_bound(numbers.begin(), numbers.end(), n) - numbers.begin();
}

bool check(int len) {
    for (int x1 = 0, x2 = 1; x2 < numbers.size(); x2++) {
        // 找第一个不在 len 区间内的 x1
        while (numbers[x2] - numbers[x1 + 1] + 1 > len) x1++;
        for (int y1 = 0, y2 = 1; y2 < numbers.size(); y2++) {
            while (numbers[y2] - numbers[y1 + 1] + 1 > len) y1++;
            if (sum[x2][y2] - sum[x1][y2] - sum[x2][y1] + sum[x1][y1] >= C)
                return true;
        }
    }
    return false;
}

int main() {
    numbers.push_back(-1);  // 加一行一列空，便于前缀和的计算
    cin >> C >> N;
    for (int i = 0; i < N; i++) {
        cin >> x >> y;
        numbers.push_back(x);
        numbers.push_back(y);
        points.push_back({x, y});
    }

    // 离散化
    sort(numbers.begin(), numbers.end());
    numbers.erase(unique(numbers.begin(), numbers.end()), numbers.end());

    // 前缀和
    for (int i = 0; i < N; i++) {
        int x = get(points[i].first), y = get(points[i].second);
        sum[x][y]++;
    }
    for (int i = 1; i < numbers.size(); i++)
        for (int j = 1; j < numbers.size(); j++)
            sum[i][j] += sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];        

    int l = 1, r = 10000;
    while (l < r) {
        int mid = (l + r) >> 1;
        if (check(mid)) r = mid;
        else l = mid + 1;
    }

    cout << l;

    return 0;
}