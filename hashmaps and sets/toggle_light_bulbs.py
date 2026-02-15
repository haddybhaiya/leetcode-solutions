from collections import Counter
class Solution(object):
    def toggleLightBulbs(self, bulbs):
        # s = set()
        l = []
        # for i in range(len(bulbs)):
        #     if bulbs[i] not in s:
        #         s.add(bulbs[i])
        #     else:
        #         l.append(bulbs[i])
        cnt = Counter(bulbs)
        for blb,freq in cnt.items():
            if (freq % 2) == 1:
                l.append(blb)
        l.sort()
        return l
        
        
                
        
