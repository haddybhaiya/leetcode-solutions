class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        cnt = 0
        # while n>=1:
        #     if num % n == 0:
        #         cnt+=1
        #     n = n//10
        # return cnt

        name = str(num)
        for i in name:
            val = int(i)
            if num % val ==0:
                cnt+=1
        return cnt