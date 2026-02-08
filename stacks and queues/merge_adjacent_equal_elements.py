class Solution(object):
    def mergeAdjacent(self, nums):
        stack = []
        for i in nums:
            stack.append(i)
            while len(stack) > 1 and stack[-1] == stack[-2]:
                val = stack.pop() + stack.pop()
                stack.append(val)
        return stack
                
                
        
                    
        
