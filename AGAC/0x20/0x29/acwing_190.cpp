#include <cstring>
#include <iostream>
#include <unordered_map>
#include <queue>

using namespace std;

const int N = 8;
string A, B;
string a[N], b[N];
int n;

// 从 a 状态到 b 状态
int extend(queue<string>& q, unordered_map<string, int>& ma, unordered_map<string, int>& mb, string a[N], string b[N]) {
    int d = ma[q.front()];  // 本次遍历的步数
    while (q.size() && ma[q.front()] == d) {
        string t = q.front();
        q.pop();

        // 查找有没有可以变化的字串
        for (int i = 0; i < n; i++)
            for (int j = 0; j < t.size(); j++) 
                if (t.substr(j, a[i].size()) == a[i]) {
                    string c = t.substr(0, j) + b[i] + t.substr(j + a[i].size());
                    if (mb.count(c)) return ma[t] + 1 + mb[c];
                    if (ma.count(c)) continue;
                    ma[c] = ma[t] + 1;
                    q.push(c);
                }
            
    }

    return 11;
}

int bfs() {
    unordered_map<string, int> da, db;  // 保存双向搜索时的变换步数
    queue<string> qa, qb;
    int step = 0;

    qa.push(A), qb.push(B);
    da[A] = 0, db[B] = 0;

    // 只要其中一个队列空，就说明无法变换到目标
    while (qa.size() && qb.size()) {
        int t;
        if (qa.size() < qb.size()) t = extend(qa, da, db, a, b);
        else t = extend(qb, db, da, b, a);
        if (t <= 10) return t;
        if (++step > 10) return -1;
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    cin >> A >> B;
    if (A == B) {cout << "0"; return 0;}
    while (cin >> a[n] >> b[n]) n += 1;

    int t = bfs();
    if (t == -1) cout << "NO ANSWER!";
    else cout << t;

    return 0;
}