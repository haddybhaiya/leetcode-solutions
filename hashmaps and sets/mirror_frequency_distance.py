from collections import Counter
class Solution(object):
    def mirrorFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
      freq = Counter(s)
      visited = set()
      ans = 0
      for c in freq:
        if c in visited:
          continue
        if c.isdigit():
          m = str(9 - int(c))
        else:
          m = chr(ord('z') - (ord(c)-ord('a'))) #ord maps number to the character
          ```
          when we use ord(c) -ord(a) then we are subtrating the position of pointer (eg say a) from starting that is a = 0 which makes 0-0 = 0
          freq.get is safe way to access a value in dictionary , this return 0 (freq.get(m,0)) if m isnt present
          ```
        ans += abs(freq[c] - freq.get(m,0))
        visited.add(m)
        visited.add(c)
      return ans
                  
