arr = []

def f(n, index):
    global arr
    for i in range(index+1, n+1):
        arr.append(i)
        n -= i
        if n > 0:
            f(n, i - 1)
            n += i
            arr.pop()
        else:
            print(arr)
            arr.pop()

f(6, 0)
