class Solution(object):
    def countCommas(self, n):
        if n<1000:
            return 0
        else:
            k = 0
            for i in range(1000,n+1):
                if len(str(i)) >= 4:
                    k+=1
        return k
        
