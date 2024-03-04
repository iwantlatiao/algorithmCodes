M, N = map(int, input().split())
school = list(map(int, input().split()))
student = list(map(int, input().split()))

ans = 0
i = 0
school.sort(), student.sort()
for stu in student:
    while i < len(school) and school[i] < stu:
        i += 1
    # 此时 school[i-1] < stu <= school[i]
    if i == 0:
        ans += school[i] - stu
    elif i == len(school):
        ans += stu - school[i - 1]
    else:
        ans += min(school[i] - stu, stu - school[i - 1])

print(ans)
