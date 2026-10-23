class Solution:
    def rob(self, nums: list[int]) -> int:
        # tabulation method
        n=len(nums)
        dp=[-1]*(n)
        dp[0]=nums[0]

        for i in range(1,n):
            take=nums[i]
            if i>1:
                take+=dp[i-2]
            not_take=dp[i-1]
            dp[i]=max(take,not_take)
        return max(dp)

        
     
        