#include <iostream>
using namespace std;

int P, depth = 0;

// a > b
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

bool dfs(int nowd, int a, int b) {
    if (nowd == depth) 
        if (a == P) return true;
        else return false;
    if (a << (depth - nowd) < P) return false;
    if (P % gcd(a, b) != 0) return false;

    int x, y;

    x = a + b, y = a;
    if (y > 0 && dfs(nowd + 1, x, y)) return true;

    x = a + b, y = b;
    if (y > 0 && dfs(nowd + 1, x, y)) return true;

    x = a << 1, y = a;
    if (y > 0 && dfs(nowd + 1, x, y)) return true;

    x = a << 1, y = b;
    if (y > 0 && dfs(nowd + 1, x, y)) return true;

    x = b << 1, y = a;
    if (x < y) swap(x, y);
    if (y > 0 && dfs(nowd + 1, x, y)) return true;

    x = b << 1, y = b;
    if (y > 0 && dfs(nowd + 1, x, y)) return true;

    x = a - b, y = a;
    if (x < y) swap(x, y);
    if (y > 0 && dfs(nowd + 1, x, y)) return true;

    x = a - b, y = b;
    if (x < y) swap(x, y);
    if (y > 0 && dfs(nowd + 1, x, y)) return true;
    
    return false;
}

int main() {
    cin >> P;
    while (!dfs(0, 1, 0)) depth += 1;
    cout << depth;
    
    return 0;
}