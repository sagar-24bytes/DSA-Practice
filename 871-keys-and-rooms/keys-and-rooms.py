from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        visited=[False]*n
        count=0
        q=deque()
        q.append(0)
        visited[0]=True
        while q:
            x=q.popleft()
            # visited[x]=True
            count+=1
            for nei in rooms[x]:
                if not visited[nei]:
                    # count+=1
                    visited[nei]=True
                    q.append(nei)
        print(count)
        return count==n

        

        