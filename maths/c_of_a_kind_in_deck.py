class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd
        cnt = Counter(deck)
        # ff = nums.count(nums[0])
        ff= 0
        for i in cnt:
            if cnt[i] < 2:
                return False
            if ff == 0:
                ff = cnt[i]
            else:
                ff = gcd(ff,cnt[i])
        return ff>=2
        