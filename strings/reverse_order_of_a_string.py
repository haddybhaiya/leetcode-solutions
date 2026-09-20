class Solution:
    def reverseDegree(self, s: str) -> int:
        lett = "abcdefghijklmnopqrstuvwxyz"
        dicc = {}
        k = 0
        for i in lett:
            dicc[i] = 26-k
            k+=1
        res = 0
        for i in range(len(s)):
            res+=(dicc.get(s[i],0))*(i+1)
        return res
