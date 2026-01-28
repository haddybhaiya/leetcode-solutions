class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        sum = 1
        i = 2
        while i*i <= num:
            if num %i == 0:
                sum += i
                if i != num // i:
                    sum += num // i
            i+= 1
        return sum == num
# best approach
return num in [6,28,496,8128,33550336]
# which results true if any number in the list
