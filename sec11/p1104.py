class UnionFindRank(object):
    def __init__(self, len_uni):
        self.par = [i for i in range(len_uni)]
        self.rank = [0] * len_uni
        self.diff_weight = [0] * len_uni
    
    def root(self, a):
        if self.par[a] == a:
            return a
        r = self.root(self.par[a])
        self.diff_weight[a] += self.diff_weight[self.par[a]]
        self.par[a] = r
        return self.par[a]
    
    def is_same(self, a, b):
        return self.root(a) == self.root(b)
    
    def unite(self, a, b, w):
        w += self.weight(a)
        w -= self.weight(b)
        a, b = self.root(a), self.root(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
            w = -w
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        self.par[b] = a
        self.diff_weight[b] = w
        return True
    
    def weight(self, a):
        self.root(a)
        return self.diff_weight[a]
    
    def diff(self, a, b):
        return self.weight(b) - self.weight(a)

n, m = map(int, input().split())
uni = UnionFindRank(n)
flg = True
for _ in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    if uni.is_same(l, r):
        dif = uni.diff(l, r)
        if d != dif:
            flg = False
            break
    else:
        uni.unite(l, r, d)
if flg:
    print('Yes')
else:
    print('No')
