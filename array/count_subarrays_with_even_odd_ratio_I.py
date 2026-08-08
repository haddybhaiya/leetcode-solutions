class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        # LIMIT = a/b 
        cnt = 0
        for i in range(len(nums)):
            even = 0
            odd = 0
            for j in range(i,len(nums)):
                if nums[j]%2 == 0:
                    even+=1
                else:
                    odd+=1
                if odd > 0 and even*b <= odd*a:
                    cnt+=1
                
        return cnt
                