"""
      10
    /  | \
   7   8  9
 / |  / | | \
1  2 3  4 5  6

10
10 7
10 8
10 9
7 1
7 2
8 3
8 4
9 5
9 6
"""
def search_depth(current, dep, parent=-1):
    depth[current] = dep
    for i in al[current]:
        if i == parent:
            continue
        search_depth(i, dep+1, current)

n = int(input())
al = [list() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
depth = [0]*n

parent = 9
search_depth(parent, 0)
print(depth)
