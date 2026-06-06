class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = []
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -=nums[i]
            l.append(abs(left -right))
            left+=nums[i]
        return l
