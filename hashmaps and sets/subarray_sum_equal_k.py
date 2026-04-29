class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # mini = float('inf')
        # l = 0
        curr_sum = 0
        cnt = 0
        prefix = {0:1}
        for num in nums: #curr_sum + previous_sum = k -> previous_sum = curr_sum - k
            curr_sum += num
            if curr_sum -k in prefix:
                cnt += prefix[curr_sum -k]
            prefix[curr_sum] = prefix.get(curr_sum,0)+1 #increase counter to the previous_sum
        return cnt
        
