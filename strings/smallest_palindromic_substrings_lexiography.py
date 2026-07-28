class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        first_half = s[:n//2]
        sorted_f = "".join(sorted(first_half))
        mid = s[n//2] if n %2 !=0 else ""
        return sorted_f + mid +sorted_f[::-1] 