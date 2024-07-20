#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int T, a, b;
string a_line, b_line;

vector<int> div(vector<int> &X, int y, int &r) {
    vector<int> C;
    r = 0;
    for (int i = X.size() - 1; i >= 0; i--) {
        r = r * a + X[i];
        C.push_back(r / y);
        r %= y;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 0 && C.back() == 0) C.pop_back();
    return C;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);

    // freopen("input.txt", "r", stdin);

    cin >> T;
    while(T--) {
        vector<int> numbers, res;
        cin >> a >> b >> a_line;
        for (auto c : a_line)
            if ('0' <= c && c <= '9') numbers.push_back(c - '0');
            else if ('A' <= c && c <= 'Z') numbers.push_back(c - 'A' + 10);
            else if ('a' <= c && c <= 'z') numbers.push_back(c - 'a' + 36);
        reverse(numbers.begin(), numbers.end());

        // 短除法换算进制
        while (numbers.size() > 0) {
            int r = 0;
            numbers = div(numbers, b, r);
            res.push_back(r);
        }

        reverse(res.begin(), res.end());
        b_line.clear();

        for (auto x : res)
            if (x <= 9) b_line += char(x + '0');
            else if (x <= 35) b_line += char(x - 10 + 'A');
            else b_line += char (x - 36 + 'a');
        
        cout << a << ' ' << a_line << '\n';
        cout << b << ' ' << b_line << '\n';
        cout << '\n';
    }

    return 0;
}