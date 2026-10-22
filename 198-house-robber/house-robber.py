from functools import lru_cache
class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        @lru_cache(None)
        def func(idx):
            if idx<0:
                return 0
            take=func(idx-2)+nums[idx]
            not_take=func(idx-1)
            return max(take,not_take)
        return func(n-1)

        