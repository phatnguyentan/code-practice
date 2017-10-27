def buildStone(a, n):
    if n == 0: return 0;
    if n == 1: return 1;
    count = 1;
    b = []
    first = a[0]
    for i in range(1, n):
        if a[i] < first:
            b = trimZero(b)
            count += buildStone(b, len(b)) + 1
        else:
            b.append(a[i] - first)
    return count

def trimZero(a):
    while len(a)>0 and a[0] == 0:
        a = a[1:]
    while len(a)>0 and a[len(a) - 1] == 0:
        a = a[0:len(a)-1]
    return a

arr = [8,8,5,7,9,8,7,4,8]
print(buildStone(arr, len(arr)))
