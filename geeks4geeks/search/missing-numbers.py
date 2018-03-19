n = 10
m = 13

arr1 = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
arr2 = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

def missing_number(a1, a2):
    dict = {}
    for a in a1:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1

    for a in a2:
        if a in dict:
            dict[a] -= 1
        else:
            dict[a] = 1
    res = []
    for key, value in dict.items():
        if value != 0:
            res.append(key)

    res.sort()
    print(' '.join(str(e) for e in res))

missing_number(arr1, arr2)
