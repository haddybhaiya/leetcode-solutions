class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summing = defaultdict(list)
        maxi_all = 0
        for i in nums:
            val = str(i)
            maxi = 0
            mini = 1000000
            for j in val:
                use  = int(j)
                maxi = max(maxi,use)
                mini = min(mini,use)
            r = maxi-mini
            maxi_all = max(maxi_all,r)
            summing[r].append(i)
        return sum(summing[maxi_all])
