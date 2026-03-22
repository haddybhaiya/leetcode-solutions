class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        enty = nums1 #copy array
        if not enty:
            return True
        mini = min(enty) #find min in array
        odds = [x for x in enty if x %2 != 0] #list of odd elements in enty
        if mini %2 != 0: #if mini is odd then true
            return True
        else:
            if not odds: #return true if odd is empty
                return True
            return False #return false in else case
