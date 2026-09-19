class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for am in range(1,amount+1):
            for coin in coins:
                if coin<=am:
                    dp[am]=min(dp[am-coin]+1,dp[am])
        return dp[amount] if dp[amount]!=float('inf') else -1

        