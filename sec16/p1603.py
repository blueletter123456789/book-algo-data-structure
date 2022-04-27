""" TLE source code
class Edge(object):
    def __init__(self, u, v, r, c=1):
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
    
    def run_flow(self, edge, f=1):
        edge.cap -= f
        self.redge(edge).cap += f
    
    def add_edge(self, fro, to, c=1):
        fro_rev = len(self.lst[fro])
        to_rev = len(self.lst[to])
        self.lst[fro].append(Edge(fro, to, to_rev, c))
        self.lst[to].append(Edge(to, fro, fro_rev, 0))

class FordFulkerson(object):
    INF = 1 << 15
    def __init__(self):
        self.seen = list()
    
    def fodfs(self, G, v, t, f):
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
    
    def solved(self, G, v, t):
        res = 0
        while True:
            self.seen = [False]*len(G)
            flow = self.fodfs(G, v, t, self.INF)
            if flow == 0:
                return res
            res += flow

from collections import defaultdict

while True:
    n, m, s, t = map(int, input().split())
    if n == 0 and m == 0 and s == 0 and t == 0:
        break
    s -= 1
    t -= 1
    G = Graph(n)
    in_lst = list()
    base = 0
    ans = defaultdict(int)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        in_lst.append((a, b))
        G.add_edge(a, b)
    ff = FordFulkerson()
    base = ff.solved(G, s, t)
    max_num = base
    for i in range(m):
        G = Graph(n)
        flow = 0
        for j in range(m):
            a, b = in_lst[j]
            if i == j:
                G.add_edge(b, a)
            else:
                G.add_edge(a, b)
        flow = ff.solved(G, s, t)
        if max_num <= flow:
            ans[flow] += 1
            max_num = flow
    if max_num == base:
        print(0, 0)
    else:
        print(max_num, ans[max_num])
"""

class Edge(object):
    def __init__(self, u, v, r, c=1):
        self.fro = u
        self.to = v
        self.rev = r
        self.cap = c
        self.icap = c
    
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
    
    def add_edge(self, fro, to, c=1):
        fro_rev = len(self.lst[fro])
        to_rev = len(self.lst[to])
        self.lst[fro].append(Edge(fro, to, to_rev, c))
        self.lst[to].append(Edge(to, fro, fro_rev, 0))

class FordFulkerson(object):
    INF = 1 << 15
    def __init__(self):
        self.seen = list()
    
    def fodfs(self, G, v, t, f):
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
    
    def solved(self, G, v, t):
        res = 0
        while True:
            self.seen = [False]*len(G)
            flow = self.fodfs(G, v, t, self.INF)
            if flow == 0:
                return res
            res += flow

def solved(G, n, s, t):
    from collections import deque

    ff = FordFulkerson()
    b = ff.solved(G, s, t)
    S, T = set(), set()
    que = deque([s])
    S.add(s)
    while len(que):
        v = que.popleft()
        for e in G[v]:
            if e.cap and e.to not in S:
                S.add(e.to)
                que.append(e.to)
    que.append(t)
    T.add(t)
    while len(que):
        v = que.popleft()
        for e in G[v]:
            if G.redge(e).cap and e.to not in T:
                T.add(e.to)
                que.append(e.to)
    res = 0
    for i in range(n):
        if i in T:
            for e in G[i]:
                if e.cap and e.cap == e.icap and e.to in S:
                    res += 1
    ma = b+1 if res else b
    print(ma, res)

while True:
    n, m, s, t = map(int, input().split())
    if n == 0 and m == 0 and s == 0 and t == 0:
        break
    s -= 1
    t -= 1
    G = Graph(n)
    base = 0
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G.add_edge(a, b)
    solved(G, n, s, t)
