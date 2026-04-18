class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = float('inf')
        last = {}
        for i,num in enumerate(nums):
            if num in last:
                mini  = min(mini,i - last[num])
            mirror = int(str(num)[::-1])
            last[mirror] = i
        if mini == float('inf'):
            return -1
        return mini
            
