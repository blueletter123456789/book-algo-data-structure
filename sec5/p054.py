n = int(input())
w, k = map(int, input().split())
INF = 10 ** 9
l = [INF] + list(map(int, input().split()))
dp = [[INF]*(w+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    for j in range(w+1):
        if j < l[i]:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-l[i]]+1)
if dp[i][j] <= k:
    print('Yes')
else:
    print('No')
