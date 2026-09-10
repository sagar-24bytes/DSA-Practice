class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        rows=len(grid)
        cols=len(grid[0])
        visited=[[False]*cols for _ in range(rows)]
        
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if grid[r][c]==0 or visited[r][c]:
                return 0
            visited[r][c]=True
            return (1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and not visited[r][c]:
                    a=dfs(r,c)
                    ans=max(ans,a)
        return ans 

        
        
        