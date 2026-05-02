class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        cnt  = numBottles
        while numBottles >= numExchange:
            new = numBottles // numExchange
            rem = numBottles % numExchange
            cnt+=new
            numBottles = new+rem
        return cnt 
