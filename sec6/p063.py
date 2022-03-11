# 全探索
# n, m = map(int, input().split())
# l = [int(input()) for _ in range(n)]
# ans = 0
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             for o in range(n):
#                 num = l[i]+l[j]+l[k]+l[o]
#                 if num <= m:
#                     ans = max(ans, num)

import bisect

n, m = map(int, input().split())
l = [0] + [int(input()) for _ in range(n)]
ans = 0
l2 = sorted([i+j for i in l for j in l])
for i in l2:
    tmp = 0
    if i <= m:
        tmp = i
        target = m - i
        if target > 0:
            j = bisect.bisect_right(l2, target)
            tmp += l2[j-1]
    ans = max(ans, tmp)
print(ans)
