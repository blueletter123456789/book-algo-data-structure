n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()
ans = 0
i = 0
while m > 0:
    tmp = m
    m -= l[i][1]
    if m >= 0:
        ans += l[i][0]*l[i][1]
    else:
        ans += l[i][0]*tmp
    i += 1
print(ans)
