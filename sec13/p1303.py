from collections import deque

n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
    al[b-1].append(a-1)

colors = [-1]*n
flg = True
for i in range(n):
    if colors[i] != -1:
        continue
    que = deque([i])
    colors[i] = 0
    while len(que):
        current = que.popleft()
        for i in al[current]:
            if colors[i] != -1:
                if colors[i] == colors[current]:
                    flg = False
                    break
                else:
                    continue
            colors[i] = 1-colors[current]
            que.append(i)

if flg:
    print('Yes')
else:
    print('No')
