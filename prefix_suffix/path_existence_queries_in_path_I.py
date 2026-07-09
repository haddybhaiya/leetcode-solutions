class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        pref = [0]*n
        for i in range(1,n):
            is_gap = (1 if (nums[i] - nums[i-1]>maxDiff) else 0)
            pref[i] = pref[i-1] + is_gap
        ans = []
        for u,v in queries:
            if u >v:
                u,v = v,u
            ans.append(pref[u]- pref[v] ==0 )
        return ans
