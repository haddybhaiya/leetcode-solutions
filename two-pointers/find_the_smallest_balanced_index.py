class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n, left, rght = len(nums), sum(nums), 1     

        for i in range(n - 1, -1, -1):              
            left -= nums[i]
            if   left > rght:               
                rght *= nums[i]
            elif left < rght:               
                break
            else:                           
                return i
        return -1
