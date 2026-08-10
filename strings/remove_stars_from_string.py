class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for i in s:
            if i == "*":
                l.pop()
                continue
            l.append(i)
        return "".join(l)