import heapq
import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        dicc = defaultdict(list)
        for i in range(len(points)):
            dis = math.pow(points[i][1]**2 + points[i][0]**2,0.5)
            dicc[dis].append([points[i][0],points[i][1]])
            heap.append(dis)
        heap.sort()
        l = []
        m = 0
        while k:
            l.append(dicc[heap[m]].pop())
            m+=1
            k-=1
        return l
