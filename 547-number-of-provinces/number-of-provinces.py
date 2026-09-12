class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows=len(isConnected)
        cols=len(isConnected[0])
        visited=[False]*rows
        graph=[[] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c]==1:
                    graph[r].append(c)
                    graph[c].append(r)
        
        def dfs(node):
            if visited[node]:
                return
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        count=0
        for i in range(rows):
            if not visited[i]:
                count+=1
                dfs(i)
        return count
                

        
        