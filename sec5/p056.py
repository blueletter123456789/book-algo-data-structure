n, w = map(int, input().split())
A = list(map(int, input().split()))
M = list(map(int, input().split()))
L = list()
for i in range(n):
    L += [A[i]]*M[i]
n = len(L)
dp = [[False]*(w+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    for j in range(w+1):
        if dp[i][j]:
            dp[i+1][j] = True
        if j >= L[i] and dp[i][j-L[i]]:
            dp[i+1][j] = True
if dp[n][w]:
    print('Yes')
else:
    print('No')

print('################################')

n, w = map(int, input().split())
A = list(map(int, input().split()))
M = list(map(int, input().split()))
INF = 10**9
dp = [[INF]*(w+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(w+1):
        if dp[i][j] < INF:
            dp[i+1][j] = 0
        if j >= A[i] and dp[i+1][j-A[i]] < M[i]:
            dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-A[i]]+1)
if dp[n][w] < INF:
    print('Yes')
else:
    print('No')
