class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0          # dp[i] means min no. of coins req to make amount i
        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i]=min(dp[i],dp[i-coin]+1) # here +1 as coin is alraedy used and we are checking for left amount i.e -> [i-coin]
        
        return dp[amount] if dp[amount]!=float("inf") else -1
        

        