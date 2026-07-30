class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        cnt = 0
        total = 0
        for i in word:
            if cnt <8:
                total+=1
            elif cnt<16:
                total += 2
            elif cnt<24:
                total+=3
            else:
                total+=4
            cnt+=1
        return total