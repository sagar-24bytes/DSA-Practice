class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        ans=0
        for sell in prices:
            profit=sell-buy
            if profit<0:
                buy=sell
            else:
                ans=max(ans,profit)
        return ans

        