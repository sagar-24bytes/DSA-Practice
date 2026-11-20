from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def func(steps):
            if steps<0:
                return 0
            if steps==0 or steps==1:
                return 1
            val=0
            for i in range(1,3):
                val+=func(steps-i)
            return val
        return func(n)

        