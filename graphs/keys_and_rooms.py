class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = set()
        # m=0
        def dfs(node,n):
            visited.add(node)
            if len(visited)==n:
                return True
            for nxt in rooms[node]:
                if nxt not in visited:
                    if dfs(nxt,n):
                        return True
            return False
        return dfs(0,n)
