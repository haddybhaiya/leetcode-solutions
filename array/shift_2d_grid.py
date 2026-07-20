class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        value = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = (i*n + j+k)%(m*n)
                r = idx//n
                c = idx %n
                value[r][c] = grid[i][j]
        return value
            