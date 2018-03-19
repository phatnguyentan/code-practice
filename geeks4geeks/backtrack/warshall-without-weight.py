n = [0, 1, 2, 3, 4, 5]
m = [[1, 2], [3, 4], [2, 4], [3, 5], [1, 3], [0, 1], [0, 2], [1, 4]]
s = 0
d = 4
x = [s]
b = [[False] * len(n) for i in range(len(n))]
c = [True] * len(n)
c[s] = False
def index():
    global m
    for i in range(len(m)):
        b[m[i][1]][m[i][0]] = True
        b[m[i][0]][m[i][1]] = True
def f(i):
    global b
    global x
    global s
    global d
    global n
    for j in range(len(n)) :
        if(c[j] and b[x[len(x) - 1]][j]):
            if (j == d):
                print(x + [j])
            else:
                x = x + [j]
                c[j] = False
                f(i + 1)
                c[j] = True
                x.pop()
index()
f(0)
