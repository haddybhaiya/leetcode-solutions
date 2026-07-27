class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        maxi_1 = nums[0]
        maxi_2 = nums[1]
        return (maxi_1-1)*(maxi_2-1)