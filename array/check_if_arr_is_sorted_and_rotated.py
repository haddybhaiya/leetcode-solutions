class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        new = nums + nums
        nums.sort()
        for i in range(n):
            if new[i:i+n] == nums:
                return True
        return False