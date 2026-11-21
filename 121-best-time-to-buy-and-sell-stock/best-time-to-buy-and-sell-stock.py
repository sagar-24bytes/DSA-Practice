class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        dp=[0]*len(prices)
        n=len(prices)
        buy=prices[0]
        for i in range(1,n):
            if prices[i]>buy:
                dp[i]=max(dp[i],prices[i]-buy)
            else:
                buy=prices[i]
        return max(dp)
        