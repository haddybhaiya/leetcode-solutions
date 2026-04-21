class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        look = set(nums)
        l = []
        mini = min(nums)
        maxi = max(nums)
        for i in range(mini,maxi+1):
            if i not in look:
                l.append(i)
        return l
