from math import *
# sort
def merge_sort(arr):
    mid = floor(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]
    res = []

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            res += [left[0]]
            left = left[1:]
        else:
            res += [right[0]]
            right = right[1:]

    if len(left) > 0:
        res += left
    if len(right) > 0:
        res += right
    return res

print(merge_sort([4, 1, 0, 2, 2, 3]))
