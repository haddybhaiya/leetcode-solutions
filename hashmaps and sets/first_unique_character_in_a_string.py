from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # seen = set()
        counter = Counter(s)
        mini = float('inf')
        for num,freq in counter.items():
            if freq == 1:
                mini = min(mini,s.index(num))
        if mini == float('inf'):
            return -1
        return mini
        
