class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        n=len(prices)
        memo={}
        def func(idx,buy,k):
            if idx==n or k==0:
                return 0
            if (idx,buy,k) in memo:
                return memo[(idx,buy,k)]
            if buy==1:
                memo[(idx,buy,k)]=max(-prices[idx]+func(idx+1,0,k) ,func(idx+1,1,k))
            elif buy==0:
                memo[(idx,buy,k)]=max(prices[idx]+func(idx+1,1,k-1) , func(idx+1,0,k))
            return memo[(idx,buy,k)]
        return func(0,1,2)
        