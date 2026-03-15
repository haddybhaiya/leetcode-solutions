class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini= 102
        for i in nums:
            if nums.count(i) == 1 and i%2 ==0:
                mini = min(nums.index(i),mini)
        if mini ==102:
            return -1
        return nums[mini] #return the value of the number at mini index as minimised by mini function
        
