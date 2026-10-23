class Solution:
    def rob(self, nums: list[int]) -> int:
        # tabulation method (space optimized)
        n=len(nums)
        prev2=0
        prev=nums[0]


        for i in range(1,n):
            take=nums[i]
            if i>1:
                take+=prev2
            not_take=prev
            curr=max(take,not_take)
            prev2,prev=prev,curr
        return prev

        
     
        