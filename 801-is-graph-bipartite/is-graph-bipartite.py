class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        def dfs(node,curr_col):
            color[node]=curr_col
            for nei in graph[node]:
                if color[nei]==-1:  # unvisited node
                    if not dfs(nei,1-curr_col):
                        return False
                else:   # already visited node
                    if color[nei]==curr_col:
                        return False
            return True
        
        for i in range(n):
            if color[i]==-1:   # starting dfs only when node is not visited(coloured)
                if not dfs(i,0):
                    return False
        return True



        