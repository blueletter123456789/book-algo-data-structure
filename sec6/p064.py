n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
l.sort()
print(l)
left, right = 0, 10**10
while right - left > 1:
    mid = (left+right)//2
    prev = 0
    cnt = 1
    for i in range(1, n):
        if (l[i]-l[prev]) >= mid:
            cnt += 1
            prev = i
    if cnt >= m:
        left = mid
    else:
        right = mid
print(left)
