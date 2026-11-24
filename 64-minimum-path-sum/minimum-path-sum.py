from functools import lru_cache
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        @lru_cache(None)
        def func(r,c):
            if r==0 and c==0:
                return grid[0][0]
            if r<0 or c<0:
                return float('inf')
            up=func(r-1,c)
            left=func(r,c-1)
            return grid[r][c]+min(up,left)
        return func(m-1,n-1)


        