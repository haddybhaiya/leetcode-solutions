from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        freq = Counter(nums)
        res = []
        for num,cnt in freq.items():
            if cnt > n // 3:
                res.append(num)
        return res
