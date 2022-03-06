def avg_num(a, b):
    res = 0
    for i in range(a, b):
        res += al[i]
    return res / (b - a)

n, m = map(int, input().split())
al = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
c = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i):
        c[j][i] = avg_num(j, i)

for i in range(n+1):
    for j in range(i):
        for k in range(1, m+1):
            dp[i][k] = max(dp[i][k], dp[j][k-1]+c[j][i])
print(max(dp[n]))
