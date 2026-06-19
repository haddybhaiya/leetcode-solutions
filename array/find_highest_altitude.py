class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = [0]
        for i in range(0,len(gain)):
            val = gain[i]
            altitude.append(altitude[i]+val)
        return max(altitude)