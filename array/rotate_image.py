class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        # col = len(matrix[0])
        for i in range(row):
            for j in range(i+1,row):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(row):
            matrix[i] = matrix[i][::-1]
        
