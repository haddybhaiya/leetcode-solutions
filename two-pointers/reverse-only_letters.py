class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        revrs = list(s)
        l,r = 0,len(s)-1
        while l<r:
            if not revrs[l].isalpha():
                l+=1
            elif not revrs[r].isalpha():
                r-=1
            else:
                revrs[l],revrs[r] = revrs[r],revrs[l]
                l +=1
                r-=1
        return "".join(revrs)