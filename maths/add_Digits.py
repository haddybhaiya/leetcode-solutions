class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        while num >= 10:
            s = 0
            for d in str(num):
                s += int(d)
            num = s
        return num
        
        
        
        

        

    
        
