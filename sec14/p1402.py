INF = float('INF')
n, m = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    al[a-1].append((b-1, -c))
dist = [INF]*n
dist[0] = 0
is_cycle = False
cnt = min(n*(n+1), 2000)
for i in range(cnt):
    update = False
    ans_n = dist[-1]
    for j in range(n):
        if dist[j] == INF:
            continue
        for v, weight in al[j]:
            tmp = dist[j]+weight
            if dist[v] > tmp:
                dist[v] = tmp
                update = True
    if not update:
        break
    # nに対して関係のない負閉路は除外
    if i == n-1 and ans_n != dist[-1]:
        is_cycle = True
        break
if is_cycle:
    print('inf')
else:
    print(-dist[n-1])
