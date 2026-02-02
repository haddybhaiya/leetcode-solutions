class Solution(object):
    def intersection(self, nums1, nums2):
        n1 , n2= set(nums1) , set(nums2)
        l = []
        for i in n1:
            if i in n2:
                l.append(i)
        return l


        
