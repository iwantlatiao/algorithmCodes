# 树状数组

[OI Wiki 对树状数组的介绍](https://oi-wiki.org/ds/fenwick)

[@Jeffery 树状数组入门指南](https://www.cnblogs.com/Jefferyz/p/18055621)

[@王超 树状数组的原理、结构 和 典型应用](https://writings.sh/post/binary-indexed-tree)

回想把正整数分解乘二的不重复次幂的唯一分解性质。若一个数的二进制表示为 $a_{k-1}a_{k-2}\cdots a_{1}a_{0}$，其中等于 1 的位是 $\{ a_{i_1}, \cdots, a_{i_m} \}$，则正整数 x 可以被二进制分解为

$$
x = 2^{i_1} + 2^{i_2} + \cdots + 2^{i_m}
$$

不妨设 $i_1>\cdots > i_m$，这样区间 $[1,x]$ 可以被分为 $O(\log(x))$ 个长度递减的区间。

1. 长度为 $2^{i_1}$ 的区间： $[1, 2^{i_1}]$
2. 长度为 $2^{i_2}$ 的区间： $[2^{i_1} + 1, 2^{i_1} + 2^{i_2}]$
3. 长度为 $2^{i_3}$ 的区间： $[2^{i_1} + 2^{i_2} + 1, 2^{i_1} + 2^{i_2} + 2^{i_3}]$
4. ... 以此类推

所以给定 x 只要不断迭代倒着减区间长度，就可以倒着找到能刚好覆盖区间 $[1,x]$ 的所有子区间。x 的最短子区间长度其实就可以用 `lowbit(x) = x & (~x + 1) = x & (-x)` 计算得出。

```c++
// 计算 [1,x] 的所有子区间
while (x > 0) {
	printf("[%d, %d]\n", x - (x & -x) + 1, x);  // start, end
	x -= x & -x;
}
```

基于上述思想就有了树状数组（Binary Indexed Tree），基本用途是维护序列的前缀和。对于给定的序列 a，可以新建一个数组 c，其中 `c[x]` 保存闭区间 `a[x - lowbit(x) + 1] ~ a[x]` 所有数的和，可以用下图表示。

![OI Wiki 树状数组示意图](https://oi-wiki.org/ds/images/fenwick.svg)

该结构满足几个性质：

1. 节点 `c[x]` 保存以它为根的子树中所有叶节点的和
2. 节点 `c[x]` 覆盖了 a 中 `lowbit(x)` 个元素
3. 除了树根，节点 `c[x]` 的父节点是 `c[x + lowbit(x)]`（ `lowbit(x)` 体现了子节点二分了父节点的一个子区间）
4. 树的深度为 $O(\log n)$

TODO：[LIS 的树状数组做法](https://writings.sh/post/find-number-of-lis)

[@lfool 线段树详解](https://leetcode.cn/problems/range-module/solutions/1612955/by-lfool-eo50/)

