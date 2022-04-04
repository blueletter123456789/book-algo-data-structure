""" sample test
4-2-----
|\ \   |
| 6-7  |
|/ /|  |
1-3-0--5

8 12
0 5
1 3
1 6
2 5
2 7
3 0
3 7
4 1
4 2
4 6
7 7
7 0
"""
def dfs(tgt):
    seen[tgt] = True
    # print('-行きがけ順--', tgt)
    for i in al[tgt]:
        if seen[i]:
            continue
        dfs(i)
    # print('#帰りがけ順##', tgt)
    order_topo.append(tgt)

n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a].append(b)

order_topo = list()
seen = [False]*n
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
order_topo.reverse()
print(order_topo)
