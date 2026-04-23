class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        cnt = Counter(s)
        quency =-1
        for freq in cnt:
            quency = cnt[s[0]]
            if cnt[freq] != quency:
                return False
            quency = cnt[freq]

        return True
        