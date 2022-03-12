# n, k = map(int, input().split())
# al = sorted(list(map(int, input().split())))
# bl = sorted(list(map(int, input().split())))
# l = sorted([i*j for i in al for j in bl])
# print(l[k-1])

import bisect

n, k = map(int, input().split())
al = list(map(int, input().split()))
bl = sorted(list(map(int, input().split())))
max_num = al[n-1]*bl[n-1]
left, right = 0, 10**19
while right - left > 1:
    mid = (left+right)//2
    cnt = 0
    for i in range(n):
        cnt += bisect.bisect_right(bl, mid//al[i])
    if cnt >= k:
        right = mid
    else:
        left = mid
print(right)
