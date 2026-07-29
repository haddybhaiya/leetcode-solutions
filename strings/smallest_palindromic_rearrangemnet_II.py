import math
from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half = n //2
        cnt = Counter(s[:half])
        def cnt_perm(r_count,Max_k):
            total_chars = sum(r_count.values())
            res = 1
            for char,count in r_count.items():
                res  = res * math.comb(total_chars,count)
                total_chars -= count
                if res > Max_k:
                    return Max_k +1
            return res
        if cnt_perm(cnt,k)<k:
            return ""
        res_half = []
        for _ in range(half):
            for char in sorted(cnt.keys()):
                if cnt[char] == 0:
                    continue
                
                # Try placing `char` here
                cnt[char] -= 1
                ways = cnt_perm(cnt, k)
                
                if k <= ways:
                    # 'char' belongs at this position
                    res_half.append(char)
                    break
                else:
                    # Skip 'ways' permutations and restore count
                    k -= ways
                    cnt[char] += 1

        first_half = "".join(res_half)
        mid = s[half] if n % 2 != 0 else ""
        
        return first_half + mid + first_half[::-1]



        