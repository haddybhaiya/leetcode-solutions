class Solution(object):
    def moveZeroes(self, nums):
        cnt = nums.count(0)
        for i in range(cnt):
                nums.remove(0)
        nums.extend([0]*cnt)
        return nums
        
