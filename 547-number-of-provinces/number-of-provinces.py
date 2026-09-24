class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[False]*len(isConnected)
        def dfs(node):
            visited[node]=True
            for i in range(len(isConnected[node])):
                nei=isConnected[node][i]
                if nei==1 and not visited[i]:
                    dfs(i)
        count=0
        for n in range(len(isConnected)):
            if not visited[n]:
                count+=1
                dfs(n)
        return count


        