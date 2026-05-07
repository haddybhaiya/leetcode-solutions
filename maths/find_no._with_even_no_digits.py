class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            val = len(str(i))
            if val %2 == 0:
                cnt+=1
        return cnt