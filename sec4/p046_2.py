n = int(input())
w = int(input())
al = list(map(int, input().split()))

numcache = [[-1]*(w+1) for _ in range(n)]

def calc_part(w, i, al):
    if i == 0:
        return 1 if w == 0 or w-al[i] == 0 else 0
    if numcache[i][w] != -1:
        res = numcache[i][w]
    else:
        res = calc_part(w, i-1, al) or calc_part(w-al[i], i-1, al)
        numcache[i][w] = res
    return res

if calc_part(w, n-1, al) == 1:
    print('Yes')
else:
    print('No')
