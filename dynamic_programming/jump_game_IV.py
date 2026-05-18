from collections import deque,defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #1st is to calculate the place where the num are equal

        mapping = defaultdict(list)
        n = len(arr)
        for i,val in enumerate(arr):
            mapping[val].append(i)

        queue = deque([(0,0)])
        visited = {0}
        while queue:
            idx,steps = queue.popleft()
            if idx == n -1:
                return steps
            next_indices = [idx-1,idx+1]
            if arr[idx] in mapping:
                next_indices.extend(mapping[arr[idx]])
                del mapping[arr[idx]]

            for j in next_indices:
                if 0 <= j <n and j not in visited:
                    visited.add(j)
                    queue.append((j,steps+1))
        return -1