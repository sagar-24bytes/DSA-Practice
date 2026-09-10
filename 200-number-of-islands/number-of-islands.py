class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        visited=[[False]*cols for _ in range(rows)]

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if visited[r][c] or grid[r][c]=='0':
                return
            visited[r][c]=True
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and not visited[r][c]:
                    islands+=1
                    dfs(r,c)
        return islands
        

        