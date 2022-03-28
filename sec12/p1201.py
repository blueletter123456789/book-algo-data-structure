def merge_sort(nums):
    len_numbers = len(nums)
    if len_numbers <= 1:
        return nums

    mid = len_numbers//2
    left_nums = merge_sort(nums[:mid])
    right_nums = merge_sort(nums[mid:])
    i = j = k = 0
    res = [0]*len_numbers

    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] <= right_nums[j]:
            res[k] = left_nums[i]
            i += 1
        else:
            res[k] = right_nums[j]
            j += 1
        k += 1

    while i < len(left_nums):
        res[k] = left_nums[i]
        i += 1
        k += 1

    while j < len(right_nums):
        res[k] = right_nums[j]
        j += 1
        k += 1

    return res
    
def binary_search(nums, val):
    left, right = 0, len(nums)
    while right >= left:
        mid = (left + right)//2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1


import random

nums = [random.randint(0, 1000) for _ in range(10)]
print(nums)
res = merge_sort(nums)
print(res)
print(' '.join([str(binary_search(res, nums[i])) for i in range(len(nums))]))
