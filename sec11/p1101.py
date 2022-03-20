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

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
ans = 0
for i in range(m):
    uni = UnionFind(n+1)
    for j in range(m):
        if i == j:
            continue
        uni.unite(l[j][0], l[j][1])
    cnt = 0
    for j in range(1, n+1):
        print(f'{j=}, {uni.root(j)=}')
        if j == uni.root(j):
            cnt += 1
    if cnt > 0:
        ans += 1
print(ans)
