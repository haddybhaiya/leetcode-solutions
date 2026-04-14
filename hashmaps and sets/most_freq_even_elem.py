class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt  = Counter(nums)
        result = -1
        max_freq = -1
        for num,freq in cnt.items():
            if num %2 == 0:
                if freq > max_freq or (freq == max_freq and num<result):
                    max_freq = freq
                    result = num
        return result
