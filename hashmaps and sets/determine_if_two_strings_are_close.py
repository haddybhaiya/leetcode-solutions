from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        any = 0
        w1 = Counter(word1)
        w2 = Counter(word2)
        if w1 == w2 : 
            return True
        if set(w1.keys()) != set(w2.keys()):
            return False
        return sorted(w1.values()) == sorted(w2.values())
