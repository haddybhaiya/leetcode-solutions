class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_zeros = nums.count(0)
        # nums = nums[::-1
        cnt = 0
        for i in range(len(nums) - n_zeros):
            if nums[i] == 0:
                cnt+=1
        return cnt