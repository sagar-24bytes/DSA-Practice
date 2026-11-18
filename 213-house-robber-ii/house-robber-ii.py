class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n<=1:
            return nums[0]
        def func(idx,base,dp):
            if idx==base:
                return nums[base]
            if idx<base:
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            take=nums[idx]+func(idx-2,base,dp)
            not_take=func(idx-1,base,dp)
            dp[idx]=max(take,not_take)
            return dp[idx]
        dp=[-1]*n
        fp=[-1]*n
        return max(func(n-1,1,dp),func(n-2,0,fp))

        