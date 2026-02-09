class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        i = 0
        j = len(s) -1
        vowel = set('aeiouAEIOU')
        while i <j:
            if s[i] in vowel and s[j] in vowel :
                s[i] , s[j] = s[j] , s[i]
                i += 1
                j -=1
            elif s[i] not in vowel :
                i +=1
            elif s[j] not in vowel  :
                j -= 1
            else :
                i+=1
                j-=1
        return "".join(s)




        
