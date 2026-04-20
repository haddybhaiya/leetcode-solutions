class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        maxi = -1
        for i in range(n):
            if colors[0] != colors[i]:
                maxi = max(maxi,i)
        for i in range(n):
            if colors[i] != colors[n-1]:
                maxi = max(maxi,n-1-i)   

        return maxi


        
