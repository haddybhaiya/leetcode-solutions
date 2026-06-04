class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for i in range(num1,num2+1):
            val = str(i)
            size = len(val)
            if size <3:
                waviness+=0
            else:
                for j in range(1,size-1):
                    curr = int(val[j])
                    left = int(val[j-1])
                    right = int(val[j+1])
                    if curr > left and curr > right:
                        waviness+=1
                    elif curr < right and curr < left:
                        waviness +=1
        return waviness 