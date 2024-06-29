# 简单数学

## 前缀和

```c++
// 一维
S[i] = a[1] + a[2] + ... a[i]
a[l] + ... + a[r] = S[r] - S[l - 1]

// 二维 S[i, j] = 第i行j列格子左上部分所有元素的和
// 以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵的和为：
S[x2, y2] - S[x1 - 1, y2] - S[x2, y1 - 1] + S[x1 - 1, y1 - 1]
```

## 差分

```c++
// 给区间[l, r]中的每个数加上c
B[l] += c, B[r + 1] -= c

// 给以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵中的所有元素加上c
S[x1, y1] += c, S[x2 + 1, y1] -= c, S[x1, y2 + 1] -= c, S[x2 + 1, y2 + 1] += c
```

## 位运算

```c++
// 求n的第k位数字
n >> k & 1
// 返回n的最后一位
lowbit(n) = n & -n
```

## 双指针

```c++
// 常见问题分类：
// (1) 对于一个序列，用两个指针维护一段区间
// (2) 对于两个序列，维护某种次序，比如归并排序中合并两个有序序列的操作
for (int i = 0, j = 0; i < n; i ++ )
{
    while (j < i && check(i, j)) j ++ ;

    // 具体问题的逻辑
}
```
## 离散化

```c++
vector<int> alls; // 存储所有待离散化的值
sort(alls.begin(), alls.end()); // 将所有值排序
alls.erase(unique(alls.begin(), alls.end()), alls.end());   // 去掉重复元素

// 二分求出x对应的离散化的值
int find(int x) // 找到第一个大于等于x的位置
{
    int l = 0, r = alls.size() - 1;
    while (l < r)
    {
        int mid = l + r >> 1;
        if (alls[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return r + 1; // 映射到1, 2, ...n
}
```
## 区间合并

```c++
// 将所有存在交集的区间合并
void merge(vector<PII> &segs)
{
    vector<PII> res;

    sort(segs.begin(), segs.end());

    int st = -2e9, ed = -2e9;
    for (auto seg : segs)
        if (ed < seg.first)
        {
            if (st != -2e9) res.push_back({st, ed});
            st = seg.first, ed = seg.second;
        }
        else ed = max(ed, seg.second);

    if (st != -2e9) res.push_back({st, ed});

    segs = res;
}
```

## 分形

```c++
// 分形一般有规律可循，找到规律后，可以用 dx, dy
// 保存需要处理的位置，然后求出子问题的解并填入所在位置
```

## 不等式

```c++
// 排序不等式 a[i] * b[i]: 正序 不小于 乱序 不小于 逆序
// a[1] <= ... <= a[n], b[1] <= ... <= b[n]
```