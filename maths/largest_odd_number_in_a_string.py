class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        sett = set()
        for i in range(len(s)):
            # jump = "" + s[i] +s[i+1]:
            if s[i] in sett:
                return s[i]
            sett.add(s[i])
