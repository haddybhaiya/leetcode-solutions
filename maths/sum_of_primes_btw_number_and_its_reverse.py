import math
class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        # orig = n
        r= int(str(n)[::-1])
        low = min(n,r)
        high = max(n,r)
        
        sum = 0
        for i in range(low,high+1):
            if i <2:
                continue
            isprime = True
            for j in range(2,int(math.sqrt(i))+1):
                if i %j == 0:
                    isprime = False
                    break
            if isprime == True:
                sum+=i
        return sum
                
        