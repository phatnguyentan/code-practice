#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
# your code goes here
def quick_sort_string(a):
    if len(a) > 1:
        left = []
        right = []
        el = a[0]
        for i in range(1, len(a)):
            if (len(a[i]) < len(el)):
                left.append(a[i])
            else:
                if (len(a[i]) == len(el) and a[i] < el):
                    left.append(a[i])
                else:
                    right.append(a[i])
        return quick_sort_string(left) + [el] + quick_sort_string(right)
    else:
        if len(a) == 1:
            return [a[0]]
        return []
unsorted = quick_sort_string(unsorted)

for v in unsorted:
    print(v)
