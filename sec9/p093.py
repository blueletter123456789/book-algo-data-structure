from collections import deque

class NotCorrectBracketsError(Exception):
    def __init__(self, *args: object):
        pass

    def __str__(self):
        return 'not correct value'


# input example: (()(())())(()())
# ( ( ) ( ( ) ) ( ) ) (  (  )  (  )  )
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
s = list(input())
symbol_list = {'(', ')'}
stack_list = deque()
idx_list = list()
try:
    for i in range(len(s)):
        # print(stack_list)
        if s[i] not in symbol_list:
            raise ValueError('input is in no brackets')
        if s[i] == '(':
            stack_list.append([i, s[i]])
        else:
            if not len(stack_list):
                raise NotCorrectBracketsError
            target = stack_list.pop()
            if target[1] == '(':
                idx_list.append([target[0], i])
            else:
                raise NotCorrectBracketsError
    if len(stack_list) > 0:
        raise NotCorrectBracketsError
except NotCorrectBracketsError as err:
    raise err
except ValueError as ex:
    raise ex
else:
    print(idx_list)
