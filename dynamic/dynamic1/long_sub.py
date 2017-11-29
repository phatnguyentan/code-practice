# input
# arr = [5, 2, 3, 4, 9, 10, 5, 6, 7, 8]
# output
# [1,2,3,4,5,6,9,10]
def longSub(a):
    # init array length at i
    a.append(9999999)
    a.insert(-9999999, 0)
    l = [0] * len(a)
    t = [0] * len(a)
    for i in range(len(a)-1, -1, -1):
        if i == len(a) - 1:
            l[i] = 0
            t[i] = None
            continue
        # min length is 0
        jmax = len(a) - 1
        for j in range(i, len(a)):
            if a[i] < a[j] and l[j] > l[jmax]:
                jmax = j
        l[i] = l[jmax] + 1
        t[i] = jmax
    print("a[i]", a)
    print("L[i]", l)
    print("T[i]", t)
    i = t[0]
    while i != len(a) -1:
        print(a[i])
        i = t[i]
    return l
