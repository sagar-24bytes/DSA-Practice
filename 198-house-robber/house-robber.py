class Solution:
    def rob(self, nums: list[int]) -> int:
        # recursion solution + Memoization
        n=len(nums)
        dp=[-1]*(n)

        def func(idx):
            if idx==0:
                return nums[0]
            if idx<0:
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            take=nums[idx]+func(idx-2)
            not_take=func(idx-1)
            dp[idx]=max(take,not_take)
            return dp[idx]
        return func(n-1)
        
     
        