class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        
        l = []
        for query in queries:
            for word in dictionary:
                cnt = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        cnt+=1
                    if cnt >2:
                        break
                if cnt <=2:
                    l.append(query)
                    break

        return l
        

