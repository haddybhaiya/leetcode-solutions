class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_1 = -1
        last_2 =  -1
        mini = float('inf')
        for i in range(len(nums)):
            if nums[i] == 1:
                last_1 = i
                if last_2 != -1:
                    mini = min(mini,abs(last_1 - last_2))
            elif nums[i] == 2:
                last_2 = i
                if last_1 != -1:
                    mini = min(mini,abs(last_1 - last_2))
        if mini == float('inf'):return -1 
        return mini
        
                
