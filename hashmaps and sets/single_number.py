from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        cnt = Counter(nums)
        for num,freq in cnt.items():
            if freq == 1:
                return num
        
        
