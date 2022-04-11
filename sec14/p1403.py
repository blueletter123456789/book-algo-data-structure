# def dfs(current):
#     seen[current] = True
#     for i in al[current]:
#         if seen[i] and not finished[i]:
#             return False
#         res = dfs(i)
#         if not res:
#             path.append(i)
#         return res
#     finished[current] = True
#     return True

# n, m = map(int, input().split())
# al = [list() for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     al[a-1].append(b-1)
# s, t = map(int, input().split())
# seen = [False]*n
# finished = [False]*n
# path = list()
# res = dfs(s-1)
# if not res:
#     path.append(s-1)
#     path.reverse()
#     print(path)

from collections import deque

n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = [i-1 for i in map(int, input().split())]
    al[a].append(b)
s, t = [i-1 for i in map(int, input().split())]

dist = [[-1]*3 for _ in range(n)]

dist[s][0] = 0
que = deque([(s, 0)])
while len(que):
    v, p = que.popleft()
    for i in al[v]:
        np = (p+1)%3
        if dist[i][np] == -1:
            dist[i][np] = dist[v][p]+1
            que.append((i, np))

if dist[t][0] == -1:
    print(-1)
else:
    print(dist[t][0]//3)
