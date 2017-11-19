n = 5
k = 4
# Khoi tao mang k phan tu -1
x = [-1] * k
# Khoi tao mang n phan tu True
c = [True] * n

def f(i):
    global x
    for j in range(n):
        if c[j]:
            x[i] = j + 1
            if (i == k - 1):
                print(x)
            else:
                c[j] = False
                f(i + 1)
                c[j] = True

f(0)
