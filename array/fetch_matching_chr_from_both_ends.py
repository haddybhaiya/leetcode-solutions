class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        mini = float('inf')
        n = len(s)
        for i in range(n):
            if s[i] == s[n-i-1]:
                mini = min(mini,i)
        if mini == float('inf'):
            return -1
        return mini
