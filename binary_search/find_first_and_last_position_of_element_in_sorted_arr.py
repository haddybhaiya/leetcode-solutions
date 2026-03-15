class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            inx= nums.index(target)
            k = nums.count(target)
            return [inx,inx+k-1]
        return [-1,-1]
