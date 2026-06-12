class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        val = str(n)+str(n*2)+str(n*3)
        return "".join(sorted(val)) == '123456789'