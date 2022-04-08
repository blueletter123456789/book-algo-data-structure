"""
6 12 0
0 1 3
0 3 100
1 2 50
1 3 57
1 4 -4
2 3 -10
2 4 57
2 5 100
3 1 -5
4 2 57
4 3 25
4 5 8
"""
import sys

INF = sys.maxsize

n, m, s = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    al[a].append((b, w))

is_negative_cycle = False
dist = [INF]*n
dist[s] = 0
for i in range(n):
    update = False
    for current in range(n):
        if dist[current] == INF:
            continue
        for to, weight in al[current]:
            cnt = dist[current] + weight
            if dist[to] > cnt:
                dist[to] = cnt
                update = True
    if not update:
        break
    print(dist)
    if i == n-1 and update:
        is_negative_cycle = True
        break

if is_negative_cycle:
    print('negative cycle')
else:
    for i in range(n):
        print(dist[i] if dist[i] < INF else 'INF')
