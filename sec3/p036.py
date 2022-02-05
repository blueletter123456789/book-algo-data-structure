k, s = map(int, input().split())
cnt = 0
for i in range(k+1):
    for j in range(k+1):
        h = s-i+j
        if 0 <= h <= k:
            cnt += 1
print(cnt)
