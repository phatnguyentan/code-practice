# Phan de quy
def _combination(arr, k, l):
    if len(arr) < k: return
    if l > len(arr): return
    if len(arr[l:]) < k -1: return
    if len(arr[l:]) > k -1:
        _combination(arr, k, l+1)
        if k == 2:
            print([arr[0]] + [arr[l]])
        else:
            for i in range(l+k-2, len(arr)):
                print([arr[0]] + arr[l:l+k-2] + [arr[i]])
        return
    if len(arr[l:]) == k -1:
        print([arr[0]] + arr[l:])
        return
# Phan ham chay tung cap
def combination(arr, k):
    for i in range(len(arr) - k + 1):
        _combination(arr[i:], k, 1)

# Main
arr = [1,2,3,4,5]
for i in range(2, len(arr) + 1):
    combination(arr, i)
