from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m=len(triangle)
        @lru_cache(None)
        def func(r,c):
            if r==m-1:
                return triangle[m-1][c]
            if r>=m or c>r:
                return float('inf')
            down=triangle[r][c]+func(r+1,c)
            right=triangle[r][c]+func(r+1,c+1)
            return min(down,right)
        return func(0,0)        