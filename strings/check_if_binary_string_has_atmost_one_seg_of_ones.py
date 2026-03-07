class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "01" not in s # check if 01 not in the code since if 01 then theres new segment of one
        
