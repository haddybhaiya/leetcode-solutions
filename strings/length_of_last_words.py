class Solution(object):
    def lengthOfLastWord(self, s):
        k = 0
        s = s.rstrip()
        for i in s:
            if i.isalpha() == True:
                k +=1
            else :
                k = 0
        return k

        
