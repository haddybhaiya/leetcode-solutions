class Solution:
    def maxProduct(self, n: int) -> int:
        val = str(n)
        l = [0]*len(val)
        for i in range(len(val)):
            l[i] = int(val[i])
        l.sort(reverse = True)
        return l[0]*l[1]
        
        
            