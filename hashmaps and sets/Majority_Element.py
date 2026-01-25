from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        cnt = Counter(nums)
        for i in nums:
            if cnt[i] > len(nums) // 2:
                return i
# optimal
class Solution(object):
    def majorityElement(self, nums):
        cnt = 0
        cand = None
        for i in nums:
            if cnt == 0:
                cand = i
            if i == cand:
                cnt += 1
            else:
                cnt -= 1
        return cand


        
                
        
              
                
        
