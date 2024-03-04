def check(x):
    i, j, cnt = 0, 1, 0
    while j < len(rock):
        if rock[j] - rock[i] < x:
            if cnt < M and j < len(rock) - 1:  # take j-th rock
                j += 1
                cnt += 1
            elif cnt < M and j == len(rock) - 1:  # take i-th rock
                break
            else:
                return False
        else:
            i = j
            j = i + 1
    return True


L, N, M = map(int, input().split())
rock = [0]
for _ in range(N):
    rock.append(int(input()))
rock.append(L)

l, r = 1, rock[len(rock) - 1]
while l < r:
    mid = (l + r) >> 1
    if check(mid):
        l = mid + 1
    else:
        r = mid

if check(l) == False:
    l -= 1

print(l)
