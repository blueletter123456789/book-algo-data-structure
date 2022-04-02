""" sample test
     7
    / \
  5     6
 / \   / \
1   2 3   4

7 6 7
7 5
7 6
5 1
5 2
6 3
6 4
"""
from collections import deque

n, m, s = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
    al[b-1].append(a-1)
seen = [False]*n

que = deque([s-1])
seen[s-1] = True
while len(que):
    current = que.popleft()
    print(current+1)
    for i in al[current]:
        if seen[i]:
            continue
        seen[i] = True
        que.append(i)
