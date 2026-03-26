class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        curr = 0 #current sum
        for i in range(k):
            curr += nums[i] #intialise fixed subarray of k size
        max_avg = curr/float(k) #calculate max_avg
        for i in range(k,n):
            curr +=nums[i] #add new value to fixed subarray 
            curr -= nums[i-k] #subtract previous value

            avg = curr/float(k) 
            max_avg = max(max_avg,avg)
        return max_avg

