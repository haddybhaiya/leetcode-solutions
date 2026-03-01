class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 :
            return 2
        if n== 0:
            return 1
        
        powers_list = []
        i = 1
        while i-1 <= n:
            powers_list.append(i-1)
            i *= 2
        return len(powers_list)
    
        