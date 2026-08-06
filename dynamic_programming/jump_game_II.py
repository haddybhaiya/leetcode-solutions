class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(len(nums)):
            for x in range(i+1,min(n,i+nums[i]+1)):
                dp[x] = min(dp[x],dp[i]+1)
        return dp[-1]