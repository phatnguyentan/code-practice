import sys

arr = list(map(int, input().strip().split(' ')))

max = arr[0]
min = arr[0]
sum = 0

for v in arr:
    if min > v:
        min = v
    if max < v:
        max = v
    sum += v

print(sum - max, sum - min)
