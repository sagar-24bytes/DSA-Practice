from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @lru_cache(None)
        def profit(idx,buy):
            if idx<0 or idx>=n:
                return 0
            if buy==1:
                return max(-prices[idx]+profit(idx+1,0) , profit(idx+1,1))
            else:
                return max(prices[idx]+profit(idx+2,1) , profit(idx+1,0))
            
        return profit(0,1)



        