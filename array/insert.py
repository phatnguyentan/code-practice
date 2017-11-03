def solution(a, i):
    if len(a) <= i:
        return a
    else:
        if a[i] == 1:
            # https://docs.python.org/2/library/array.html
            # array.insert(i, x)
            # Insert a new item with value x in the array before position i. Negative values are treated as being relative to the end of the array.
            a.insert(i, 0)
        else:
            a.insert(i, 1)
        a = solution(a, i+2)
    return a

a = [0, 1, 0]
print(solution(a, 0))
