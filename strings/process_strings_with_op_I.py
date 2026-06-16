class Solution:
    def processStr(self, s: str) -> str:
        l = ""
        sett = "#%*"
        for i in s:
            if i not in sett:
                l = l +i
            elif i =="*":
                n = len(l)
                l = l[:n-1]
            elif i =="#":
                result = l
                l = l+result
            elif i =="%":
                l = l[::-1]
        return l