class Solution(object):
    from collections import Counter
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        maxi = 0
        for num in cnt:
            if num +1 in cnt:
                maxi = max(maxi,cnt[num] + cnt[num +1])
        return maxi
        
