from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt  = Counter(nums)
        l = []
        for i in cnt:
            if cnt[i] == 2:
                l.append(i)
        return l

        
