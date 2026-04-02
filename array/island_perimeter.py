class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        """
        ll = len(grid)
        lw = len(grid[0])
        perimi = 0
        for i in range(ll):
            for j in range(lw):
                if grid[i][j] == 1 :
                    perimi +=4
                    if i >0  and grid[i-1][j] == 1:
                        perimi -= 2
                    if j >0 and grid[i][j-1] == 1:
                        perimi-=2
        return perimi        
                    

        
