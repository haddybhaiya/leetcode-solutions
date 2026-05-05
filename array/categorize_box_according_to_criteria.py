class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        bulky = False
        Heavy = False
        vol = length*width*height
        
        if (vol >= 1000000000) or (height >= 10000) or (width >= 10000) or (length >= 10000):  
            bulky =True
        if mass >= 100:
            Heavy =True
        if Heavy and bulky:
            return "Both"
        elif Heavy and not bulky :
            return "Heavy"
        elif bulky and not Heavy :
            return "Bulky"
        elif not bulky and not Heavy:
            return "Neither"