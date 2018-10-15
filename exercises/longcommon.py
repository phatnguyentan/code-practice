
a = [1, 3, 4, 5, 6, 7, 8, 90, 11 ]
b = [4, 5, 6, 8, 90, 10, 11]
tmp = "0"
max = 0

def tryit(p1, p2):
  global tmp
  global max
  if(a[p1] == b[p2]):
    tmp = tmp + str(b[p2])
  else:
    if (max < int(tmp)):
      max = int(tmp)
    tmp = "0"

for i in range(len(a)):
  p = 0
  for j in range(len(b)):
    if(i+p >= len(a)):
      break
    tryit(i + p, j)
    p = p + 1

print(max)
# 890