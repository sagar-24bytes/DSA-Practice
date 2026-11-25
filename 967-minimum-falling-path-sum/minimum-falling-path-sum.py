class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        dp=[[float('inf')]*m for _ in range(m)]
        dp[0]=matrix[0]
        for r in range(1,m):
            for c in range(m):
                val=float('inf')
                for col in(c-1,c,c+1):
                    if 0<=col<m:
                        val=min(val,dp[r-1][col])
                dp[r][c]=matrix[r][c]+val
        return min(dp[-1])



        