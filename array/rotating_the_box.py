class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])
        for row in boxGrid:
            empty = n-1
            for j in range(n-1,-1,-1):
                if row[j] == "*":
                    empty = j -1
                elif row[j] == "#":
                    row[j],row[empty] =  ".","#"
                    empty -=1

        new = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                new[j][m-i-1] = boxGrid[i][j]
        return new
        
        



                    