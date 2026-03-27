class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l= 0 #left ptr
        zero_cnt = 0
        max_len = 0
        for r in range(len(nums)):
            if nums[r] == 0: #right ptr reaches desired 0
                zero_cnt+=1
            while zero_cnt >k: #on exceeding the flips for 0->1
                if nums[l] == 0:
                    zero_cnt-=1
                l+=1
            max_len = max(max_len,r-l+1)
        return max_len

