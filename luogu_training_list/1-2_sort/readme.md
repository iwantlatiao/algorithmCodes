# 1-2 排序总结

## P1271 选举学生会

桶排

## P1177 排序

排序模板题：[快速排序算法实现](https://oi-wiki.org/basic/quick-sort/)；[单路、双路和三路快速排序](https://blog.csdn.net/weixin_45666566/article/details/108646880)

在 python 中手动实现两路快排会 TLE，提交使用 sort 函数

## P1923 求第 k 小的数 (MLE)

使用三路快排做到期望时间 $O(n)$ 找第 k 小的数

[本题超过空间限制的讨论](https://www.luogu.com.cn/discuss/672452)：
如果用 `input().split()` 直接读入会 MLE，假设 `input().split()` 中 `input()` 这个字符串在 `.split()` 过程中不会及时地释放内存，假设第二行数据有 5000000 个数，每个都是 100000000，加上空格，每个数字平均约 11 个字节，那么第二句占用内存最大的时候应该有约
$$5000000\times (8_{指针}+49_{空串}+11_{每个字符}\times 2_{记录两次}) +56+49=376 MB$$

所以普通读入最后两个点会爆空间，据说洛谷可以用 numpy 但是我没调出来


## P1059 \[NOIP2006 普及组\] 明明的随机数

桶排

## P1093 \[NOIP2007 普及组\] 奖学金

多字段排序

## P1781 宇宙总统

大整数排序，对于没有高精度的语言可以用字符串找最大值

```python
num = ["123", "2345", "132", "66", "12345"]
sorted(num, key=lambda x: (len(x[0]), x[0]), reverse=True)
```

## P2676 \[USACO07DEC\] Bookshelf B

排序模板题：[归并排序算法实现](https://oi-wiki.org/basic/merge-sort/)

## P1116 车厢重组

求逆序对的题目，由于数据量不大，所以可以使用朴素/冒泡排序/插入排序计算逆序对

本解法修改归并排序以计算逆序对。


## P1152 欢乐的跳

简单排序

## P1068 \[NOIP2009 普及组\] 分数线划定

简单排序

## P5143 攀爬者

根据 z 轴排序，算距离相加即可

## P1104 生日

生日排序，多字段排序

## P1012 \[NOIP1998 提高组\] 拼数 & LeetCode 179 最大数

题目描述：给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例：输入 (10, 2) 输出 210；输入 (3,30,34,5,9) 输出 9534330

思路

- 为了构建最大数字，希望越高位的数字越大越好。朴素的思想是做降序排序，依次取数。但如果仅按降序排序，对相同的开头长度不同数字的时候会出现问题。所以对于长度不同的数，如 6 和 65 在比较完 6 这一位后，空 和 5 应该选空。具体实现方法是写一个 cmp 函数，然后每次取一次位作比较，这样的复杂度会比较高。
- 还有一种更简单的实现方法，对于一串数字 a, b, ... 实际就是每次比较两个数字，然后把更优的放在前面。对于 cmp 函数，因为 ab 和 ba 的长度是相同的，所以我们可以把检查数位转换为检查字符串，如果字符串 ab 大于字符串 ba 就说明 a 比 b 更应该放在前面。

关于排序方式的速度比较：Python中自带 sorted 函数，对于简单的多字段排序问题可以使用 `key=lambda x:...`，对于一些需要自定义的排序问题，则可以重写 `__lt__` （速度慢）实现排序：

```python
class LargerNumKey(int):
    def __lt__(self, other):  # 重写小于号，所以不能用小于号
        return other > self

num_keyclass = sorted(num_keyclass, key=LargerNumKey)
```

或者 使用 `key=cmp_to_key(methodName)` （速度一般）的方法实现排序：

```python
from functools import cmp_to_key

def cmp(a, b): # -1: a 应该在前
    if a < b:  
        return -1
    elif a == b:
        return 0
    else:
        return 1

num_cmptokey = sorted(num_cmptokey, key=cmp_to_key(cmp))
```
对 100K 个数排序速度测试如下：
- 原始 `sort` 函数用时 0.14s
- 使用 `cmp` 函数用时 1.72s 
- 重写 `__lt__` 方法用时 3.09s

