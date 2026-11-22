from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def func(r,c):
            if r==0 and c==0:
                return 1
            if r<0 or c<0:
                return 0
            return func(r-1,c)+func(r,c-1)
        return func(m-1,n-1)