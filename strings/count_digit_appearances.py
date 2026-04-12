class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        key = ""
        for i in nums:
            key+=str(i)
        return key.count(str(digit))
            
