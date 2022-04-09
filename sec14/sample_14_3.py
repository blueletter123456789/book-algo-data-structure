"""
6 9 0
0 1 3
0 2 5
1 2 4
1 3 12
2 4 4
2 3 9
4 3 7
3 5 2
4 5 8
"""
import sys

INF = sys.maxsize

n, m, s = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    al[a].append((b, w))

used = set()
dist = [INF]*n
dist[s] = 0
for i in range(n):
    min_dist = INF
    min_v = -1
    for j in range(n):
        if j not in used and dist[j] < min_dist:
            min_dist = dist[j]
            min_v = j
    
    if min_v == -1:
        break
    
    for v, weight in al[min_v]:
        dist[v] = min(dist[v], dist[min_v]+weight)
    used.add(min_v)

for k, v in enumerate(dist):
    print(f'{k}: {v}' if v < INF else f'{k}: INF')
