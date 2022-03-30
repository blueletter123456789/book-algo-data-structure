import heapq

n, k = map(int, input().split())
l = [-1*i for i in map(int, input().split())]
low = list(l[:k])
heapq.heapify(low)
print(-1*low[0])
for i in range(k, n):
    if low[0] < l[i]:
        heapq.heappop(low)
        heapq.heappush(low, l[i])
    print(-1*low[0])
