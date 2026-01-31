class Solution(object):
    def search(self, nums, target):
        r = 0
        l  = len(nums) - 1
        while r <= l:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target :
                r = mid + 1
            else :
                l = mid - 1
        return -1


        
