class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
            cnt_target = 0
            for j in range(i,n):
                if nums[j] == target:
                    cnt_target +=1
                size = j-i+1
                if cnt_target > size//2:
                    res+=1
        return res
        