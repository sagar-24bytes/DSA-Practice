class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for amt in range(1,amount+1):
                if coin<=amt:
                    dp[amt]+=dp[amt-coin]
        return dp[amount]

        