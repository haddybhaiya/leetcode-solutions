class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        diff = [0]*(2*limit+2)

        n = len(nums)
        for i in range(n//2):
            a,b = nums[i] , nums[n-1-i]
            low = min(a,b)+1
            high = max(a,b) +limit
            diff[low] -=1
            diff[high+1] +=1
            actual_sum = a+b
            diff[actual_sum] -=1
            diff[actual_sum+1] += 1
        ans = n
        curr_moves = n
        for i in range(2,2*limit +1):
            curr_moves += diff[i]
            ans = min(ans,curr_moves)
        return ans

        