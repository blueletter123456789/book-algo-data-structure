from collections import deque

INF = 10**9

k = int(input())
dist = [INF]*k
dist[1] = 1
que = deque([1])

while len(que):
    v = que.popleft()
    v2 = (v*10) % k
    if dist[v2] > dist[v]:
        dist[v2] = dist[v]
        que.appendleft(v2)
    v2 = (v+1) % k
    if dist[v2] > dist[v]:
        dist[v2] = dist[v] + 1
        que.append(v2)
print(dist[0])
