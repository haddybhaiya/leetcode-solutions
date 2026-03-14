class Solution(object):
    def search(self, nums, target):
        # arr = nums[:]
        # nums.sort()
        # i = 0
        # j = len(nums) - 1
        # while i <= j:
        #     mid = (i+j) // 2
        #     if nums[mid] == target:
        #         return arr.index(target)
        #     elif nums[mid] < target:
        #         i = mid +1
        #     else:
        #         j = mid -1
        # if nums[mid] not in arr:
        #     return -1
        # return arr.index(mid)
        if target not in nums:
            return -1
        return nums.index(target)
            
        
