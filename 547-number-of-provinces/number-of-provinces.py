class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows=len(isConnected)
        cols=len(isConnected[0])
        # graph=[[] for _ in range(rows)]
        visited=[False]*rows
        count=0
        def dfs(node):
            if visited[node]:
                return
            visited[node]=True
            for nei in range(cols):
                if isConnected[node][nei]==1 and not visited[nei]:
                    dfs(nei)
        
        for i in range(rows):
            if not visited[i]:
                dfs(i)
                count+=1
        return count
        