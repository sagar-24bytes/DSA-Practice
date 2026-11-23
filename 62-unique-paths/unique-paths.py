from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def func(r,c):
            if r==m-1 and c==n-1:
                return 1
            if r>=m or c>=n:
                return 0
            return func(r,c+1)+func(r+1,c)
        return func(0,0)
        