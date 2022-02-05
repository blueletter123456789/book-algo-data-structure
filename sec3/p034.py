l = list(map(int, input().split()))
min_num = max_num = l[0]
for i in range(1, len(l)):
    if l[i] < min_num:
        min_num = l[i]
    elif l[i] > max_num:
        max_num = l[i]
print(max_num - min_num)
