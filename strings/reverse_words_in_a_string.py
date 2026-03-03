class Solution(object):
    def reverseWords(self, s):
        # return " ".join(s.split()[::-1])
          word  = s.split()
          word = word[::-1]
          return " ".join(word)
            
            






        
