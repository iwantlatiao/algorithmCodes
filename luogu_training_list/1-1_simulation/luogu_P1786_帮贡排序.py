family = []
n = int(input())
for i in range(n):
    name, job, bangg, level = input().split()
    family.append([name, job, int(bangg), int(level), i])

# 跳过帮主和副帮主
for i in range(3):
    print(family[i][0], family[i][1], family[i][3])

# 按帮贡降序 输入顺序升序排序
s1family = sorted(family[3:], key=lambda x: (-x[2], x[4]))

for i in range(n - 3):
    if i == 0 or i == 1:
        s1family[i][1] = "HuFa"
    elif 2 <= i and i <= 5:
        s1family[i][1] = "ZhangLao"
    elif 6 <= i and i <= 12:
        s1family[i][1] = "TangZhu"
    elif 13 <= i and i <= 37:
        s1family[i][1] = "JingYing"
    else:
        s1family[i][1] = "BangZhong"

job2num = {
    "BangZhu": 1,
    "FuBangZhu": 2,
    "HuFa": 3,
    "ZhangLao": 4,
    "TangZhu": 5,
    "JingYing": 6,
    "BangZhong": 7,
}

# 按职位和等级降序 输入顺序升序排序
s2family = sorted(s1family, key=lambda x: (job2num[x[1]], -x[3], x[4]))

for i in range(n - 3):
    print(s2family[i][0], s2family[i][1], s2family[i][3])
