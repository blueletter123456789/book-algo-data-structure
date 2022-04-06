"""
8 8
.#....#G
.#.#....
...#.##.
#.##...#
...###.#
.#.....#
...#.#..
S.......
"""
from collections import deque

h, w = map(int, input().split())
input_list = list()
al = [list() for _ in range(h*w)]

for _ in range(h):
    input_list.append(list(input()))
s = g = 0
for i in range(h):
    for j in range(w):
        tgt = input_list[i][j]
        tgt_idx = i*h + j
        if tgt == '#':
            continue
        if tgt == 'S':
            s = tgt_idx
        elif tgt == 'G':
            g = tgt_idx
        if i-1 >= 0 and input_list[i-1][j] != '#':
            al[tgt_idx].append((i-1)*h + j)
        if j+1 < w and input_list[i][j+1] != '#':
            al[tgt_idx].append(i*h + (j+1))
        if i+1 < h and input_list[i+1][j] != '#':
            al[tgt_idx].append((i+1)*h + j)
        if j-1 >= 0 and input_list[i][j-1] != '#':
            al[tgt_idx].append(i*h + (j-1))

dist = [-1]*(h*w)
que = deque([s])
dist[s] = 0
while len(que):
    current = que.popleft()
    for i in al[current]:
        if dist[i] != -1:
            continue
        dist[i] = dist[current]+1
        que.append(i)
print(dist[g])

""" sample source
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
h, w = map(int, input().split())
field = list()
for _ in range(h):
    field.append(list(input()))
sx = sy = gx = gy = -1
for i in range(h):
    for j in range(w):
        if field[i][j] == 'S':
            sx, sy = i, j
        elif field[i][j] == 'G':
            gx, gy = i, j

Q = deque([[sx, sy]])
dist = [[-1]*w for i in range(h)]
dist[sx][sy] = 0
while len(Q):
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if field[nx][ny] == '#':
            continue
        if dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y]+1
            Q.append([nx, ny])
print(dist[gx][gy])
"""
