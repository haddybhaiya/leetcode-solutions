class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        new = [[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                new[j][i] = matrix[i][j]
        return new
        
