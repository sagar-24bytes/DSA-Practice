class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        memo={}
        def profit(idx,buy):
            if idx<0 or idx>=n:
                return 0
            if (idx,buy) in memo:
                return memo[(idx,buy)]
            if buy==1:
                memo[(idx,buy)]=max(-prices[idx]+profit(idx+1,0) , profit(idx+1,1))
            else:
                memo[(idx,buy)]=max(prices[idx]+profit(idx+2,1) , profit(idx+1,0))
            return memo[(idx,buy)]
            
        return profit(0,1)



        