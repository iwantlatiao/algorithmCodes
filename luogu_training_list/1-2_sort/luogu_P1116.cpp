#include <cstdio>
using namespace std;

const int MAXN = 10010;

int N, num[MAXN];
int ans = 0;

void merge(int *a, int aLen, int *b, int bLen, int *c)
{
    int i = 0, j = 0, k = 0;
    while (i < aLen && j < bLen)
    {
        if (a[i] <= b[j])
        {
            c[k] = a[i];
            ++i;
        }
        else
        {
            c[k] = b[j];
            ++j;
            ans += aLen - i;
        }
        ++k;
    }
    for (; i < aLen; ++i, ++k)
        c[k] = a[i];
    for (; j < bLen; ++j, ++k)
        c[k] = b[j];
}

void mergeSort(int *a, int l, int r) // [l,r)
{
    if (r - l <= 1)
        return;
    int mid = (r + l) >> 1;
    mergeSort(a, l, mid);
    mergeSort(a, mid, r);

    int tSize = r - l + 1;
    int tmp[tSize] = {};
    merge(a + l, mid - l, a + mid, r - mid, tmp);

    for (int i = l, j = 0; i < r; ++i, ++j)
        a[i] = tmp[j];
}

int main()
{
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
        scanf("%d", &num[i]);

    mergeSort(num, 0, N);

    printf("%d", ans);
    return 0;
}