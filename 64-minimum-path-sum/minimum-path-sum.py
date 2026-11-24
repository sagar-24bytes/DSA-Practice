class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        prev=[float('inf')]*n
        for r in range(m):
            curr=[float('inf')]*n
            for c in range(n):
                if r==0 and c==0:
                    curr[c]=grid[r][c]
                    continue
                up=prev[c] if r>0 else float('inf')
                left=curr[c-1] if c>0 else float('inf')
                curr[c]=grid[r][c]+min(up,left)
            prev=curr
        return prev[-1]

        