class Solution:
    def digitCount(self, num: str) -> bool:
        from collections import Counter
        cnt = Counter(num)
        for i in range(len(num)):
            val = int(num[i])
            if  val != cnt[str(i)]:
                return False
        return True
