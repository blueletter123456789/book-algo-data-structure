import math

a, b, c = map(int, input().split())

# f(t)=A×t+B×sin(C×t×π) 
def calc(t):
    return a*t + b*math.sin(c*t*math.pi)

left, right = 0, 300
while right - left > 10**(-12):
    mid = (left+right)/2
    ft = calc(mid)
    if ft >= 100:
        right = mid
    else:
        left = mid
print(mid)
