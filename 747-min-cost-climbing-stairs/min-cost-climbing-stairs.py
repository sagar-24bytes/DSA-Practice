class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        cost.append(0)
        dp=[-1]*(n+1)
        def func(idx):
            if idx<0:
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            first=func(idx-1)+cost[idx]

            sec=func(idx-2)+cost[idx]
            dp[idx]=min(first,sec)
            return dp[idx]
        return func(n)

