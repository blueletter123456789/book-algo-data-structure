n = int(input())
al = list(map(int, input().split()))
sl = [0]*(n+1)
for i in range(n):
    sl[i+1] = sl[i]+al[i]

INF = 10**15
dp = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n):
    dp[i][i+1] = 0

for t in range(2, n+1):
    i = 0
    while t + i <= n:
        j = i + t
        for k in range(i+1, j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+sl[j]-sl[i])
        i += 1
print(dp[0][n])
