from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m=len(triangle)
        @lru_cache(None)
        def func(r,c):
            if r==0 and c==0:
                return triangle[0][0]
            if r<0 or c<0 or c>=len(triangle[r]):
                return float('inf')
            f=func(r-1,c) if r>0 else float('inf')
            s=func(r-1,c-1) if r>0 and c>0 else float('inf')
            return triangle[r][c]+min(f,s)
        ans=float('inf')
        for i in range(len(triangle[-1])):
            ans=min(ans,func(m-1,i))
        return ans
        