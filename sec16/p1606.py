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

n = int(input())
A = list(map(int, input().split()))
s, t = 0, n+1
ans = 0

G = Graph(n+2)
off_set = 0
for i in range(n):
    if A[i] >= 0:
        G.add_edge(s, i+1, 0)
        G.add_edge(i+1, t, A[i])
        off_set += A[i]
    else:
        G.add_edge(s, i+1, -A[i])
        G.add_edge(i+1, t, 0)
for i in range(1, n+1):
    for j in range(i*2, n+1, i):
        G.add_edge(i, j, INF)

di = Dinic()
ans = di.solved(G, s, t)
print(off_set - ans)



""" Sample code
#Dinic法で最大流を求める
#deque のimport が必要
#逆辺追加しなきゃいけないから、
#グラフの構成はadd_edgeで行う
#最大流は　flow    メソッドで

from collections import deque
class Dinic:
    def __init__(self,N):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.level = None
        self.progress = None
    def add_edge(self,fr,to,cap):
        forward = [to,cap,None]
        forward[2] = backward = [fr,0,forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
    def add_multi_edge(self,v1,v2,cap1,cap2):
        edge1 = [v2,cap1,None]
        edge1[2] = edge2 = [v1,cap2,edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)
    def bfs(self,s,t):
        self.level = level = [None] * self.N
        q = deque([s])
        level[s] = 0
        G = self.G
        while q:
            v = q.popleft()
            lv = level[v] + 1
            for w,cap,_ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    q.append(w)
        return level[t] is not None
    def dfs(self,v,t,f):
        if v == t:return f
        level = self.level
        Gv = self.G[v]
        for i in range(self.progress[v],len(Gv)):
            self.progress[v] = i
            w,cap,rev = e = Gv[i]
            if cap and level[v] < level[w]:
                d = self.dfs(w,t,min(f,cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
    def flow(self,s,t,):
        flow = 0
        inf = 1 << 30
        G = self.G
        while self.bfs(s,t):
            self.progress = [0] * self.N
            f = inf
            while f:
                f = self.dfs(s,t,inf)
                flow += f
        return flow
    def min_cut(self,s):
        #最小カットを実現する頂点の分割を与える
        #True  なら　source側
        #False なら　sink側
        visited = [False for i in range(self.N)]
        q = deque([s])
        while q:
            now = q.popleft()
            visited[now] = True
            for to,cap,_ in self.G[now]:
                if cap and not visited[to]:
                    visited[to] = True
                    q.append(to)
        return visited
    
N = int(input())
a = list(map(int,input().split()))
dinic = Dinic(N + 2)
ans = 0
for i in range(N):
    if a[i] > 0:
        ans += a[i]
        dinic.add_edge(0,i+1,a[i])
    elif a[i] < 0:
        dinic.add_edge(i+1,N+1,-a[i])
inf = 1 << 30
for i in range(1,N+1):
    for j in range(i * 2,N+1,i):
        dinic.add_edge(j,i,inf)
print(ans - dinic.flow(0,N+1))
"""