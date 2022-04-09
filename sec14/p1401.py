import sys

sys.setrecursionlimit(10**6)

def dfs(current):
    seen[current] = True
    for i in al[current]:
        if seen[i]:
            continue
        dfs(i)
    order.append(current)

n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
order = list()
seen = [False]*n
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
order.reverse()
dp = [0]*n
for i in order:
    for j in al[i]:
        dp[j] = max(dp[j], dp[i]+1)
print(max(dp))

# sample code1 ###################
"""
import sys

sys.setrecursionlimit(10**6)

def rec(v):
    if s_dp[v] != -1:
        return s_dp[v]
    res = 0
    for nv in al[v]:
        res = max(res, rec(nv)+1)
    s_dp[v] = res
    return s_dp[v]

n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
s_dp = [-1]*n
res = 0
for v in range(n):
    res = max(res, rec(v))
print(res)
"""

# sample code2 ###################
"""
from collections import deque

n, m = map(int, input().split())
al = [list() for _ in range(n)]
deg = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    al[b-1].append(a-1)
    deg[a-1] += 1

dp = [0]*n
que = deque()
for i in range(n):
    if deg[i] == 0:
        que.append(i)

while len(que):
    v = que.popleft()
    for nv in al[v]:
        deg[nv] -= 1
        if deg[nv] == 0:
            que.append(nv)
            dp[nv] = max(dp[nv], dp[v]+1)
res = 0
for i in range(n):
    res = max(res, dp[i])
print(res)
"""
