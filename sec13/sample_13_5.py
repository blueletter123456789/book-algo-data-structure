"""
1 2 3	1 2-3	1 2 3 6
|X /	|X /	|X /  |
4 5		4 5		4 5   7

5 4		5 5		7 5
1 4		1 4		1 4
1 5		1 5		1 5
2 4		2 4		2 4
3 5		3 5		3 5
		2 3		6 7
"""
def dfs(current, current_color):
    colors[current] = current_color
    seen[current] = True
    res = True
    for i in al[current]:
        if seen[i]:
            if colors[i] == current_color:
                res = False
                break
            else:
                continue
        res = dfs(i, not current_color)
        if not res:
            break
    return res

n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
    al[b-1].append(a-1)

ans = True
colors = [False]*n
seen = [False]*n
for i in range(n):
    if seen[i]:
        continue
    if not dfs(i, True):
        ans = False
        break
if ans:
    print('Yes')
else:
    print('No')


# sample code ####################################
def dfs_sample(v, cur=0):
    color[v] = cur
    for next_v in al[v]:
        if color[next_v] != -1:
            if color[next_v] == cur:
                return False
            continue
        if not dfs_sample(next_v, 1-cur):
            return False
    return True

color = [-1]*n
is_bipartite = True
for v in range(n):
    if color[v] != -1:
        continue
    if not dfs_sample(v):
        is_bipartite = False

if is_bipartite:
    print('Yes')
else:
    print('No')
