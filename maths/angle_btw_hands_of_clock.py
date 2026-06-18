class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hrs = ((30*hour))
        mins = (5.5*minutes)
        val = abs(hrs - mins)
        mini = min(val,360 - val)
        return mini