from collections import Counter
class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        cnt = Counter(nums)
        cnter = 0
        for num,freq in cnt.items():
            if freq % 2 == 0:
                cnter+=freq
        return cnter == n

        
