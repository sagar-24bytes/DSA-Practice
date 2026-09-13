class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        visited=[False]*numCourses
        path=[False]*numCourses
        ans=[]
        for a,b in prerequisites:
            graph[b].append(a)
        ANS=[]

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
            ans.append(node)
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return []
        return ans[::-1]

        