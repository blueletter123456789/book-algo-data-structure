n = int(input())
al = sorted(list(map(int, input().split())))
bl = sorted(list(map(int, input().split())))
ans = 0
i = j = 0
while i < n and j < n:
    if al[i] < bl[j]:
        ans += 1
        i += 1
    j += 1
print(ans)
