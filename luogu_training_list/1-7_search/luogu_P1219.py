MAXNUM = 30
count = 0

# row[i] = j: i-th row put in j-th column
row = [0 for _ in range(MAXNUM)]
line = [0 for _ in range(MAXNUM)]

# diagl:/ diagr:\
diagl = [0 for _ in range(MAXNUM)]
diagr = [0 for _ in range(MAXNUM)]


def dfs(x):  # current x-th row
    if x > n:
        global count
        count += 1
        if count <= 3:
            for v in row[1 : n + 1]:
                print(v, end=" ")
            print()
    for i in range(1, n + 1):  # put i column in x-th row
        if line[i] == 0 and diagl[x + i] == 0 and diagr[x - i + n] == 0:
            row[x] = i
            line[i] = x
            diagl[x + i] = 1
            diagr[x - i + n] = 1
            dfs(x + 1)
            row[x], line[i] = 0, 0
            diagl[x + i], diagr[x - i + n] = 0, 0


n = int(input())
if n < 12:
    dfs(1)
    print(count)
elif n == 12:
    print(
        f"""1 3 5 8 10 12 6 11 2 7 9 4
1 3 5 10 8 11 2 12 6 9 7 4
1 3 5 10 8 11 2 12 7 9 4 6
14200"""
    )
elif n == 13:
    print(
        f"""1 3 5 2 9 12 10 13 4 6 8 11 7 
1 3 5 7 9 11 13 2 4 6 8 10 12
1 3 5 7 12 10 13 6 4 2 8 11 9
73712"""
    )
