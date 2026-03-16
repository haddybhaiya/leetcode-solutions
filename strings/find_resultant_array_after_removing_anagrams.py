class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l = []
        prev = None #assign null value to prev counter
        for i in words:
            key = sorted(i)
            if key != prev:
                l.append(i)
            prev = key
                
        return l
