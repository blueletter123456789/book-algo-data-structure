# class Edge(object):
#     def __init__(self, f, t, r, c):
#         self.fro = f
#         self.to = t
#         self.rev = r
#         self.cap = c

# class Graph(object):
#     def __init__(self, n):
#         self.lst = [list() for _ in range(n)]
    
#     def __getitem__(self, key):
#         return self.lst[key]
    
#     def __len__(self):
#         return len(self.lst)
    
#     def redge(self, edge):
#         return self.lst[edge.to][edge.rev]
    
#     def run_flow(self, edge, f):
#         edge.cap -= f
#         self.redge(edge).cap += f
    
#     def add_edge(self, f, t, c=1):
#         fro_rev = len(self.lst[f])
#         to_rev = len(self.lst[t])
#         self.lst[f].append(Edge(f, t, to_rev, c))
#         self.lst[t].append(Edge(t, f, fro_rev, 0))

# class FordFulkerson(object):
#     INF = 1 << 20
#     def __init__(self):
#         self.seen = list()
    
#     def fodfs(self, G, v, t, f):
#         if v == t:
#             return f
#         self.seen[v] = True
#         for edge in G[v]:
#             if self.seen[edge.to]:
#                 continue
#             if edge.cap == 0:
#                 continue
#             flow = self.fodfs(G, edge.to, t, min(f, edge.cap))
#             if flow == 0:
#                 continue
#             G.run_flow(edge, flow)
#             return flow
#         return 0

#     def solved(self, G, s, t):
#         total_flow = 0
#         while True:
#             self.seen = [False]*len(G)
#             flow = self.fodfs(G, s, t, self.INF)
#             if flow == 0:
#                 return total_flow
#             total_flow += flow

# def graph_idx(w, x, y):
#     return w*x + y + 1

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# h, w = map(int, input().split())
# input_map = [list(input()) for _ in range(h)]
# s, t = 0, h*w+1
# G = Graph(h*w+2)
# ans = 0
# for ri in range(h):
#     for ci in range(w):
#         if input_map[ri][ci] == '.':
#             ans += 1
#         current_idx = graph_idx(w, ri, ci)
#         if current_idx % 2 == 0:
#             G.add_edge(s, current_idx)
#         else:
#             G.add_edge(current_idx, t)
#         for di in range(4):
#             nx = ri+dx[di]
#             ny = ci+dy[di]
#             n_idx = graph_idx(w, nx, ny)
#             if nx < 0 or nx >= h or ny < 0 or ny >= w:
#                 continue
#             if input_map[nx][ny] == '.' and current_idx % 2 != n_idx % 2:
#                     G.add_edge(current_idx, n_idx)

# ff = FordFulkerson()
# print(ans - ff.solved(G, s, t))

from collections import deque

class HopcroftKarp(object):
    def __init__(self, l, r):
        self.size_l = l
        self.size_r = r
        self.lst = [list() for _ in range(l)]
        self.level = list()
        self.matched = list()
        self.matching = list()
        self.seen = list()
    
    def __getitem__(self, key):
        return self.lst[key]
    
    def add_edge(self, fro, to):
        self.lst[fro].append(to)
    
    def hobfs(self):
        que = deque()
        for left in range(self.size_l):
            self.level[left] = -1
            if not self.matched[left]:
                que.append(left)
                self.level[left] = 0
        self.level[self.size_l] = self.size_l
        while len(que):
            left = que.popleft()
            for i in range(len(self.lst[left])):
                right = self.lst[left][i]
                next = self.matching[right]
                if self.level[next] == -1:
                    self.level[next] = self.level[left]+1
                    que.append(next)

    def hodfs(self, left):
        if left == self.size_l:
            return True
        if self.seen[left]:
            return False
        self.seen[left] = True
        for i in range(len(self.lst[left])):
            right = self.lst[left][i]
            next = self.matching[right]
            if self.level[next] > self.level[left] and self.hodfs(next):
                self.matching[right] = left
                return True
        return False
    
    def solved(self):
        self.seen = [False] * self.size_l
        self.matched = [False] * self.size_l
        self.level = [-1] * (self.size_l + 1)
        self.matching = [self.size_l] * self.size_r
        res = 0
        while True:
            self.hobfs()
            self.seen = [False] * self.size_l
            finished = True
            for left in range(self.size_l):
                if not self.matched[left] and self.hodfs(left):
                    self.matched[left] = True
                    res += 1
                    finished = False
            if finished:
                break
        return res

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())
fi = [input() for _ in range(R)]
V = R*C
hk = HopcroftKarp(V, V)
for i in range(R):
    for j in range(C):
        left = i * C + j
        if fi[i][j] == '*':
            V -= 1
            continue
        if (i + j) % 2:
            continue
        for dir in range(4):
            ni, nj = i + dx[dir], j + dy[dir]
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue
            if fi[ni][nj] == '*':
                continue
            right = ni * C + nj
            hk.add_edge(left, right)
res = hk.solved()
print(V - res)
