class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        res = []
        for i in spells:
            l = 0
            r = m -1
            ans = m
            while l<=r:
                mid = l+(r-l)//2
                if i * potions[mid] >=success: 
                    ans = mid
                    r = mid-1
                else:
                    l = mid+1
            res.append(len(potions)-ans)
        return res
