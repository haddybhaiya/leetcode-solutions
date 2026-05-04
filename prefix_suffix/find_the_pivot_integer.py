class Solution(object):
    def pivotInteger(self, n):
        prefix  = 0
        suffix = 0
        for i in range(n+1):
            suffix+=i
        for i in range(1,n+1):
            prefix+=i
            if prefix == suffix:
                return i
            suffix-=i
        return -1
        
