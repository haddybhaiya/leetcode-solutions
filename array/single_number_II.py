class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set(nums)
        for i in n:
            if nums.count(i) == 1:
                return i        
