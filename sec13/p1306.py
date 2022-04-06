def dfs(current):
    seen[current] = True
    for i in al[current]:
        if seen[i] and not finished[i]:
            return False
        res =  dfs(i)
        if not res:
            path.append(i)
        return res
    finished[current] = True
    return True


n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    al[a].append(b)    
flg = True
path = list()
for i in range(n):
    seen = [False]*n
    finished = [False]*n
    flg = dfs(i)
    if not flg:
        path.append(i)
        break
if flg:
    print('not cycle path')
else:
    print('cycle')
    path.reverse()
    print(path)
