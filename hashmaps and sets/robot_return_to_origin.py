class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        mapping = {"R":7,"L":-7,"U":2,"D":-2}
        val = 0
        for i in moves:
                val += mapping[i]
        return val == 0

        
