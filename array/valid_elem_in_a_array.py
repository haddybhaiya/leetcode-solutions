class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = []
        for i in range(n):
            val = nums[i]
            if i ==0 or i == n-1:
                l.append(val)
                continue
            
            if val > max(nums[i+1:]):
                l.append(val)
            elif val > max(nums[:i]):
                l.append(val)
        return l
                
                
