class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowl = set('aeiou')
        reversed_s = "".join(reversed(s)) #one way to reverse a string
        for ch in reversed_s:
            if ch in vowl:
                reversed_s = reversed_s.replace(ch,"",1)
            else:
                break
        s = reversed_s[::-1] #another way to reverse a string
        return s
        
