# 1-6 二分查找总结

## P2249	查找

输入 $n$ 个单调不减的非负整数然后进行 $m$ 次询问, 输出输出这个数字在序列中第一次出现的编号, 没有找到的话输出 $-1$.

### 思路

二分模板题, 注意超出右边界时需要判断.

```python
i = bisect_left(num, q)
if i == len(num) or num[i] != q:  # 注意判断超出右边界
    print("-1", end=" ")
else:
    print(i + 1, end=" ")
```

## P1102	A-B 数对

给出一串正整数数列以及一个正整数 $C$，要求计算出所有满足 $A - B = C$ 的数对的个数（不同位置的数字一样的数对算不同的数对）。

### 思路

先对数列排序, 然后二分查找 $A=B+C$, 用`bisect_right` 减去 `bisect_left` 即可得到一个数的答案.

## P1873	\[COCI 2011/2012 #5\] EKO / 砍树

有 $N$ 棵树, 要求求出锯片的最高高度 $H$, 使得能得到的木材**至少**为 $M$ 米.

### 思路

二分查找. 左端点为 $0$, 右端点为 $max(height)$. 注意返回的端点不一定满足条件.

```python
def bS(l, r):
    # 注意 res[:r] > M, res[r] <= M
    # 所以要判断返回值是否等于 M
    if l == r:
        if cal(l) >= M: return l
        else: return l - 1
    mid = (l + r) >> 1
    res = cal(mid)
    if res <= M: return bS(l, mid)  # 不够, 砍多点
    else: return bS(mid + 1, r)
```

## P1024	\[NOIP2001 提高组\] 一元三次方程求解
## P1678	烦恼的高考志愿
## P2440	木材加工
## P2678	\[NOIP2015 提高组\] 跳石头
## P3853	\[TJOI2007\] 路标设置
## P1182	数列分段 Section II
## P1163	银行贷款
## P3743	kotori的设备