from math import *

def divide(n):
    d = []
    for a in range(2, ceil((n+1)/2)):
        if(n % a == 0):
            d.append(a)
    return d

def f(n):
    cache = {}
    for i in range(1, n+1):
        d = divide(i)
        if len(d) == 0:
            cache[i] = i
        else:
            x = [i]
            for a in d:
                x.append([cache[a], cache[int(i/a)]])
            cache[i] = x
    return cache[n]

arr = f(int(input()))
print(arr)
