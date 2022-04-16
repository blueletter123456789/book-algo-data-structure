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

def calc(n, id=-1):
    cost = 0
    res = list()
    uf = UnionFind(n)
    for i in range(len(edges)):
        if i == id:
            continue
        w, e = edges[i]
        u, v = e
        if uf.is_same(u, v):
            continue
        res.append(i)
        cost += w
        uf.unite(u, v)
    if len(res) < n-1:
        return 1 << 60, list()
    return cost, res

n, m = map(int, input().split())
edges = list()
for _ in range(m):
    s, d, c = map(int, input().split())
    edges.append((c, (s-1, d-1)))
edges.sort()

base, lst = calc(n)
num = res = 0
for id in lst:
    cost, tgt = calc(n, id)
    if cost > base:
        num += 1
        res += edges[id][0]
print(num, res)
