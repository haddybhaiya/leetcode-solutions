from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
         """
      #counter approach
        l = []
        seen = set()
        mini = float('inf')
        for i in nums1:
            if i in nums2:
                if i not in seen:
                    mini = min(nums1.count(i),nums2.count(i))
                    while (mini !=0):
                        l.append(i)
                    seen.add(i)            
                else:
                    continue
        return l
      #brute force
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
         """
        l = []
        seen = set()
        mini = float('inf')
        for i in nums1:
            if i in nums2:
                if i not in seen:
                    mini = min(nums1.count(i),nums2.count(i))
                    while (mini !=0):
                        l.append(i)
                        mini -=1
                    seen.add(i)            
                else:
                    continue
        return l
    
