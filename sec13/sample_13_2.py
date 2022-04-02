""" sample test
     7
    / \
  5     6
 / \   / \
1   2 3   4

7 6 7
7 5
7 6
5 1
5 2
6 3
6 4
"""
def dfs(tgt):
    seen[tgt] = True
    print('-行きがけ順--', tgt+1)
    for i in al[tgt]:
        if seen[i]:
            continue
        dfs(i)
    print('#帰りがけ順##', tgt+1)

n, m, s = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
    al[b-1].append(a-1)

seen = [False]*n
dfs(s-1)
