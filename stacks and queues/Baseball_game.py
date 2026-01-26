from collections import deque
class Solution(object):
    def calPoints(self, operations):
        q = deque()
        for i in operations:
            if i == '+':
                 m = q.pop()
                 n = q[-1]
                 q.append(m)
                 q.append(m+n)
            elif i == 'D':
                 q.append(2*q[-1])
            elif i == 'C':
                 q.pop()
            else:
                q.append(int(i))
        return sum(q)
