# import math
# class Solution(object):
#     def isPerfectSquare(self, num):
#         n = math.sqrt(num)
#         return n% 1 == 0

class Solution(object):
    def isPerfectSquare(self, num):
      l = 0
      r = num
      while l<=r:
        m = (l+r) //2
        r = m*m
        if r == num:
          return True
        elif r > num:
          r = m - 1
        else :
          l = m + 1
     return False
          
          

