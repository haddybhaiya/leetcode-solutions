class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        from collections import defaultdict
        cnt = defaultdict(int) #create a dictionary
        limit = int(n **(1.0/3))+1 #set limit to stop cuberoot(n)
        for a in range(limit):
            for b in range(a,limit):
                s = a**3 + b ** 3
                if s>n:
                    break #break if a cube and b cube is larger than n
                cnt[s] +=1 #map number to its frequency
        l = []
        for i in cnt:
            if cnt[i] >=2:
                l.append(i) #append those which have frequency of 2 or more
        return sorted(l)
        
