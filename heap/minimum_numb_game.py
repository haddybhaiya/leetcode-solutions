class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        import heapq
        heap=[]
        #heapq.heapify(heap)
        heapq.heapify(nums)
        while nums:
            a= heapq.heappop(nums)
            b= heapq.heappop(nums)
            heap.append(b)
            heap.append(a)
        return heap