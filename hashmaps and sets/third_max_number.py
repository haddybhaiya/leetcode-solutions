class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        if n < 3:
            return max(nums)
        return nums[n - 3]

            


        
