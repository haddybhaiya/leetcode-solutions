from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n):
            if n <100:
                return 0
            s = str(n)
            @cache
            def dp(i,tight,started,prev2,prev1):
                if i == len(s):
                    return (1,0)
                limit = int(s[i]) if tight else 9
                total_cnt = 0
                total_wave = 0
                for d in range(limit+1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        cnt,wave = dp(i+1,ntight,False,-1,-1)
                    else:
                        add = 0
                        if prev2 != -1:
                            if(prev1 > prev2 and prev1 > d) or  (prev1 < prev2 and prev1 < d):
                                add = 1
                        if prev1 == -1:
                            cnt,wave = dp(i+1,ntight,True,-1,d)
                        else:
                            cnt,wave = dp(i+1,ntight,True,prev1,d)
                        wave += add*cnt
                    total_cnt +=cnt
                    total_wave += wave
                return total_cnt,total_wave
            return dp(0,True,False,-1,-1)[1]
        return solve(num2) - solve(num1 -1)


        