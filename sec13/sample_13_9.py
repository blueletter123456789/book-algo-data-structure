"""
9-8
|
1 5-6
|/
0-3
|\
2 4-7

10
0 1
0 2
0 3
0 4
0 5
1 9
4 7
5 6
9 8
"""

def dfs(current, dep, parent=-1):
    depth[current] = dep
    for i in al[current]:
        if i == parent:
            continue
        dfs(i, dep+1, current)
    sub_size[current] = 1
    for i in al[current]:
        if i == parent:
            continue
        sub_size[current] += sub_size[i]

n = int(input())
al = [list() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    al[a].append(b)
    al[b].append(a)

depth = [0]*n
sub_size = [0]*n
root = 0
dfs(root, 0)
for i in range(n):
    print(f'{i=}: {depth[i]=}, {sub_size[i]=}')
