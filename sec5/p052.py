n = int(input())
w = int(input())
l = [0] + list(map(int, input().split()))
dp = [[0]*(w+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(w+1):
        if l[i] > j:
            dp[i][j] = dp[i-1][j]
            continue
        elif l[i] == j:
            dp[i][j] = dp[i-1][j] + 1
        elif dp[i-1][j-l[i]]:
            dp[i][j] = dp[i-1][j-l[i]]
        dp[i][j] += dp[i-1][j]
print(dp)
if dp[i][w]:
    print('Yes')
else:
    print('No')
