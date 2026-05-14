class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = max(nums)
        sett = set(nums)
        ll = len(nums)
        if ll < n+1 or ll > n+1:
            return False
        if nums.count(n) != 2:
            return False
        for num in range(1,n+1):
            if num not in sett:
                return False
        return True