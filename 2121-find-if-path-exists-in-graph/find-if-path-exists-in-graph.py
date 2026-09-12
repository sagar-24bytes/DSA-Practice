from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=[[] for _ in range(n)]
        q=deque()
        visited=[False]*n
        q.append(source)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        if source==destination:
            return True
        while q:
            x=q.popleft()

            for nei in graph[x]:
                if not visited[nei]:
                    visited[nei]=True
                    if nei==destination:
                        return True
                    q.append(nei)
        return False

        