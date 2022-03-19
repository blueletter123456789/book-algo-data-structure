import re
from collections import deque

# (3 + 4) * (1 - 2) / (4 - 3)
# 3 4 + 1 2 - 4 3 - * /
s = input().split()
num_check = re.compile('\d')
symbol_list = {'+', '-', '*', '/'}
stack_list = deque()
for i in s:
    if num_check.match(i):
        stack_list.append(float(i))
    elif i in symbol_list:
        val2 = stack_list.pop()
        val1 = stack_list.pop()
        if i == '+':
            val1 += val2
        elif i == '-':
            val1 -= val2
        elif i == '*':
            val1 *= val2
        else:
            val1 /= val2
        stack_list.append(val1)
    else:
        raise ValueError('invalid symbol is inputed')
print(stack_list.pop())
