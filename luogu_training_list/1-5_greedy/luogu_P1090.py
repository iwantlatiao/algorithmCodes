from queue import PriorityQueue as PQ

pq = PQ()

N = int(input())
l = list(map(int, input().split()))
if N == 1:
    print(l[0])
    exit(0)

for i in range(N):
    pq.put(l[i])

ans = 0
a = pq.get()
while not pq.empty():
    b = pq.get()
    sum = a + b
    ans += sum
    pq.put(sum)
    a = pq.get()

print(ans)
