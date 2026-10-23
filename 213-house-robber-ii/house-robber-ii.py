class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]
        a1,b1=0,nums[0]
        a2,b2=0,nums[1]
        for i in range(1,n-1):
            take1=nums[i]
            if i>1:
                take1+=a1
            not_take1=b1
            curr1=max(take1,not_take1)
            a1,b1=b1,curr1
        for i in range(2,n):
            take2=nums[i]
            if i>1:
                take2+=a2
            not_take2=b2
            curr2=max(take2,not_take2)
            a2,b2=b2,curr2
        return max(b1,b2)
        
            

        