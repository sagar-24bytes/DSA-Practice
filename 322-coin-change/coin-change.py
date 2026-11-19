from functools import lru_cache
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @lru_cache(None)
        def func(amt):
            if amt==0:
                return 0
            if amt<0:
                return float('inf')
            val=float('inf')
            for coin in coins:
                if coin<=amt:
                    val=min(val,1+func(amt-coin))
            return val
        ans=func(amount)
        return ans if ans!=float('inf') else -1

        