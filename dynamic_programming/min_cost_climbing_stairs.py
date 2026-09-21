class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        df= [0]*len(cost)
        df[0] = cost[0]
        df[1] = cost[1]
        for i in range(2,len(cost)):
            df[i] = cost[i]+min(
                df[i-2],
                df[i-1]

            )
        return min(df[-1],df[-2])
