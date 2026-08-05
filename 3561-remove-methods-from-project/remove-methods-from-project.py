class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for x,y in invocations:
            graph[x].append(y)
        sus=[False]*n
        def dfs(node):
            sus[node]=True
            for n in graph[node]:
                if not sus[n]:
                    dfs(n)
        dfs(k)
        for x,y in invocations:
            if not sus[x] and sus[y]:
                return [i for i in range(n)]
        return [i for i in range(n) if not sus[i]]
            
            
                

        