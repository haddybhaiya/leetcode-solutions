class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        mini = float('inf')
        l = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                mini = min(mini,r -l +1)
                curr_sum -= nums[l]
                l+=1
        return 0 if mini == float('inf') else mini
            
        
            
        
