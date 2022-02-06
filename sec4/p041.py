from collections import defaultdict

n = int(input())

def tribo(n, c):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    tmp = c.get(n, None)
    if tmp:
        return tmp
    res = tribo(n-3, c)+ tribo(n-2, c) + tribo(n-1, c)
    c[n] = res
    return res

d = defaultdict(int)
print(tribo(n, d))
