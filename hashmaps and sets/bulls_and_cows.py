from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cows = 0
        bull = 0
        s_rem =[]
        g_rem = []
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bull +=1
            else:
                s_rem.append(secret[i])
                g_rem.append(guess[i])
        s_c = Counter(s_rem)
        g_c = Counter(g_rem)
        for i in s_c:
            if i in g_c:
                cows += min(g_c[i],s_c[i])
        return str(bull)+"A"+str(cows)+"B"
