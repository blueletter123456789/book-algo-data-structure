from collections import deque

# 有効グラフを前提に作成
n, m, s, t = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
dist = [-1]*n
que = deque([s-1])
dist[s-1] = 0
flg = False
while len(que):
    current = que.popleft()
    for i in al[current]:
        if i == t-1:
            flg = True
            break
        elif dist[i] != -1:
            continue
        dist[current] += 1
        que.append(i)

# 最短経路を求め、解答のコードはdist[t]!=-1で判定
if flg:
    print('Yes')
else:
    print('No')
