class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
    
    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i+1)
            yield csum - psum
            psum = csum
        raise StopIteration
    
    def __str__(self):
        return str(list(self))
    
    def sum(self, i):
        if not 0 <= i <= self.size:
            raise ValueError('error in sum method')
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def add(self, i, x):
        if not 0 <= i <= self.size:
            raise ValueError('error in add')
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    
    def __getitem__(self, key):
        if not 0 <= key < self.size:
            raise ValueError('error in getitem')
        return self.sum(key+1) - self.sum(key)
    
    def __setitem__(self, key, value):
        if not 0 <= key < self.size:
            raise ValueError('error in setitem')
        self.add(key, value - self[key])

n = int(input())
l = list(map(int, input().split()))
left, right = 0, 10**10
geta = n+1
while right - left > 1:
    mid = (left+right)//2
    num = sum_val = 0
    bit = Bit(n*2+10)
    d = [0]*n
    bit.add(sum_val+geta, 1)
    for i in range(n):
        val = 0
        if l[i] <= mid:
            val = 1
        else:
            val = -1
        sum_val += val
        num += bit.sum(sum_val+geta)
        bit.add(sum_val+geta, 1)
    if num > n*(n+1)//2//2:
        right = mid
    else:
        left = mid
print(right)
