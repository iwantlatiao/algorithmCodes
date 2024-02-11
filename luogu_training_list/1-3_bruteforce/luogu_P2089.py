# search(第k种调料 放的质量 总质量)
def search(k, w, total):
    solution[k] = w
    if k == M:
        if total == N:
            global ans
            ans += 1
            ansSolution.append(solution[1:].copy())
        return
    if total > N:
        return
    for i in range(1, 3 + 1):
        search(k + 1, i, total + i)


N = int(input())
M = 10  # 调料个数
ans = 0
solution = [0 for _ in range(M + 1)]
ansSolution = []
if N < M or M * 3 < N:
    print("0")
else:
    for i in range(1, 3 + 1):
        search(1, i, i)

    print(ans)
    for i in range(ans):
        for j in range(M):
            print(ansSolution[i][j], end=" ")
        print("")
