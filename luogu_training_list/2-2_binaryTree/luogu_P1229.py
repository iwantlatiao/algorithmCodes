pre = input()
post = input()
N = len(pre)

ans = 1
for i in range(N - 1):  # 最后一个肯定没有儿子
    j = post.find(pre[i])
    if j > 0 and post[j - 1] == pre[i + 1]:
        ans = ans << 1

print(ans)
