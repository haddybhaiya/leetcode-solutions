class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        mini = float('inf')
        for i in range(len(nums)):
            val = nums[i]
            if val not in seen:
                seen[val]=[i] #add mapping of val->i in seen if not there in list form
            else:
                seen[val].append(i) #if number is there already then append list
                if len(seen[val]) >= 3: # if that list len is >=3
                    m = seen[val][-3]
                    n = seen[val][-2]
                    o = seen[val][-1]

                    dis = abs(m-n)+abs(n-o)+abs(o-m) #cal abs val
                    mini = min(mini,dis) #cal mini
        if mini == float('inf'):
            return -1
        return mini