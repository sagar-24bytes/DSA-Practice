class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]

        def func(start,idx,dp):
            if idx==start:
                return nums[idx]
            if idx<start:
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            take=nums[idx]+func(start,idx-2,dp)
            not_take=func(start,idx-1,dp)
            dp[idx]=max(take,not_take)
            return dp[idx]
        dp=[-1]*n
        fp=[-1]*n
        ans=max(func(0,n-2,dp), func(1,n-1,fp))
        return ans
        
            

        