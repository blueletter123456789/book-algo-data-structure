n = int(input())
w = int(input())
al = list(map(int, input().split()))

def calc_part(w, i, al):
    if i == 0:
        return w == 0 or w-al[i] == 0
    return calc_part(w, i-1, al) or calc_part(w-al[i], i-1, al)

if calc_part(w, n-1, al):
    print('Yes')
else:
    print('No')
