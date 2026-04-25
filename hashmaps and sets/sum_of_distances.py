class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        n = len(nums)
        res = [0]*n
        count = defaultdict(int)
        total = defaultdict(int)
        for i in range(n):
            num = nums[i]
            res[i] += count[num]*i - total[num]
            count[num] += 1
            total[num] += i
        count.clear()
        total.clear()
        for i in range(n-1,-1,-1):
            num = nums[i]
            res[i] += total[num] - count[num] *i 
            count[num] += 1
            total[num] += i
        return res
