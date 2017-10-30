
def transmitter(a, k):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return 1
    count = 0
    m = 0
    l = 0
    r = 0
    while m < len(a):
        if m == len(a) - 1:
            return count + 1
        while m < len(a) - 1 and a[m+1] - k <= a[l]:
            m+=1
        while r < len(a) - 1 and a[m] + k >= a[r+1]:
            r+=1
        m = r + 1
        l = m
        r = m
        count+=1
<<<<<<< 5bc5072bd88b155488620c52f5cf8459d105dfa8


=======
>>>>>>> radio-transmitter
    return count

a = [7,2,4,6,5,9,12,11]
# a = [1,2,3,4,5]
a.sort()
n = 2

print(transmitter(a, n))
