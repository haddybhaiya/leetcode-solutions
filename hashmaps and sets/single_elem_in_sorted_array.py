from collections import Counter 
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        for i in cnt:
            if cnt[i] == 1:
                return i

        