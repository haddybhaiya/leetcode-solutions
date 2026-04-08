class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        l = []
        n = len(arr)
        diff = float('inf')
        for i in range(n-1):
            # current_diff = abs(arr[i+1] - arr[i])
            # if current_diff < diff:
            #     diff = current_diff

            diff = min(diff,abs(arr[i+1] - arr[i]))
        for i in range(n -1):
            if arr[i+1] - arr[i] == diff:
                l.append([arr[i],arr[i+1]])
        return l
