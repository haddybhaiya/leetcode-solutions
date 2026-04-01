from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = Counter(arr)
        sett = set()
        for num,freq in cnt.items():
            if freq in sett:
                return False
            sett.add(freq)
        return True

        

        
