class Solution:
    def rob(self, nums: list[int]) -> int:
        # tabulation method (space optimized)
        n=len(nums)
        prev2=nums[0]
        if n==1:
            return nums[0]
        prev=max(nums[0],nums[1])

        for i in range(2,n):
            take=nums[i]+prev2
            not_take=prev
            curr=max(take,not_take)
            prev2,prev=prev,curr
        return prev

        
     
        