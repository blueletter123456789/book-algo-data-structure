l = list(map(int, input().split()))

min1, min2 = min(l[0], l[1]), max(l[0], l[1])
for i in range(2, len(l)):
    if l[i] < min1:
        min1, min2 = l[i], min1
    elif l[i] < min2:
        min2 = l[i]

print(min2)
