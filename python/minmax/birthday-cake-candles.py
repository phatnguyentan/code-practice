#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max = ar[0]
    count = 1
    for i in range(1, n):
        if len(ar) > i:
            if max < ar[i]:
                max = ar[i]
                count = 1
            else:
                if ar[i] == max:
                    count += 1
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
