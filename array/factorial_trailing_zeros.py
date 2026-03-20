#original approach 4448ms too slow:
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0,1,2,3,4]:
            return 0
        else:
            k =0
            fact = 1
            for i in range(1,n+1):
                fact *= i
            fact = list(str(fact))
            for i in range(len(fact)-1,-1,-1):
                if fact[i] == "0":
                    k+=1
                else:
                    break
            return k
    #optimised
  class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n >0:
            n //= 5 #a number has 5 divisible amount of trailing zeros
            cnt +=n
        return cnt
