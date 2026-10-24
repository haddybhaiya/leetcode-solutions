class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        numett1 = set(nums1)
        numett2 = set(nums2)
        cnt_set = set()

        for i in numett1:
            if i not in numett2:
                answer[0].append(i)
        for i in numett2:
            if i not in numett1:
                answer[1].append(i)
        return answer 
