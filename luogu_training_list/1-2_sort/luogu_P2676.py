def merge(a, b):
    i, j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        # <!> 先判断 b[j] < a[i]，保证排序的稳定性
        if b[j] < a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    # 此时一个数组已空，另一个数组非空，将非空的数组并入 c 中
    c.extend(a[i:])
    c.extend(b[j:])
    return c


def merge_sort(a, ll, rr):  # [l, r)
    if rr - ll <= 1:
        return
    # 分解
    mid = (rr + ll) >> 1
    merge_sort(a, ll, mid)  # [l,mid)
    merge_sort(a, mid, rr)  # [mid, r)
    # 合并
    a[ll:rr] = merge(a[ll:mid], a[mid:rr])


N, B = map(int, input().split())
num = []
for _ in range(N):
    num.append(int(input()))
merge_sort(num, 0, N)

ans = 0
for i in range(N - 1, -1, -1):
    ans += num[i]
    if ans >= B:
        print(N - i)
        exit(0)
