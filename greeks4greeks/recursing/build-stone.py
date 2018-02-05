def buildStone(a, n):
    if n == 0: return 0
    if n == 1: return 1
    count = 1
    tmp = a[0]
    index = 0
    for i in range(n):
        if a[i] < tmp:
            b = trimZero(a[index:i])
            count += buildStone(b, len(b))

            b = trimZero(a[i:])
            count += buildStone(b, len(b))
            return count
        else:
            a[i] = a[i] - tmp
            if i == n -1:
                b = trimZero(a[index:])
                count += buildStone(b, len(b))
    return count

def trimZero(a):
    while len(a)>0 and a[0] == 0:
        a = a[1:]
    while len(a)>0 and a[len(a) - 1] == 0:
        a = a[0:len(a)-1]
    return a

arr = [8,8,5,7,9,8,7,4,8,8]
# arr = [8,8,5,7,9,8,7,4,8,8,5]
# arr = [8,5]
print(buildStone(arr, len(arr)))
