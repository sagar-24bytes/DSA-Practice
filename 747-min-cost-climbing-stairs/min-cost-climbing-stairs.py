from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @lru_cache(None)
        def func(step,base):
            if step==base:
                return cost[base]
            if step<base:
                return float('inf')
            val=float('inf')
            
            return cost[step]+min(func(step-1,base),func(step-2,base))
        n=len(cost)
        cost.append(0)
        return min(func(n,0) , func(n,1))
        