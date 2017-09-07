def combination(n, k):
    a = []
    res = []
    for i in range(n):
        a += [i]
    left = 0

    while left <= n - k:
        right = left + 1
        while right < n:
            res += [a[:left] + a[right:n-left]]
        left += 1

    return res;

print(combination(5, 4))
