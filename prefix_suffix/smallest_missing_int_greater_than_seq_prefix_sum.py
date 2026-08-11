class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                prefix += nums[i]
            else:break
        sett = set(nums)
        while prefix in sett:
            prefix+=1
        return prefix