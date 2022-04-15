class UnionFind(object):
    def __init__(self, length):
        self.par = [-1]*length
        self.size = [1]*length
    
    def root(self, a):
        if self.par[a] == -1:
            return a
        self.par[a] = self.root(self.par[a])
        return self.par[a]
    
    def is_same(self, a, b):
        return self.root(a) == self.root(b)
    
    def unite(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return False
        if self.uni_size(a) < self.uni_size(b):
            a, b = b, a
        self.par[b] = a
        self.size[a] += self.size[b]
        return True
    
    def uni_size(self, a):
        return self.size[self.root(a)]

n, m = map(int, input().split())
edges = list()
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append([w, (u, v)])
edges.sort()
res = 0
shortest = list()
uf = UnionFind(n)
for i in range(m):
    w, edge = edges[i]
    u, v = edge
    if uf.is_same(u, v):
        continue
    res += w
    uf.unite(u, v)
    shortest.append((u, v))
print(res)
print(shortest)
