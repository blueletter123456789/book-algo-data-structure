# TLE code
# INF = 10**4
# d_x = [0, 1, 0, -1]
# d_y = [1, 0, -1, 0]

# h, w = map(int, input().split())
# sx = sy = 0
# gx = gy = 0
# G = []
# for i in range(h):
#     G.append(list(input()))
#     for j in range(w):
#         if G[i][j] == 's':
#             sx, sy = i, j
#         if G[i][j] == 'g':
#             gx, gy = i, j

# dist = [[INF]*w for _ in range(h)]
# dist[sx][sy] = 0
# for n in range(h*w):
#     update  = False
#     for i in range(h):
#         for j in range(w):
#             for k in range(4):
#                 nx = i + d_x[k]
#                 ny = j + d_y[k]
#                 if 0 <= nx < h and 0 <= ny < w:
#                     if G[nx][ny] == '.' or (nx == gx and ny == gy):
#                         if dist[nx][ny] > dist[i][j]:
#                             dist[nx][ny] = dist[i][j]
#                             update = True
#                     else:
#                         if dist[nx][ny] > dist[i][j]:
#                             dist[nx][ny] = dist[i][j]+1
#                             update = True
#     if not update:
#         break
# if dist[gx][gy] <= 2:
#     print('YES')
# else:
#     print('NO')

from collections import deque

INF = 10**4
d_x = [0, 1, 0, -1]
d_y = [1, 0, -1, 0]

h, w = map(int, input().split())
sx = sy = 0
gx = gy = 0
G = []
for i in range(h):
    G.append(list(input()))
    for j in range(w):
        if G[i][j] == 's':
            sx, sy = i, j
        if G[i][j] == 'g':
            gx, gy = i, j

for i in range(1, 4):
    dist = [[INF]*w for _ in range(h)]
    dist[sx][sy] = 0
    que = deque([(sx, sy)])
    while len(que):
        cx, cy = que.popleft()
        for k in range(4):
            nx = cx + d_x[k]
            ny = cy + d_y[k]
            if 0 <= nx < h and 0 <= ny < w:
                if dist[nx][ny] != INF:
                    continue
                if nx == gx and ny == gy:
                    dist[nx][ny] = dist[cx][cy]
                    break
                if G[nx][ny] == '.':
                    dist[nx][ny] = min(dist[nx][ny], dist[cx][cy])
                    que.append((nx, ny))
                else:
                    dist[nx][ny] = min(dist[nx][ny], dist[cx][cy]+1)
    for n in range(h):
        for m in range(w):
            if dist[n][m] == 1:
                G[n][m] = '.'
if not dist[gx][gy]:
    print('YES')
else:
    print('NO')

# sample code ###########################################
from collections import deque

INF = 1 << 29
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]
sx = sy = gx = gy = -1
for i in range(h):
    for j in range(w):
        if field[i][j] == 's':
            sx, sy = i, j
        elif field[i][j] == 'g':
            gx, gy = i, j
que = deque([(sx, sy)])
dist = [[INF]*w for _ in range(h)]
dist[sx][sy] = 0
while len(que):
    x, y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if field[nx][ny] != '#':
            if dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                que.appendleft((nx, ny))
        else:
            if dist[nx][ny] > dist[x][y]+1:
                dist[nx][ny] = dist[x][y]+1
                que.append((nx, ny))

if dist[gx][gy] <= 2:
    print('YES')
else:
    print('NO')
