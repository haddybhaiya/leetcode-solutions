class Solution(object):
    def sortColors(self, nums):
        n0 = nums.count(0)
        n1 = nums.count(1)
        n2 = nums.count(2)
        nums[:] = [0]*n0 + [1]*n1 + [2]*n2
