class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        ans=0
        for sell in prices:
            if sell<buy:
                buy=sell
            elif sell>buy:
                profit=sell-buy
                ans=max(ans,profit)
        return ans
            

        