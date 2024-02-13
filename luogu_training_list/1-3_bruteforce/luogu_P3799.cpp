#include <iostream>
#include <vector>
using namespace std;

const int MAXNUM = 5010;
const int MODNUM = 1000000000 + 7;

int main()
{
    int ans = 0;
    int N;
    cin >> N;

    vector<int> num(MAXNUM, 0);
    for (int i = 0; i < N; ++i)
    {
        int inputNum;
        scanf("%d", &inputNum);
        ++num[inputNum];
    }

    vector<int> numMap;
    for (int i = 0; i < MAXNUM; ++i)
    {
        if (num[i] > 0)
        {
            numMap.push_back(i);
        }
    }

    for (int indX = 1; indX < numMap.size(); ++indX)
    {
        for (int indY = 0; indY < indX; ++indY)
        {
            int x = numMap[indX];
            int y = numMap[indY];
            int xQ = num[x];
            int yQ = num[y];

            if (y + y == x)
            {
                if (xQ >= 2 && yQ >= 2)
                {
                    ans = (ans + ((xQ * (xQ - 1)) >> 1) * ((yQ * (yQ - 1)) >> 1)) % MODNUM;
                }
            }
            else if (y + y < x)
            {
                int z = x - y;
                int zQ = num[z];
                if (xQ >= 2 && zQ >= 1)
                {
                    ans = (ans + ((xQ * (xQ - 1)) >> 1) * yQ * zQ) % MODNUM;
                }
            }
            else
            {
                break;
            }
        }
    }

    cout << ans << endl;
    return 0;
}
