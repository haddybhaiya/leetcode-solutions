class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        cnt = 0
        for i in patterns:
            if i in word:
                cnt+=1
        return cnt