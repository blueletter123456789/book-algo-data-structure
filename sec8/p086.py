from collections import Counter

n, m = map(int, input().split())
nl = Counter(list(map(int, input().split())))
ml = list(map(int, input().split()))
ans = 0
for i in ml:
    ans += nl.get(i, 0)
print(ans)
