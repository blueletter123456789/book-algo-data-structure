n, m = map(int, input().split())
nl = set(map(int, input().split()))
ml = list(map(int, input().split()))
count_num = 0
for i in ml:
    if i in nl:
        count_num += 1
print(count_num)
