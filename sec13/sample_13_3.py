"""
1-2-3 
|\  |
4-5-6-7 
|      \
8-9-10-11

11 13 1 11
1 2
2 3
1 4
1 5
4 5
5 6
6 7
4 8
3 6
7 11
8 9
9 10
10 11
"""

from collections import deque

n, m, s, g = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
    al[b-1].append(a-1)

dist = [-1]*n
que = deque([s-1])
dist[s-1] = 0
while len(que):
    current = que.popleft()
    for i in al[current]:
        if dist[i] != -1:
            continue
        dist[i] = dist[current]+1
        que.append(i)
print(dist[g-1])
