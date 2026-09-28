class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        buy=prices[0]
        for sell in prices:
            p=sell-buy
            if p<0:
                buy=sell
            else:
                profit=max(profit,p)
        return profit

        