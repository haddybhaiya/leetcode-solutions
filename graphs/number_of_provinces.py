class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        n = len(isConnected)
        cnt=0
        def dfs(node):
            visited.add(node)
            for j in range(n):
                if isConnected[node][j]==1 and j not in visited:
                    dfs(j)
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt+=1
        return cnt