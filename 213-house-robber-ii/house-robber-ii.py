class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n<=1:
            return nums[0]
        dp=[-1]*n
        fp=[-1]*n
        dp[0]=nums[0]
        fp[1]=nums[1]
        fp[0]=0
        for i in range(1,n-1):
            take=nums[i]
            if i>1:
                take+=dp[i-2]
            not_take=dp[i-1]
            dp[i]=max(take,not_take)
        for i in range(2,n):
            take=nums[i]
            if i>1:
                take+=fp[i-2]
            not_take=fp[i-1]
            fp[i]=max(take,not_take)
        return max(dp[n-2],fp[n-1])


        