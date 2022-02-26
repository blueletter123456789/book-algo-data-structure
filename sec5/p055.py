n, w = map(int, input().split())
l = list(map(int, input().split()))
dp = [False] * (w+1)
dp[0] = True
for i in range(1, w+1):
    for j in l:
        if i < j:
            continue
        if dp[i-j]:
            dp[i] = True
if dp[w]:
    print('Yes')
else:
    print('No')

print('##################################')

n, w = map(int, input().split())
l = list(map(int, input().split()))
dp = [[False]*(w+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    for j in range(w+1):
        if dp[i][j]:
            dp[i+1][j] = True
        if j >= l[i] and dp[i+1][j-l[i]]:
            dp[i+1][j] = True
if dp[n][w]:
    print('Yes')
else:
    print('No')
