class Solution(object):
    def dominantIndices(self, nums):
        tot = sum(nums)
        n = len(nums)
        k = 0
        for i in range(len(nums) - 1):
            tot = tot - nums[i]
            if nums[i] > ((tot ) / (n -i - 1)):
                k+=1
                
        return k
                
