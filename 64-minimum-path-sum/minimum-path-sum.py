class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        for r in range(m):
            for c in range(n):
                if r==0 and c==0:
                    continue
                up=grid[r-1][c] if r>0 else float('inf')
                left=grid[r][c-1] if c>0 else float('inf')
                grid[r][c]=grid[r][c]+min(up,left)
        return grid[m-1][n-1]

        