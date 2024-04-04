# 2-2 二叉树总结

## P4715	【深基16.例1】淘汰赛

有 $2^n$（$n\le7$）个国家参加世界杯决赛圈且进入淘汰赛环节。已经知道各个国家的能力值，且都不相等。能力值高的国家和能力值低的国家踢比赛时高者获胜。1 号国家和 2 号国家踢一场比赛，胜者晋级。3 号国家和 4 号国家也踢一场，胜者晋级……晋级后的国家用相同的方法继续完成赛程，直到决出冠军。给出各个国家的能力值，请问亚军是哪个国家？

### 思路

- 直接对列表排序后取第二个最大的思路不正确, 因为可能第二个最大的在决赛之前就碰到了最大的被淘汰.
- 除了用二叉树或递归的方式直接模拟, 实际上分析可得只需对列表分成前半和后半, 然后分别排序后取最大, 比较出第二大即为答案.

## P4913	【深基16.例3】二叉树深度

有一个 $n(n \le 10^6)$ 个结点的二叉树。给出每个结点的两个子结点编号（均不超过 $n$），建立一棵二叉树（根节点的编号为 $1$），如果是叶子结点，则输入 `0 0`。

建好这棵二叉树之后，请求出它的深度。二叉树的**深度**是指从根节点到叶子结点时，最多经过了几层。

### 思路

先建树, 然后用 BFS 或 DFS 搜索深度. 注意 `python` 递归深度默认只有 $996$ , 需要手动设置递归深度:

```python
import sys
sys.setrecursionlimit(limit)
```

## P1827	[USACO3.4] 美国血统 American Heritage

给定前序遍历和中序遍历, 求后序遍历

### 思路

二叉树遍历顺序: 前序遍历根左右; 中序遍历左根右; 后序遍历左右根.

所以给定前序 `pre` 和中序 `inor`, 可以先根据前序 `pre` 的第一位找到根节点 `root`, 然后在中序 `inor` 中找到 `root` 的位置, 左侧节点构成左子树, 右侧节点构成右子树, 然后分别继续递归即可.

```c++
string pre,inor;
void work(string pre,string inor)
{
    if(pre.empty())return;
    //如果序列空了，就没必要继续了
    char root=pre[0];
    //取到前序序列的首字母，即根节点
    int k=inor.find(root);
    //找到中序序列中根节点的位置
    pre.erase(pre.begin());
    //删去前序序列中的根节点
    string leftpre=pre.substr(0,k);
    //从0开始切割k个
    string rightpre=pre.substr(k);
    //从k开始切割到最后
    string leftinor=inor.substr(0,k);
    //从0开始切割k个
    string rightinor=inor.substr(k+1);
    //从k+1开始切割到最后
    work(leftpre,leftinor);
    work(rightpre,rightinor);
    printf("%c",root);
    //因为要输出后序序列，所以是左右根
    //先遍历左子树，再右子树，再根节点
}
int main()
{
    cin>>inor>>pre;
    work(pre,inor);
    putchar('\n');
    return 0;
}
```
如果需要建树, 则递归返回 `root` 节点, 父节点的儿子指向 `root` 节点. 如果节点数较多, 可以做一个哈希映射, 帮助我们快速定位根节点. [Leetcode 105](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/255811/cong-qian-xu-yu-zhong-xu-bian-li-xu-lie-gou-zao-9/)

```python
# 构造哈希映射，帮助我们快速定位根节点
index = {element: i for i, element in enumerate(inorder)}
```

## P5076	【深基16.例7】普通二叉树（简化版）

要求实现一个 BST, 操作有插入和查询前序, 后继, 第 k 个. 其实与 [P2234](../2-1_linearList/readme.md/#p2234-hnoi2002-营业额统计) 差不多.

## P1364	医院设置
## P1229	遍历问题
## P1305	新二叉树
## P1030	[NOIP2001 普及组] 求先序排列

已知中序遍历和后序遍历, 求先序遍历. 和 P1827 一样的思路.

## P3884	[JLOI2009] 二叉树问题
## P1185	绘制二叉树