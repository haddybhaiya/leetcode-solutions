class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        t ,l = 0,0
        b,r = len(grid) -1,len(grid[0]) -1
        while t<b and l<r:
            length,width = b -t,r-l
            perimeter = (2* length)+(2 *width)
            j = k % perimeter
            while j:
                tmp = grid[t][l]
                for i in range(l,r):
                    grid[t][i] = grid[t][i+1]
                for i in range(t,b):
                    grid[i][r] = grid[i+1][r]
                for i in range(r,l,-1):
                    grid[b][i] = grid[b][i -1]
                for i in range(b,t,-1):
                    grid[i][l] = grid[i-1][l]
                grid[t+1][l] = tmp
                j-=1
            t+=1
            l+=1
            b-=1
            r-=1
        return grid
