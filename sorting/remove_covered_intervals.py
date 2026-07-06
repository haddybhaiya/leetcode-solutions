class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        cnt=0
        n= len(intervals)
        intervals.sort(key= lambda x :( x[0],-x[1]))
        end = intervals[0][1]
        for i in range(1,n):
            if intervals[i][1] <= end :
                cnt+=1
            else:
                end = intervals[i][1]
        return n-cnt
