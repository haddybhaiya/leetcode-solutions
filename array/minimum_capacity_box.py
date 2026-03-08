class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        
        mini = 1001 # choose a max value as min
        for i in range(len(capacity)):
            if capacity[i] == itemSize: #if itemSize is present in array then return i
                return i
            elif capacity[i] > itemSize: #if all members are greater than itemSize then update mini
                mini = min(capacity[i],mini)
        if mini == 1001: #if all the members are smaller than itemSize
            return -1
        else:
            return capacity.index(mini) #return index of mini
                
        
                
                
        
