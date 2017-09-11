#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    count = 0
    dict = {}
    for x in a:
        if x in dict:
            count += dict[x]
            dict[x] = 1
        else:
            if x + k in dict:
                dict[x + k] += 1
            else:
                dict[x + k] = 1
            if x - k in dict:
                dict[x - k] += 1
            else:
                dict[x - k] = 1
    return count
# Tail starts here
if __name__ == '__main__':
    a = "5 1"
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = "1 5 3 4 2"
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
