from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = []
        # p = []
        # maxi = 0
        cnt = Counter(nums)
        for num,freq in cnt.most_common():
            if k!=0:
                l.append(num)
                k-=1
        return l
            
                 

            


        
