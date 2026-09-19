from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[[False]*cols for _ in range(rows)]
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited[r][c]=True
            while q:
                i,j=q.popleft()
                for x,y in d:
                    nr=i+x
                    nc=j+y
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1' and not visited[nr][nc]:
                        visited[nr][nc]=True
                        q.append((nr,nc))

        ans=0
        
        for  i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and not visited[i][j]:
                    ans+=1
                    bfs(i,j)
        return ans

        