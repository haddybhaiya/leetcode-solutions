class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        word = ""
        for i in s:
                if i!=" ":
                    word = word+"".join(i)
                if i == " ":
                    l.append(word[::-1])
                    l.append(" ")
                    word = ""
        l.append(word[::-1])
        return "".join(l)

# optimal
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # l = []
        word = list(s.split())
        for i in range(len(word)):
            word[i] = word[i][::-1]
        return " ".join(word)
        
                

        
                

        
