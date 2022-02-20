n = int(input())
w = 10000
l = [0] + list(map(int, input().split()))
dp = [[False]*(w+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(1, n+1):
    for j in range(w+1):
        if dp[i-1][j]:
            dp[i][j] = True
        if dp[i-1][j-l[i]]:
            dp[i][j] = True
print(dp[n].count(True))
