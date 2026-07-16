class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxi = 0
        prefixGcd = []
        for i in nums:
            maxi = max(maxi,i)
            prefixGcd.append(gcd(maxi,i))
        prefixGcd.sort()
        summing = 0
        l = 0
        r = len(prefixGcd)-1
        while l<r:
            summing+=gcd(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1
        return summing