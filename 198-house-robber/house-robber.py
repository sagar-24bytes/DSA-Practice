class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n<=1:
            return nums[0]
        prev2=nums[0]
        prev1=max(nums[0],nums[1])

        for i in range(2,n):
            take=nums[i]+prev2
            not_take=prev1
            curr=max(take,not_take)
            prev2,prev1=prev1,curr
        return prev1
        