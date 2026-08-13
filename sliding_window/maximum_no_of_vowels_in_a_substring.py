class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = set('aeiou')
        win = sum(1 for ch in s[:k] if ch in vowel)
        maxi = win
        for r in range(k,len(s)):
            win += (s[r] in vowel) - (s[r-k] in vowel)
            maxi  = max(win,maxi)
        return maxi