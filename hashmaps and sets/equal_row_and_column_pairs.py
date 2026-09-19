class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = {}
        cnt = 0
        for row in grid:
            row = tuple(row)
            rows[row] = rows.get(row,0)+1
        for j in range(len(grid[0])):
            col = tuple(grid[i][j] for i in range(len(grid)))
            if col in rows:
                cnt += rows[col]
        return cnt

        
