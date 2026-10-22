class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        cost.append(0)
        dp=[-1]*(n+1)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n+1):
            first=cost[i]+dp[i-1]
            sec=cost[i]+dp[i-2]
            dp[i]=min(first,sec)
        return dp[n]
        

