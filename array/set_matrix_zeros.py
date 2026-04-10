class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        m  = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i) # add the ith row in row
                    col.add(j) # add the jth col in col
        for i in range(m):
            for j in range(n):
                if i in row or j in col: # if i or j in row or col 
                    matrix[i][j] = 0
                    
                


                    
