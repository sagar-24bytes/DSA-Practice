class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*n for _ in range(m)]
        def func(r,c):
            if obstacleGrid[r][c]==1:
                return 0
            if r==0 and c==0:
                return 1
            if r<0 or c<0:
                return 0
            
            if dp[r][c]!=-1:
                return dp[r][c]
            up=func(r-1,c)
            left=func(r,c-1)
            dp[r][c]=up+left
            return dp[r][c]
        return func(m-1,n-1)      