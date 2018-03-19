x = []
bestWay = ""
max = 1000
minCost = max
arrMark = None
hashPicked = {0: True}
arrCost = None
n = None
m = None

def salemanTravel(n1, m1, arr):
    global n
    global m
    global x
    global arrMark
    global arrCost
    global hashPicked
    global bestWay
    n = n1
    m = m1
    init(arr)
    tryPick(1)
    print(bestWay)
    print(minCost)

def init(arr):
    global arrMark
    global arrCost
    global max
    global x
    arrMark = [[max] * n for i in range(n)]
    for a in arr:
        arrMark[a[0]][a[1]] = a[2]
        arrMark[a[1]][a[0]] = a[2]

    arrCost = [0] * (n + 1)
    x = [0] * (n + 1)


def tryPick(i):
    global x
    global minCost
    global bestWay
    # for each value can try for x
    for j in range(n):
        # if path not tralvel, we will try it
        if hashPicked.get(j) == None:
            # try x
            x[i] = j
            # plus arrCost at i
            arrCost[i] = arrCost[i - 1] + arrMark[x[i-1]][j]
            if arrCost[i] < minCost:
                if i == n -1:
                    x[i+1] = 0
                    arrCost[i+1] = arrCost[i] + arrMark[j][0]
                    if arrCost[i+1] < minCost:
                        minCost = arrCost[i+1]
                        bestWay = str(x)
                else:
                    # print("i = " + str(i+1) + " danh dau thanh pho: " + str(j+1))
                    hashPicked[j] = True
                    tryPick(i+1)
                    # print("i = " + str(i+1) + " bo thanh pho: " + str(j+1))
                    hashPicked[j] = None

# i = 2 danh dau thanh pho: 2
    # i = 3 danh dau thanh pho: 3
    # i = 3 bo thanh pho: 3
    # i = 3 danh dau thanh pho: 4
    # i = 3 bo thanh pho: 4
# i = 2 bo thanh pho: 2

# i = 2 danh dau thanh pho: 3
    # i = 3 danh dau thanh pho: 2
    # i = 3 bo thanh pho: 2
    # i = 3 danh dau thanh pho: 4
    # i = 3 bo thanh pho: 4
# i = 2 bo thanh pho: 3

# i = 2 danh dau thanh pho: 4
    # i = 3 danh dau thanh pho: 2
    # i = 3 bo thanh pho: 2
    # i = 3 danh dau thanh pho: 3
    # i = 3 bo thanh pho: 3
# i = 2 bo thanh pho: 4
