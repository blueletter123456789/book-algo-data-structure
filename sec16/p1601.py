class Edge(object):
    def __init__(self, a, b, r, c=1):
        self.fro = a
        self.to = b
        self.rev = r
        self.cap = c

class Graph(object):
    def __init__(self, n):
        self.lst = [list() for _ in range(n)]
    
    def __getitem__(self, key):
        return self.lst[key]
    
    def __len__(self):
        return len(self.lst)
    
    def redge(self, edge):
        return self.lst[edge.to][edge.rev]
    
    def run_flow(self, edge, f=1):
        edge.cap -= f
        self.redge(edge).cap += f
    
    def add_edge(self, fro, to, cap=1):
        fro_idx = len(self.lst[fro])
        to_idx = len(self.lst[to])
        self.lst[fro].append(Edge(fro, to, to_idx))
        self.lst[to].append(Edge(to, fro, fro_idx))

class FordFullkurson(object):
    INF = 1 << 16
    def __init__(self, p):
        self.seen = list()
        self.p = p
    
    def fodfs(self, G, v, f):
        if v in self.p:
            self.p.remove(v)
            return f
        self.seen[v] = True
        for edge in G[v]:
            if self.seen[edge.to]:
                continue
            if edge.cap == 0:
                continue
            flow = self.fodfs(G, edge.to, min(f, edge.cap))
            if flow == 0:
                continue
            G.run_flow(edge)
            return flow
        return 0

    def solved(self, G, s):
        res = 0
        while True:
            self.seen = [False]*len(G)
            flow = self.fodfs(G, s, self.INF)
            if flow == 0:
                return res
            res += flow
    
n, g, e = map(int, input().split())
p = {int(i) for i in input().split()}
G = Graph(n)
for _ in range(e):
    a, b = map(int, input().split())
    G.add_edge(a, b)
ff = FordFullkurson(p)
res = ff.solved(G, 0)
print(res)

""" smaple source
class Edge(object):
    def __init__(self, a, b, r, c):
        self.fro = a
        self.to = b
        self.rev = r
        self.cap = c

class Graph(object):
    def __init__(self, n):
        self.lst = [list() for _ in range(n)]
    
    def __getitem__(self, key):
        return self.lst[key]
    
    def __len__(self):
        return len(self.lst)
    
    def redge(self, edge):
        return self.lst[edge.to][edge.rev]
    
    def run_flow(self, edge, f=1):
        edge.cap -= f
        self.redge(edge).cap += f
    
    def add_edge(self, fro, to, cap=1):
        fro_idx = len(self.lst[fro])
        to_idx = len(self.lst[to])
        self.lst[fro].append(Edge(fro, to, to_idx, cap))
        self.lst[to].append(Edge(to, fro, fro_idx, 0))

class FordFullkurson(object):
    INF = 1 << 16
    def __init__(self):
        self.seen = list()
    
    def fodfs(self, G, v, t, f):
        if v == t:
            return f
        self.seen[v] = True
        for edge in G[v]:
            if self.seen[edge.to]:
                continue
            if edge.cap == 0:
                continue
            flow = self.fodfs(G, edge.to, t, min(f, edge.cap))
            if flow == 0:
                continue
            G.run_flow(edge)
            return flow
        return 0

    def solved(self, G, s, t):
        res = 0
        while True:
            self.seen = [False]*len(G)
            flow = self.fodfs(G, s, t, self.INF)
            if flow == 0:
                return res
            res += flow
    
n, g, e = map(int, input().split())
T = list(map(int, input().split()))
G = Graph(n+1)
for _ in range(e):
    a, b = map(int, input().split())
    G.add_edge(a, b)
    G.add_edge(b, a)
for t in T:
    G.add_edge(t, n)
    G.add_edge(n, t)
ff = FordFullkurson()
res = ff.solved(G, 0, n)
print(res)
"""
