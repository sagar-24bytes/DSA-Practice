class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[-1]*(amount+1)

        def func(amt):
            if amt==0:
                return 0
            if amt<0:
                return float('inf')
            if dp[amt]!=-1:
                return dp[amt]
            val=float('inf')
            for coin in coins:
                val=min(val,1+func(amt-coin))
            dp[amt]=val
            return dp[amt]
        ans=func(amount)
        return ans if ans!=float('inf') else -1
        