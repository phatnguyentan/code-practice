# f la gia tri lay dc tu i goi hang voi j khoi luong
# f(i, j) = f(i-1, j)
# f(i, j) = f(i-1, j - w[i]) + v[i]
# arr = [[3,3], [4,4], [5,4], [9, 10], [4, 4]]
arr = [[3,3], [4,4], [5,4], [9, 10], [4, 4]]

mem = {}
n = 0
m = 0
a = None
def bag(arr, k):
    # Init
    global n
    global m
    global a
    a = arr
    n = len(a)
    m = k
    a = arr
    f(n, m)
    print(mem)
    print(mem[str(n)+str(m)])
    while n != 0:
        if mem.get(str(n)+str(m)) != mem.get(str(n-1)+str(m)):
            print(n)
            m = m - a[n-1][1]
        n = n -1

def f(i, j):
    if mem.get(str(i)+str(j)) != None:
        return mem[str(i)+str(j)]
    if i == 0:
        mem['00'] = 0
        return mem['00']
    else:
        mem[str(i) + str(j)] = f(i-1, j)
        if j >= a[i-1][0] and f(i-1, j - a[i-1][0]) + a[i-1][1] > mem[str(i) + str(j)]:
            mem[str(i) + str(j)] = f(i-1, j - a[i-1][0]) + a[i-1][1]
        return mem[str(i) + str(j)]



import copy
arr = [[3,3], [4,4], [5,4], [9, 10], [4, 4]]
n = len(arr)
m = 11
v = 0
a = [0] * n
mark = [False] * n
vbest = 0
best = []
def chosse(i):
    global n
    global m
    global v
    global vbest
    global a
    global mark
    global best
    for j in range(len(arr)):
        if mark[j] != True:
            if m >= arr[j][0]:
                print(m, arr[j])
                a[i] = arr[j]
                m = m - arr[j][0]
                v = v + arr[j][1]
                mark[j] = True
                if v >= vbest:
                    best = copy.copy(a)
                    vbest = v
                chosse(i+1)
                m = m + arr[j][0]
                v = v - arr[j][1]
                mark[j] = False

def printF():
    global best
    global vbest
    print(best)
    print(vbest)
