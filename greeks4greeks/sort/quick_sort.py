# sort
def quick_sort(arr):
    if len(arr) > 1:
        left = []
        right = []
        frist = arr[0]
        for i in range(1, len(arr)):
            if arr[i] <= frist:
                left = left + [arr[i]]
            else:
                right = right + [arr[i]]
        return quick_sort(left) + [frist] + quick_sort(right)
    else:
        if len(arr) == 0:
            return []
        else:
            return [arr[0]]
print(quick_sort([2, 2, 3, 1, 4]))
