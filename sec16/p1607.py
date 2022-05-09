from collections import deque

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

    def add_edge(self, u, v, c):
        fro_edge = len(self.lst[u])
        to_edge = len(self.lst[v])
        self.lst[u].append(Edge(u, v, to_edge, c))
        self.lst[v].append(Edge(v, u, fro_edge, 0))

class Dinic(object):
    
    INF = 1 << 59
    def __init__(self):
        self.level = list()
        self.iter = list()
    
    def dibfs(self, G, s):
        self.level = [-1] * len(G)
        self.level[s] = 0
        que = deque([s])
        while len(que):
            v = que.popleft()
            for e in G[v]:
                if self.level[e.to] < 0 and e.cap > 0:
                    self.level[e.to] = self.level[v] + 1
                    que.append(e.to)
    
    def didfs(self, G, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(G[v])):
            self.iter[v] = i
            e = G[v][i]
            re = G.redge(e)
            if self.level[v] < self.level[e.to] and e.cap > 0:
                d = self.didfs(G, e.to, t, min(f, e.cap))
                if d > 0:
                    e.cap -= d
                    re.cap += d
                    return d
        return 0
    
    def solved(self, G, s, t):
        self.level = [-1] * len(G)
        self.iter = [0] * len(G)
        res = 0
        while True:
            self.dibfs(G, s)
            if self.level[t] < 0:
                return res
            for i in range(len(self.iter)):
                self.iter[i] = 0
                flow = 0
                while True:
                    flow = self.didfs(G, s, t, self.INF)
                    if flow > 0:
                        res += flow
                    else:
                        break

INF = 1 << 55

def idx_conv(i, j):
    return i * n + j

n, m = map(int, input().split())
in_lst = [input() for _ in range(n)]

num_black = 0
num_adj = 0
G = Graph(n*m*3 + 2)
s, t = n*m*3, n*m*3+1
for i in range(n):
    for j in range(m):
        if in_lst[i][j] == '.':
            continue
        num_black += 1

        if i+1 < n and in_lst[i+1][j] == '#':
            num_adj += 1
            newv = idx_conv(i, j) + n*m
            G.add_edge(newv, t, 1)
            G.add_edge(idx_conv(i, j), newv, INF)
            G.add_edge(idx_conv(i+1, j), newv, INF)
        
        if j+1 < m and in_lst[i][j+1] == '#':
            num_adj += 1
            newv = idx_conv(i, j) + n*m*2
            G.add_edge(s, newv, 1)
            G.add_edge(newv, idx_conv(i, j), INF)
            G.add_edge(newv, idx_conv(i, j+1), INF)

di = Dinic()
ans = di.solved(G, s, t)

print(num_black - (num_adj - ans))
