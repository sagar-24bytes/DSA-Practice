class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp=[[[0]*3 for _ in range(2)] for _ in range(n+1)]
        for idx in range(n-1,-1,-1):
            for buy in range(2):
                for k in range(1,3):
                    if buy==1:
                        dp[idx][buy][k]=max(-prices[idx]+dp[idx+1][0][k] , dp[idx+1][1][k])
                    elif buy==0:
                        dp[idx][buy][k]=max(prices[idx]+dp[idx+1][1][k-1] , dp[idx+1][0][k])
        return dp[0][1][2]
        