n = 5
k = 3
# Khoi tao mang k phan tu -1
x = [-1] * k

def f(i):
    for j in range(x[i - 1] + 1, n-k+i+1):
        x[i] = j
        if(i == k - 1):
            print(x)
        else:
            f(i + 1)
f(0)
