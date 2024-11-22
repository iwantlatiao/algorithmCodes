# 0x31 质数

## 质数的判定

### 试除法

对于整数 N ，扫描 2 到 根号 N 之间的所有整数，看能不能整除 N。如果都不能则 N 是质数，否则为合数。

```c++
bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0) return false;
    return true;
}
```

## 质数的筛选

### 埃氏筛法

思路：任意整数 x 的整数倍都不是质数。

时间复杂度为 `O(NloglogN)`

```c++
void primes(int n) {
    memset(v, 0, sizeof v);  // 合数标记
    for (int i = 2; i <= n; i++) {
        if (v[i]) continue;
        cout << i << endl;   // i 是质数
        for (int j = i; i * j <= n; j++) v[i * j] = 1;
    }
}
```

### 线性筛（欧拉筛）

虽然埃氏筛法从 `i*i` 开始标记合数，但是仍然会重复标记。例如 12 会被 2 和 3 标记，根本原因是没有确定出唯一产生 12 的方式。

线性筛通过记录每个数的最小质因子实现合数被唯一地筛出。线性筛的步骤如下：

1. 依次考虑 `2~N` 中的每个整数 i
2. 用数组 v 保存每个数的最小质因子。如果 `v[i] = 0` 说明 i 是质数，将其保存至质数数组 prime 中。
3. 扫描不大于 `v[i]` 的每个质数 p，由于 `p*i` 的最小质因子是 `p`，所以有 `v[i*p] = p`。

```c++
void primes(int n) {
    memset(v, 0, sizeof v)  // 最小质因数标记
    m = 0;  // 质数个数
    for (int i = 2; i <= n; i++) {
        if (v[i] == 0) { v[i] = i; prime[++m] = i; }  // i 是质数
        // 给当前的数 i 乘质因子 prime[j]
        for (int i = 1; i <= m; i++) {
            // prime[j] 不是 i 的最小质因子了，或者乘完超出范围
            if (prime[j] > v[i] || prime[j] * i > n) continue;
            v[prime[j] * i] = prime[j];
        }
    }
}
```

## 质因数分解

### 算数基本定理

任何一个大于 1 的正整数 N 都可以被唯一分解为有限个质数的乘积。

### 试除法

结合质数判定的试除法和埃氏筛法，可以扫描 2 到 根号 N 之间的所有整数 d，若 d 能整除 N，则从 N 中去掉所有 d。由于是从小到大扫，所以这些 d 一定都是质数。时间复杂度为 `O(sqrt(N))`

```c++
void divide(int n) {
    
}
```