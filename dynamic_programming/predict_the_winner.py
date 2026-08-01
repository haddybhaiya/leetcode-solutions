class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}
        def solve(i,j):
            if i==j:
                return nums[i]
            if (i,j) in memo:
                return memo[(i,j)]
            l = nums[i] - solve(i+1,j)
            r = nums[j] - solve(i,j-1)
            memo[(i,j)] = max(l,r)
            return memo[(i,j)]
        return solve(0,len(nums)-1) >=0