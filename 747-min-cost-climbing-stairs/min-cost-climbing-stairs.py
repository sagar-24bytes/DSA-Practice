class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        prev1=cost[0]
        prev2=cost[1]
        cost.append(0)
        for i in range(2,n+1):
            curr=cost[i]+min(prev1 , prev2)
            prev1,prev2=prev2,curr
        return prev2
        