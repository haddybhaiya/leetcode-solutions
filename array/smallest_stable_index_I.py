class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = -1
        mini = float('inf')
        smallest = float('inf')
        n = len(nums)
        for i in range(n):
            maxi = max(nums[0:i+1])
            mini = min(nums[i:n])
            val = maxi - mini
            if val <= k:
                smallest = min(smallest,i)
        return -1 if smallest == float('inf') else smallest
            
