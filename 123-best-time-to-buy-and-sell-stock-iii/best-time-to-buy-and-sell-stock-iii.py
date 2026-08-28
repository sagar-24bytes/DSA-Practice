class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        n=len(prices)
        def func(idx,buy,cap):
            if idx==n or cap==0:
                return 0
            if (idx,buy,cap) in memo:
                return memo[(idx,buy,cap)]
            if buy==1:
                memo[(idx,buy,cap)]=max(-prices[idx]+func(idx+1,0,cap),func(idx+1,1,cap))
            elif buy==0:
                memo[(idx,buy,cap)]=max(prices[idx]+func(idx+1,1,cap-1),func(idx+1,0,cap))
            return memo[(idx,buy,cap)]
        return func(0,1,2)

