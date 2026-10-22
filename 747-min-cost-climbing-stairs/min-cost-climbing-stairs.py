class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        cost.append(0)
        # dp=[-1]*(n+1)
        prev2=cost[0]
        prev=cost[1]
        for i in range(2,n+1):
            first=cost[i]+prev
            sec=cost[i]+prev2
            curr=min(first,sec)
            prev2,prev=prev,curr
        return prev
        

