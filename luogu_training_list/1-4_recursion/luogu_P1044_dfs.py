MAXNUM = 20
f = [[0 for _ in range(MAXNUM)] for _ in range(MAXNUM)]


# i: unchecked num, j: instack num
def search(i, j):
    if f[i][j] != 0:
        return f[i][j]
    if i == 0:
        f[i][j] = 1
    elif j == 0:  # stack is empty
        f[i][j] = search(i - 1, j + 1)
    else:  # stack is not empty
        f[i][j] = search(i - 1, j + 1) + search(i, j - 1)
    return f[i][j]


N = int(input())
print(search(N, 0))
