class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        mapping  = {}
        numbering = {}
        for i in range(26):
            mapping[letters[i]] = weights[i]
            numbering[i] = letters[25 -i]
        total = ""
        for j in words:
            empty = 0
            for m in j:
                   empty+=(mapping.get(m,0))
            total += numbering[empty%26]
        return total
