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

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    edges = list()
    for _ in range(m):
        s, t, c = map(int, input().split())
        s, t = s-1, t-1
        edges.append((c, (s, t)))
    sort_edges = sorted(edges)

    uni = UnionFind(n)
    spanning = list()
    for i in range(m):
        w, v = sort_edges[i]
        s, t = v
        if uni.is_same(s, t):
            continue
        spanning.append(w)
        uni.unite(s, t)
    median_idx = len(spanning) // 2
    print(spanning[median_idx])
