class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        prev=[0]*n
        for r in range(m):
            curr=[0]*n
            for c in range(n):
                if obstacleGrid[r][c]==1:
                    continue
                if r==0 and c==0:
                    curr[0]=1
                    continue
                up=prev[c]
                left=curr[c-1] if c>0 else 0
                curr[c]=up+left
            prev=curr
        return prev[-1]

        