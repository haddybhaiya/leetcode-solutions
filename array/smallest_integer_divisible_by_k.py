class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k == 2 or k==5 :
            return -1
        rem = 0
        for i in range(1,k+1):
            rem = (rem*10 +1) % k
            if rem ==0:
                return i
        return -1
