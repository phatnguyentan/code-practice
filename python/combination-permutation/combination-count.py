def combinationCount(n, k):
    def _factorial(n):
        r = 1
        for i in range(1, n+1):
            r *= i
        return r

    return _factorial(n)/ (_factorial(k) * _factorial(n - k))

print(combinationCount(5, 4))
