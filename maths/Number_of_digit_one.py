class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        place  = 1
        while place<=n:
            left = n // (place*10) #calculates left part of the number
            mid = (n //place)%10 #mid part of the number
            right = n %place #1ones place
            if mid == 0:
                ans+=left*place
            elif mid == 1:
                ans+=left*place+right+1
            else:
                ans += (left+1) *place
            place*=10
        return ans
