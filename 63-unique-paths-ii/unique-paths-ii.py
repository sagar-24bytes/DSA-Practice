class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1 if obstacleGrid[0][0]!=1 else 0
        for r in range(m):
            for c in range(n):
                if r==0 and c==0:
                    continue
                if obstacleGrid[r][c]!=1:
                    up=dp[r-1][c] if r>0 else 0
                    left=dp[r][c-1] if c>0 else 0
                    dp[r][c]=up+left
        return dp[m-1][n-1]
        