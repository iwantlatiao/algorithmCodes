#include <iostream>
#include <queue>
using namespace std;

deque<int> cards[15];
char c;

int main() {
    for (int i = 1; i <= 13; i++) {
        for (int j = 1; j <= 4; j++) {
            cin >> c;
            if ('2' <= c and c <= '9') cards[i].push_back(c - '0');
            else if (c == '0') cards[i].push_back(10);
            else if (c == 'J') cards[i].push_back(11);
            else if (c == 'Q') cards[i].push_back(12);
            else if (c == 'K') cards[i].push_back(13);
            else cards[i].push_back(1);  // c == 'A'
        }
    }

    while (cards[13].size() > 0) {
        int now = cards[13].front();
        cards[13].pop_front();

        if (now==13) continue;
        
    }

    return 0;
}