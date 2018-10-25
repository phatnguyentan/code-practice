# Need optimize 999
from math import *
class Solution:
    def convert(self, s, numRows):
      if(numRows == 1):
        return s
      tmp = s
      x, y = 0, 0
      arr = [[0 for i in range(numRows)] for j in range(999)] 
      mode = "zig"
      while(len(tmp) > 0):
        arr[x][y] = tmp[0]
        tmp =  tmp[1:len(tmp)]
        if(y == 0):
          mode = "zig"
        if(y == numRows - 1):
          mode = "zag"
        if(mode == "zig"):
          y = y + 1
        else:
          x = x + 1
          y = y - 1
      for i in range(numRows):
        for j in range(x+1):
          if(arr[j][i] != 0):
            tmp = tmp + arr[j][i]
      return tmp


s = Solution()
# s.convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3)
# print(s.convert("ABCDEFGHIJKM", 3))
print(s.convert("PAYPALISHIRING", 3))
