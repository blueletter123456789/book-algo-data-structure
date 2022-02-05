n = int(input())
l = list(map(int, input().split()))
cnt = 0
while all([i%2==0 for i in l]):
    cnt += 1
    l = [i//2 for i in l]
print(cnt)


print('#################################')

from collections import defaultdict
import math
n = int(input())
l = list(map(int, input().split()))
d = defaultdict(int)
for i in l:
    cnt = 0
    tmp = i
    while tmp % 2 == 0:
        cnt += 1
        tmp /= 2
    d[i] = cnt
print(d[min(d.keys())])
