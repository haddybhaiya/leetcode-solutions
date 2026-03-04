from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_sum = 0
        cnt = Counter(nums)
        for num,freq in cnt.items():
            if freq == 1:
                unique_sum = unique_sum + num
        return unique_sum
