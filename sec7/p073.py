n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort(key=lambda x: x[1])
ans = 0
flg = True
for i in range(n):
    ans += l[i][0]
    if ans > l[i][1]:
        flg = False
        break
if flg:
    print('Yes')
else:
    print('No')
