class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        buy=0
        for sell in range(len(prices)):
            p=prices[sell]-prices[buy]
            if p>0:
                profit=max(profit,p)
            else:
                buy=sell
        return profit
        