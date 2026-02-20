class Solution(object):
    def lengthOfLongestSubstring(self, s):
        q= []
        maxi = 0
        for char in s:
            while char in q:
                q.pop(0) # removes everything from front int the queue
            q.append(char)
            maxi = max(maxi,len(q)) # updates value at every char iteration
        return maxi
