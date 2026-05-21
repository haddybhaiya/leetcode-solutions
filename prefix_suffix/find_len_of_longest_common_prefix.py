class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()
        for num in arr1:
            while num>0:
                prefixes.add(num)
                num //=10 #set containg single num 
        longest_len = 0
        for num in arr2:
            while num>0:
                if num in prefixes:
                    curr_len = len(str(num))
                    longest_len = max(longest_len,curr_len)
                    break
                #otherwise
                num//=10
        return longest_len







        # cnt = 0
        # for i in arr1:
        #     val = str(i)
        #     somethig = False
        #     for j in arr2:
        #         matching = str(j)
        #         if val[0] == matching[0]:
        #             cnt+=1
        # return cnt
        # # """another approach"""
        # # sett = set(arr1)
        # # cnt = 0
        # # matching = ""
        # # for i in range(len(arr2)):
        # #     val = str(arr2[i])
        # #     for j in val:
        # #         matching += j
        # #         if int(matching) in sett: #later on checks for arr2 respect to arr1
        # #             cnt+=1
        # matching = ''
        # sett2 = set(arr2)
        # for i in range(len(arr1)):
        #     val = str(arr1[i])
        #     for j in val:
        #         matching += j
        #         if int(matching) in sett2:
        #             cnt+=1
        # return cnt