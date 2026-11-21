from functools import lru_cache
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        @lru_cache(None)
        def func(idx,buy):
            if idx==n:
                return 0
            if buy==1:
                return max(-prices[idx]+func(idx+1,0) , func(idx+1,1))
            elif buy==0:
                return max(prices[idx]+func(idx+1,1) , func(idx+1,0))
        return func(0,1)
        