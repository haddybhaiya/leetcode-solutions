class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        count = 0
        l = len(flowerbed)
        for i in range(l):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i-1] == 0)
                right  = (i == l-1) or (flowerbed[i+1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    count+=1
                if count >= n:
                    return True
        return False
