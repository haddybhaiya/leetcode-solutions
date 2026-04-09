class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for _ in range(n-1):
            party = []
            cnt = 1
            for i in range(1,len(result)):
                if result[i] == result[i-1]:
                    cnt+=1
                else:
                    party.append(str(cnt)+result[i-1])
                    cnt = 1
            party.append(str(cnt) +result[-1])
            result = "".join(party)
        return result



        
