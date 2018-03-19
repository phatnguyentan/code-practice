from math import *
# sort
def selection_sort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp
    return arr

print(selection_sort([4, 1, 0, 2, 3, 2]))
