from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        q=deque()
        for n in range(numCourses):
            if indegree[n]==0:
                q.append(n)
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return ans if len(ans)==numCourses else []

        
        

    