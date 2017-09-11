t = 2
m = 4
n = 5
arr = [1,4,5,3,2]

def get_ice_cream(m, arr):
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            print(dict[arr[i]] + 1, i + 1)
        else:
            dict[m - arr[i]] = i

get_ice_cream(m, arr)
