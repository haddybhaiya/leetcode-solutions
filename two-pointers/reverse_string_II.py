class Solution(object):
    def reverseStr(self, s, k):
        n = len(s) -1
        temp = list(s)
        for i in range(0,n+1 ,2*k):
            l = i
            r = min(i+k - 1,n)
            while l<r: #swapping machine
                temp[l],temp[r] = temp[r],temp[l]
                l +=1
                r-=1

        return "".join(temp)

        
