n = int(input())
num = []

for i in range(n):
    num.append([input(), i])

snum = sorted(num, key=lambda x: (len(x[0]), x[0]), reverse=True)

print(snum[0][1] + 1)
print(snum[0][0])
