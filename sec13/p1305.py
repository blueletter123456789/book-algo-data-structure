"""
8 12
4 1
4 6
4 2
1 6
6 7
1 3
2 7
3 0
3 7
7 0
2 5
0 5
"""
from collections import deque

n, m = map(int, input().split())
al = [list() for _ in range(n)]
deg = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    al[b].append(a)
    deg[a] += 1

que = deque([])
for i in range(n):
    if deg[i] == 0:
        que.append(i)
order = list()
while len(que):
    current = que.popleft()
    order.append(current)
    for i in al[current]:
        deg[i] -= 1
        if deg[i] == 0:
            que.append(i)
order.reverse()
print(order)
