facing = []
job = []
currentPosition = 0
direction = 1

n, m = map(int, input().split())

for _ in range(n):
    x, s = input().split()
    facing.append(int(x))
    job.append(s)

for _ in range(m):
    a, s = map(int, input().split())
    if a == facing[currentPosition]:  # a=0, facing=0 or a=1, facing=1
        direction = -1
    else:
        direction = 1
    currentPosition = (currentPosition + direction * s) % n

print(job[currentPosition])
