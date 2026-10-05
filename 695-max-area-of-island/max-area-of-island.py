class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if grid[r][c]==0:
                return 0
            grid[r][c]=0
            return 1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1)
        rows=len(grid)
        cols=len(grid[0])
        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=dfs(r,c)
                    ans=max(ans,area)
        return ans

        