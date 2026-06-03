class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def calc(start1: List[int], dur1: List[int], start2: List[int], dur2: List[int]) -> int:
            first_finish = min(s+d for s,d in zip(start1,dur1))
            return min(max(first_finish,s)+d for s,d in zip(start2,dur2))
        ans1 = calc(landStartTime,landDuration,waterStartTime,waterDuration)
        ans2 = calc(waterStartTime,waterDuration,landStartTime,landDuration)
        return min(ans1,ans2)