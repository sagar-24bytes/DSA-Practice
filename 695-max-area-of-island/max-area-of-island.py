class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if grid[r][c]==0:
                return 0
            grid[r][c]=0
            return 1+ dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1)

        ans=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    a=dfs(i,j)
                    ans=max(ans,a)
        return ans

                 
        
        