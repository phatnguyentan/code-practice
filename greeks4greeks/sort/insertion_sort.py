from math import *
# sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
    return arr

print(insertion_sort([4, 1, 0, 2, 3, 2]))
