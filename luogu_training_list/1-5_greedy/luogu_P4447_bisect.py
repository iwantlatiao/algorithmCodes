from bisect import bisect


MAXNUM = 100000
N = int(input())
a = list(map(int, input().split()))
a.sort()

# team = [[下一个队员的实力, 目前人数]]
# team 在构造的过程中肯定是升序的
team = [[a[0] + 1, 1]]
for x in a[1:]:
    i = bisect(team, x, key=lambda x: x[0])
    i -= 1
    if i < 0:
        team.append([x + 1, 1])
    elif team[i][0] != x:  # 当前的队伍都放不了
        team.append([x + 1, 1])
    else:
        team[i][0] = x + 1
        team[i][1] += 1

ans = min(team, key=lambda x: x[1])
print(ans[1])
