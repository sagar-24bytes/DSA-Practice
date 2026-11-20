class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=dp[1]=1
        for step in range(2,n+1):
            for x in range(1,3):
                dp[step]+=dp[step-x]
        return dp[n]

        