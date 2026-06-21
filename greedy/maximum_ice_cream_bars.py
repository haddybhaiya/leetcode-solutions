class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        cnt = 0
        for i in costs:
            if coins >= i:
                coins-=i
                cnt+=1
        return cnt
            