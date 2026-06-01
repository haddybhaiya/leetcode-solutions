class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        bal = 0
        n = len(cost)
        count = 0
        for i in range(n -1,-1,-1):
            count+=1
            if n >=3:    
                if count %3 !=0:
                    bal += cost[i]
                else:
                    continue
            else:
                bal+=cost[i]
        return bal