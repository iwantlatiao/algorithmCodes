#include <iostream>
#include <queue>
using namespace std;

deque<int> cards[15];
char c;
int ans = 0, now, back;
int bucket[15];

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
        now = cards[13].front();
        cards[13].pop_front();

        while (now != 13) {
            cards[now].push_front(now);
            if (++bucket[now] >= 4) ++ans;  // 这张牌翻开且放到最前

            back = cards[now].back();  // 从末尾抽牌
            cards[now].pop_back();
            now = back;
        }
    }
    cout << ans;

    return 0;
}