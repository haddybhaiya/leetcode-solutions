class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        k=0
        m =0
        capii = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if word[0] in capii:
            for i in word:
                if i in capii:
                    k+=1
            if k == 1:
                return (k==1 and word[0] in capii)
            return k==len(word)
        for j in word:
            if j not in capii:
                k+=1
        return k == len(word)
