from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        odd_1 = 0
        count = 0
        for i,freq in cnt.items():
            if freq%2 != 0:
                count+=freq-1
                odd_1=1
            elif freq %2 == 0:
                count+=freq
        return count+odd_1

                            
