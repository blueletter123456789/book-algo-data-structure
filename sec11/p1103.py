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

n, k, l = map(int, input().split())
road_uni = UnionFind(n)
train_uni = UnionFind(n)
both_map = [defaultdict(int) for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    road_uni.unite(a-1, b-1)
for i in range(l):
    a, b = map(int, input().split())
    train_uni.unite(a-1, b-1)
for i in range(n):
    root_road = road_uni.root(i)
    root_train = train_uni.root(i)
    both_map[root_road][root_train] += 1
ans = list()
for i in range(n):
    root_road = road_uni.root(i)
    root_train = train_uni.root(i)
    ans.append(str(both_map[root_road][root_train]))
print(' '.join(ans))
