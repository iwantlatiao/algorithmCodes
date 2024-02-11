N, M = map(int, input().split())
ansSquare = 0
ansRectangle = int(N * M * (N + 1) * (M + 1) / 4)

for i in range(min(N, M)):
    ansSquare += (N - i) * (M - i)

print(ansSquare, ansRectangle - ansSquare, sep=" ")
