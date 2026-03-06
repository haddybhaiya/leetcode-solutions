class Solution(object):
    def reverseStr(self, s, k):
        n = len(s) -1
        temp = list(s)
        for i in range(0,n,2*k):
            temp[i:i+k] = reversed(temp[i:i+k])
        return "".join(temp)


        
