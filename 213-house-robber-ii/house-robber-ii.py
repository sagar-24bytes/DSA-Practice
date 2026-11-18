class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n<=1:
            return nums[0]
        a2,a1=0,nums[0]
        b2,b1=0,nums[1]
        for i in range(1,n-1):
            take=nums[i]
            if i>1:
                take+=a2
            not_take=a1
            curr=max(take,not_take)
            a2,a1=a1,curr
        for i in range(2,n):
            take=nums[i]
            if i>1:
                take+=b2
            not_take=b1
            curr=max(take,not_take)
            b2,b1=b1,curr
        return max(a1,b1)


        