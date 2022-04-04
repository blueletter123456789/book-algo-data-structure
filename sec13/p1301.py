"""
4-2-9 1-6 0
| |/  |   |
3 5   7   8

10 8
4 3
4 2
2 5
2 9
5 9
1 7
1 6
0 8
"""
def dfs(current):
    seen_dfs[current] = True
    for i in al[current]:
        if seen_dfs[i]:
            continue
        dfs(i)
    
n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a].append(b)
    al[b].append(a)

seen_dfs = [False]*n
cnt_dfs = 0
for i in range(n):
    if seen_dfs[i]:
        continue
    dfs(i)
    cnt_dfs += 1

print(f'DFS: {cnt_dfs=}')
print('-------------------')

from collections import deque

seen_bfs = [False]*n
cnt_bfs = 0
for i in range(n):
    if seen_bfs[i]:
        continue
    que = deque([i])
    seen_bfs[i] = True
    while len(que):
        current = que.popleft()
        for j in al[current]:
            if seen_bfs[j]:
                continue
            seen_bfs[j] = True
            que.append(j)
    cnt_bfs += 1
print(f'BFS: {cnt_bfs=}')
