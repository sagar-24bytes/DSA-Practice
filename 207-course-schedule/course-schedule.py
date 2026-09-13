class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)
        visited=[False]*numCourses
        path=[False]*numCourses

        def dfs(node):
            visited[node]=True
            path[node]=True
            for nei in graph[node]:
                if path[nei]:
                    return False
                elif not visited[nei]:
                    if not dfs(nei):
                        return False
            path[node]=False
            return True
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True

        
        
        