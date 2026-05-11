class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        for i in nums:
            val = str(i)
            for j in val:
                l.append(int(j))
        return l