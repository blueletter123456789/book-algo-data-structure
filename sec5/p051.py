n = int(input())
dp = [[0]*(3) for _ in range(n+1)]
for i in range(1, n+1):
    l = list(map(int, input().split()))
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k]+l[j])
print(max(dp[n]))

######################################
n = int(input())
A = [0]*(n+1)
B = [0]*(n+1)
C = [0]*(n+1)
for i in range(1, n+1):
    a, b, c = map(int, input().split())
    A[i] = a+max(B[i-1], C[i-1])
    B[i] = b+max(A[i-1], C[i-1])
    C[i] = c+max(A[i-1], B[i-1])
print(max(A[n], B[n], C[n]))
