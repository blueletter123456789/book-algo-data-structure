""" O(NlogN)
n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
print(l[k-1])
"""

from datetime import datetime

def cnt_time(func):
    def _wrapper(*args):
        start_time = datetime.now()
        print(func(*args))
        print(datetime.now() - start_time)
    return _wrapper

"""
test function 1
"""
@cnt_time
def sort_func(lst, k):
    sorted_lst = sorted(lst)
    return sorted_lst[k-1]

"""
test function 2
"""
def partition(lst, pivot):
    """Modifired partition algorithm in section 7.1"""
    pivot_idx = None
    for idx, value in enumerate(lst):
        if value == pivot:
            pivot_idx = idx
    if pivot_idx is None:
        raise Exception
    lst[pivot_idx], lst[-1] = lst[-1], lst[pivot_idx]
    pivot = lst[-1]
    i = -1
    for j, val in enumerate(lst[:-1]):
        if val <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[-1] = lst[-1], lst[i + 1]
    return i + 1
 
def select(lst, i):
    """Selection in linear time"""
    if len(lst) == 1:
        return lst[0]
    split_lists = [lst[i * 5: (i + 1) * 5] for i in range((len(lst) + 4) // 5)]
    split_list_medians = [
        sorted(split_list)[(len(split_list) - 1) // 2]
        for split_list in split_lists
    ]
    x = select(split_list_medians, (len(split_list_medians) - 1) // 2)
    k = partition(lst, x)
    if i == k:
        return x
    elif i < k:
        return select(lst[:k], i)
    else:
        return select(lst[k + 1:], i - (k + 1))

@cnt_time
def linear_search(lst, k):
    """Calculate median by selection algorithm"""
    return select(lst, k)

@cnt_time
def wrapper_rec(lst, k):
    return rec(lst, k)

def rec(lst, k):
    len_lst = len(lst)
    if len_lst == 1:
        return lst[0]
    if len_lst <= 100:
        lst.sort()
        return lst[k-1]
    # median_lst = [lst[i * 5: (i + 1) * 5] 
    #   for i in range((len(lst) + 4) // 5)]
    # median_lst = [lst[i*5+2] if i*5+2 <= len(lst)-1 else len(lst)-1 
        # for i in range((len(lst)+4)//5)]
    median_lst = [lst[i+50] for i in range(0, len_lst-100, 100)]
    median_lst.append(lst[len_lst-1])

    m = rec(median_lst, len_lst//200)

    p, q, r = list(), list(), list()
    for i in range(len_lst):
        if lst[i] < m:
            p.append(lst[i])
        elif lst[i] == m:
            q.append(lst[i])
        else:
            r.append(lst[i])
    
    if k <= len(p):
        return rec(p, k)
    elif k <= len(p)+len(q):
        return m
    else:
        return rec(r, k - len(p) - len(q))

@cnt_time
def base_time(A):
    len_A = len(A)
    for _ in range(len_A):
        pass

# n, k = map(int, input().split())
# lst = list(map(int, input().split()))

import random
k = 4
lst = [random.randint(0, 10**9) for _ in range(10**7)]

sort_func(lst, k)
# linear_search(lst, k)
base_time(lst)
wrapper_rec(lst, k)
