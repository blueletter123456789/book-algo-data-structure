from collections import defaultdict
class UnionFind(object):
    def __init__(self, len_uni):
        self.par = [-1 for _ in range(len_uni)]
        self.size = [1 for _ in range(len_uni)]
    
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

""" TLE source
n, m = map(int, input().split())
A = [0]*m
B = [0]*m
for i in range(m):
    A[i], B[i] = map(int, input().split())

for i in range(m):
    uni = UnionFind(n+1)
    for j in range(m):
        if i >= j:
            continue
        uni.unite(A[j], B[j])
    root_dict = defaultdict(int)
    for j in range(1, n+1):
        root_dict[uni.root(j)] += 1
    cnt = 0
    if len(root_dict) > 1:
        seen = set()
        for k, v in root_dict.items():
            seen.add(k)
            for x, y in root_dict.items():
                if k != x and x not in seen:
                    cnt += v * y
    print(cnt)
"""

n, m = map(int, input().split())
A = [0]*m
B = [0]*m
for i in range(m):
    a, b = map(int, input().split())
    A[i], B[i] = a-1, b-1
uf = UnionFind(n)
# 逆順の初期の組み合わせ: nC2
cur = n*(n-1) // 2
res = list()
for i in range(m):
    res.append(cur)
    a, b = A[m-1-i], B[m-1-i]
    if uf.is_same(a, b):
        continue
    sa, sb = uf.uni_size(a), uf.uni_size(b)
    cur -= sa * sb
    uf.unite(a, b)
res = reversed(res)
for i in res:
    print(i)
