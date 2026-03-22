class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # nums2 = []
        # for i in range(len(nums1)):
        #     if i%2 != 0 or i == len(nums1)-1 :
        #         nums2.append(nums1[i])
        #     else: 
        #         nums2.append(nums1[i] - nums1[i+1])
        # def even(arr):
        #     return all(n%2 == 0 for n in arr)
        # def odd(arr):
        #     return all(n%2 != 0 for n in arr)        
        # return even(nums2) or odd(nums2)
        odds = 0
        for n in nums1:
            if n %2!=0:
                odds+=1 #count no. of odds
        even = len(nums1) -1 # else are even
        can_even = (odds!=1) # boolean which is true when odds>1
        can_odd = (odds >0 or even == 0) #can be true when odds>1 or even are none
        return can_even or can_odd
