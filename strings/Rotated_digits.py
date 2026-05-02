class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        orig = n
        # n = str(n)
        cnt= 0
        for i in range(1,orig+1):
            jane = str(i)
            new = ""
            for j in jane:
                if j in ['0','1','8']:
                    new = new + j
                elif j in ['2','5']:
                    if j == "2":
                        new = new + "5"
                    else:
                        new = new + '2'
                elif j in ['6','9']:
                    if j == '6':
                        new = new + "9"
                    else:
                        new = new + "6"
                else:
                    new = ""
                    break
            if new != jane and new != "":
                cnt+=1
            # elif new == jane or new =="":
            #     continue
        return cnt
"""
complexity : O(NlogN) opitmal
"""


                
                    
        
        
