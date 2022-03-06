# s = list(input())
# t = list(input())
# INF = 10 ** 9
# dp = [[INF]*(len(t)+1) for _ in range(len(s)+1)]
# dp[0][0] = 0
# for i in range(len(s)+1):
#     for j in range(len(t)+1):
#         if i > 0 and j > 0:
#             if s[i-1] == t[j-1]:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j-1])
#             else:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
#         if i > 0:
#             dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
#         if j > 0:
#             dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
# print('  ', '  '.join(t))
# for i in range(len(dp)):
#     print(dp[i])


s = list(input())
t = list(input())
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

ans = ''
i = len(t)
j = len(s)
while i > 0 and j > 0:
    if dp[j][i] == dp[j-1][i]:
        j -= 1
    elif dp[j][i] > dp[j][i-1]:
        ans = t[i-1] + ans
        i -= 1
        j -= 1
    else:
        i -= 1
print(ans)
