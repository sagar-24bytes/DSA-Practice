class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        visited=[False]*n
        count=0
        def dfs(node):
            nonlocal count
            if visited[node]:
                return
            count+=1
            visited[node]=True
            for nei in rooms[node]:
                if not visited[nei]:
                    dfs(nei)
        dfs(0)
        return count==n

        