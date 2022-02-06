from collections import defaultdict
from copy import copy

def pattern(n, i, pat):
    if n < i:
        pat[i] = {-1}
        return
    j = i * 10
    pat[j+3] = copy(pat[i])
    pat[j+5] = copy(pat[i])
    pat[j+7] = copy(pat[i])
    pat[j+3].add(3)
    pat[j+5].add(5)
    pat[j+7].add(7)
    pattern(n, j+3, pat)
    pattern(n, j+5, pat)
    pattern(n, j+7, pat)

n = int(input())
pat = defaultdict(set)
pat[0] = set()

pattern(n, 0, pat)
cnt = 0
for k, v in pat.items():
    if len(v) == 3:
        cnt += 1
print(cnt)

