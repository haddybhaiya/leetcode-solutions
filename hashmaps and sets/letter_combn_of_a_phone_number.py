from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictt = {
            '2' : 'abc',
            '3' : 'def', #map indices to letters
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        l = []
        for chr in digits:
            if chr in dictt:
                l.append(dictt[chr]) #put mapped indices letter to a list
        if not l:
            return []
        res = []
        for p in product(*l): #product the list combination
            res.append("".join(p)) #product and join to a string
        return res
        

        
