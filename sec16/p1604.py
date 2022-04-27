import sys
from collections import defaultdict

sys.setrecursionlimit(10000000)


class Edge:
    def __init__(self, f, t, r, c):
        self.fro = f
        self.to = t
        self.rev = r
        self.cap = c

class Graph:
    def __init__(self, n):
        self.lst = [list() for _ in range(n)]
    
    def __getitem__(self, key):
        return self.lst[key]
    
    def __len__(self):
        return len(self.lst)
    
    def redge(self, edge):
        return self.lst[edge.to][edge.rev]
    
    def run_flow(self, edge, f):
        edge.cap -= 1
        self.redge(edge).cap += f
    
    def add_edge(self, u, v, c=1):
        fro_rev = len(self.lst[u])
        to_rev = len(self.lst[v])
        self.lst[u].append(Edge(u, v, to_rev, c))
        self.lst[v].append(Edge(v, u, fro_rev, 0))

class FordFulkerson:
    INF = 1 << 15
    def __init__(self):
        self.seen = list()
    
    def fod_fs(self, G, v, t, f):
        if v == t:
            return f
        self.seen[v] = True
        for e in G[v]:
            if self.seen[e.to]:
                continue
            if e.cap == 0:
                continue
            flow = self.fod_fs(G, e.to, t, min(f, e.cap))
            if flow == 0:
                continue
            G.run_flow(e, flow)
            return flow
        return 0
    
    def solved(self, G, s, t):
        res = 0
        while True:
            self.seen = [False]*len(G)
            flow = self.fod_fs(G, s, t, self.INF)
            if flow == 0:
                return res
            res += flow

ca = defaultdict(dict)
def my_cache(func):
    def _inner(a, b):
        ans = 0
        a, b = max(a, b), min(a, b)
        if b in ca[a]:
            ans = ca[a][b]
        if not ans:
            ans = func(a, b)
            ca[a][b] = ans
        return ans
    return _inner

@my_cache
def gcd(a, b):
    if b in ca[a]:
        return ca[a][b]
    if b == 0:
        return a
    return gcd(b, a%b)

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    b = list()
    r = list()
    while True:
        b += list(map(int, input().split()))
        if len(b) == m:
            break
    while True:
        r += list(map(int, input().split()))
        if len(r) == n:
            break

    s, t = 0, n+m+1
    G = Graph(t+1)
    for i in range(m):
        G.add_edge(s, i+1)
    for i in range(n):
        G.add_edge(m+i+1, t)
    for i in range(m):
        for j in range(n):
            if gcd(b[i], r[j]) > 1:
                G.add_edge(i+1, m+j+1)
    ff = FordFulkerson()
    print(ff.solved(G, s, t))
