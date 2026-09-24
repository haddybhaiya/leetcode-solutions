class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = str(nums[i])
            m = 0
            for j in val:
                m+=int(j)
            if m == i:
                return i
        return -1