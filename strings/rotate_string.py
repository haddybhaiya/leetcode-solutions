class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # orgL = list(reversed(list(s)))
        # rev = orgL
        # for i in range(len(s)):
        #     orgL[:i] = reversed(orgL[:i])
        #     if goal == "".join(orgL):
        #         return True
        #     orgL = rev
        # return False
        if len(s) != len(goal): #if len of goal and string are not same
            return False
        return goal in (s+s) #all combination lies in the double string

        
