class Edge(object):
    def __init__(self, u, v, r, c):
        self.fro = u
        self.to = v
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
    
    def run_flow(self, edge, f):
        edge.cap -= f
        self.redge(edge).cap += f
    
    def add_edge(self, u, v, c):
        fro_idx = len(self.lst[u])
        to_idx = len(self.lst[v])
        self.lst[u].append(Edge(u, v, to_idx, c))
        self.lst[v].append(Edge(v, u, fro_idx, 0))

class FordFulkerson(object):
    INF = 1 << 15
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
            G.run_flow(edge, flow)
            return flow
        return 0

    def solved(self, G, s, t):
        res = 0
        while True:
            self.seen = [False] * len(G)
            flow = self.fodfs(G, s, t, self.INF)
            if flow == 0:
                return res
            res += flow

n, m, s, t = map(int, input().split())
G = Graph(n)
for _ in range(m):
    u, v, d, c = map(int, input().split())
    G.add_edge(u-1, v-1, d)
ff = FordFulkerson()
