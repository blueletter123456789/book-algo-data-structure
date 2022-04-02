"""
1-2-3 
|\  |
4-5-6-7 
|      \
8-9-10-11

11 13 1 11
1 2
2 3
1 4
1 5
4 5
5 6
6 7
4 8
3 6
7 11
8 9
9 10
10 11
"""

def search_st_path(current, t):
    res = False
    seen[current] = True
    for i in al[current]:
        if i == t:
            res = True
            break
        elif seen[i]:
            continue
        res = search_st_path(i, t)
        if res:
            break
    return res

n, m, s, t = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
    al[b-1].append(a-1)
seen = [False]*n
if search_st_path(s-1, t-1):
    print('Yes')
else:
    print('No')
