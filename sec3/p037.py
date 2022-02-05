s = input()
sl = list(s)
idx = len(sl)-1
sig_map = []
for i in range(1 << idx):
    tmp = sl[0]
    for j in range(idx):
        if i & (1 << j):
            tmp += '+'
        tmp += sl[j+1]
    sig_map.append(eval(tmp))
print(sum(sig_map))

print('##########################')

s = input()
sl = [int(i) for i in s]
idx = len(sl)-1
res = 0
for i in range(1 << idx):
    tmp = sl[0]
    for j in range(idx):
        if i & (1 << j):
            res += tmp
            tmp = sl[j+1]
        else:
            tmp *= 10
            tmp += sl[j+1]
    res += tmp
print(res)
