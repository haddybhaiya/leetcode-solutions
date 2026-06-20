class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1,0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n,n-1])
        m = len(restrictions)
        for i in range(1,m):
            id_diff = restrictions[i][0] -restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1],restrictions[i-1][1]+id_diff)
        for i in range(m-2,-1,-1):
            id_diff = restrictions[i+1][0] -restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + id_diff)
        max_height = 0
        for i in range(m-1):
            x1,h1 = restrictions[i]
            x2,h2 = restrictions[i+1]
            peak = (h1+h2+(x2-x1)) //2
            max_height = max(max_height,peak)
        return max_height
