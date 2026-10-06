from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*(numCourses)
        q=deque()
        ans=[]
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            ans.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return ans if numCourses==len(ans) else []
            
        

        
        