class Edge(object):
    def __init__(self, r, f, t, c) -> None:
        self.rev = r
        self.fro = f
        self.to = t
        self.cap = c

class Graph():
    def __init__(self, n):
        self.lst = [list() for _ in range(n)]
    
    def __getitem__(self, key):
        return self.lst[key]
    
    def __len__(self):
        return len(self.lst)
    
    def redge(self, e):
        return self.lst[e.to][e.rev]
    
    def run_flow(self, e, f):
        e.cap -= f
        self.redge(e).cap += f
    
    def add_edge(self, f, t, c):
        from_rev = len(self.lst[f])
        to_rev = len(self.lst[t])
        self.lst[f].append(Edge(to_rev, f, t, c))
        self.lst[t].append(Edge(from_rev, f, t, c))

class FordFulkurson():
    INF = 1 << 30
    
    def __init__(self) -> None:
        self.seen = list()
    
    def fodfs(self, G, v, t, f=None):
        if not f:
            f = self.INF
        if v == t:
            return f
        self.seen[v] = True
        for e in G[v]:
            if self.seen[e.to]:
                continue
            if e.cap == 0:
                continue
            flow = self.fodfs(G, e.to, t, min(f, e.cap))
            if flow == 0:
                continue
            G.run_flow(e, flow)
            return flow
        return 0
    
    def solved(self, G, s, t):
        res = 0
        while True:
            self.seen = [False] * len(G)
            flow = self.fodfs(G, s, t)
            if flow == 0:
                return res
            res += flow

n, m = map(int, input().split())
s, t = 0, n-1
G = Graph(n)
for _ in range(m):
    u, v, c = map(int, input().split())
    G.add_edge(u, v, c)
ff = FordFulkurson()
print(ff.solved(G, s, t))
