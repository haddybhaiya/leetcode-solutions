from collections import deque
class Solution(object):
    def isValid(self, s):
        q = deque()
        pair = {')':'(','}':'{',']':'['}
        for i in s:
            if i in pair.values():
                q.append(i)
            else:
                if not q or q.pop() != pair[i]:
                    return False
        return not q
            
            
        
