class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 0
        for i in range(len(nums)):
            while nums[i]>0:
                val += nums[i]%10
                nums[i] //= 10
            nums[i] = val
            val = 0
        return min(nums)

        
        
