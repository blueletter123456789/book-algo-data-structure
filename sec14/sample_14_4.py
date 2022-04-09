"""
"""
import heapq
import sys

INF = sys.maxsize

n, m, s = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    al[a].append((b, w))

dist = [INF]*n
dist[s] = 0
que = [(dist[s], s)]
heapq.heapify(que)
while len(que):
    cur_dist, cur_v = heapq.heappop(que)
    if cur_dist > dist[cur_v]:
        continue
    for v, weight in al[cur_v]:
        tmp_dis = dist[cur_v] + weight
        if dist[v] > tmp_dis:
            dist[v] = tmp_dis
            heapq.heappush(que, (tmp_dis, v))

for k, v in enumerate(dist):
    print(f'{k}: {v}' if v < INF else f'{k}: INF')
