class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l= []
        curr = 0
        for i in s:
            if i.isalpha():
                curr+=1
            elif i == '*':
                if curr>0:
                    curr-=1
            elif i == '#':
                curr *= 2
            elif i == '%':
                pass
            l.append(curr)
        if k >= curr or k <0:
            return "."
        for i in range(len(s)-1,-1,-1):
            char = s[i]
            if char.isalpha():
                if k == l[i] -1:
                    return char
            elif char == "*":
                    pass
            elif char == "#":
                    prev = l[i]//2
                    if prev>0:
                        k %=prev
            elif char == "%":
                    curr_len_at_step = l[i]
                    if curr_len_at_step >0:
                        k = curr_len_at_step -1-k
        return "."