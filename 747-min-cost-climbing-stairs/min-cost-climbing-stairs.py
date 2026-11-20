class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[float('inf')]*(n+1)
        dp[0]=cost[0]
        dp[1]=cost[1]
        cost.append(0)
        for i in range(2,n+1):
            dp[i]=cost[i]+min(dp[i-1] , dp[i-2])
        return dp[n] if dp[n]!=float('inf') else -1
        