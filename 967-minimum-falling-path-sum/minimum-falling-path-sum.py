from functools import lru_cache
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m=n=len(matrix)
        @lru_cache(None)
        def func(r,c):
            if r>=m or c>=m or c<0:
                return float('inf')
            if r==m-1:
                return matrix[r][c]
            # if r>=m or c>=m or c<0:
            #     return float('inf')
            val=float('inf')
            for i in (-1,0,1):
                f=func(r+1,c+i)
                val=min(val,f)
            return matrix[r][c]+val
        ans=float('inf')
        for x in range(m):
            ans=min(ans,func(0,x))
        return ans



        