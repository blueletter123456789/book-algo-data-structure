import bisect

n = int(input())
l = list(map(int, input().split()))
l2 = sorted(l)
ans = list()
for i in l:
    idx = bisect.bisect_left(l2, i)
    ans.append(str(idx))
print(' '.join(ans))
