class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        ans=0
        for sell in range(len(prices)):
            p=prices[sell]-prices[buy]
            if p>=0:
                ans=max(ans,p)
            else:
                buy=sell
        return ans
        