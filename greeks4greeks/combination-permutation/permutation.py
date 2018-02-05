def permutate(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r+1):
            print("swap1 l= ", l, "i= ", i)
            a[i], a[l] = a[l], a[i]
            permutate(a, l+1, r)
            print("swap2 l= ", l, "i= ", i)
            a[i], a[l] = a[l], a[i]

arr = [1, 2, 3, 4]
permutate(arr, 0, len(arr) - 1)
