"""
"""
import sys

INF = sys.maxsize

n, m = map(int, input().split())
dp = [[INF]*(n) for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    dp[a][b] = w
for i in range(n):
    dp[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

is_negative_cycle = False
for i in range(n):
    if dp[i][i] < 0:
        is_negative_cycle = True
        break
if is_negative_cycle:
    print('negative cycle')
else:
    for i in range(n):
        out_row = list()
        for j in range(n):
            if dp[i][j] < INF/2:
                out_row.append(str(dp[i][j]))
            else:
                out_row.append('INF')
        print(' '.join(out_row))
