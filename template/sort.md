# sort template

## quick sort

```c++
template <typename T>
int Paritition(T A[], int low, int high) {
  int pivot = A[low];
  while (low < high) {
    while (low < high && pivot <= A[high]) --high;
    A[low] = A[high];
    while (low < high && A[low] <= pivot) ++low;
    A[high] = A[low];
  }
  A[low] = pivot;
  return low;
}
template <typename T>
void QuickSort(T A[], int low, int high) {
  if (low < high) {
    int pivot = Paritition(A, low, high);
    QuickSort(A, low, pivot - 1);
    QuickSort(A, pivot + 1, high);
  }
}
template <typename T>
void QuickSort(T A[], int len) {
  QuickSort(A, 0, len - 1);
}
```

## merge sort

```c++
void merge(const int *a, size_t aLen, const int *b, size_t bLen, int *c) {
  size_t i = 0, j = 0, k = 0;
  while (i < aLen && j < bLen) {
    // <!> 先判断 b[j] < a[i]，保证稳定性
    if (b[j] < a[i]) { c[k] = b[j]; ++j; /* 逆序对: cnt += aLen - i; */} 
    else { c[k] = a[i]; ++i; }
    ++k;
  }
  // 此时一个数组已空，另一个数组非空，将非空的数组并入 c 中
  for (; i < aLen; ++i, ++k) c[k] = a[i];
  for (; j < bLen; ++j, ++k) c[k] = b[j];
}

void merge_sort(int *a, int l, int r) {
  if (r - l <= 1) return;
  // 分解
  int mid = l + ((r - l) >> 1);
  merge_sort(a, l, mid), merge_sort(a, mid, r);
  // 合并
  int tmp[1024] = {};  // 请结合实际情况设置 tmp 数组的长度（与 a 相同），或使用
                       // vector；先将合并的结果放在 tmp 里，再返回到数组 a
  merge(a + l, a + mid, a + mid, a + r, tmp + l);  // pointer-style merge
  for (int i = l; i < r; ++i) a[i] = tmp[i];
}
```

## custom cmp function

```c++
struct data {
  int a, b;

  bool operator<(const data& rhs) const {
    return (a == rhs.a) ? (b < rhs.b) : (a < rhs.a);
  }
} da[1009];

// 在第一参数小于（即先序于）第二参数时返回 ​true
bool cmp(const data u1, const data u2) {
  return (u1.a == u2.a) ? (u1.b > u2.b) : (u1.a > u2.a);
}

// ...
std::sort(da + 1, da + 1 + 10);  // 使用结构体中定义的 < 运算符，从小到大排序
std::sort(da + 1, da + 1 + 10, cmp);  // 使用 cmp 函数进行比较，从大到小排序
std::stable_sort(da + 1, da + 1 + 10);  // 保证相等元素排序后的相对位置与原序列相同。
```