class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        def dfs(node,col):
            color[node]=col
            for nei in graph[node]:
                if color[nei]==-1:
                    if not dfs(nei,1-col):
                        return False
                elif color[nei]==col:
                    return False
            return True
        for x in range(n):
            if color[x]==-1:
                if not dfs(x,0):
                    return False
        return True

        