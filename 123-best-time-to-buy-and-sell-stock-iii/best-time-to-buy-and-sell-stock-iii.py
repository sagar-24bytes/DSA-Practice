from functools import lru_cache
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @lru_cache(None)
        def func(idx,buy,k):
            if idx==len(prices) or k==0:
                return 0
            if buy==1:
                return max(-prices[idx]+func(idx+1,0,k) , func(idx+1,1,k))
            if buy==0:
                return max(prices[idx]+func(idx+1,1,k-1) , func(idx+1,0,k))
        return func(0,1,2)


        
        