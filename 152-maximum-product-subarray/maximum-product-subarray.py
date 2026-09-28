class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_p=max_p=nums[0]
        ans=nums[0]

        for i in range(1,len(nums)):
            curr=nums[i]
            if curr<0:
                max_p,min_p=min_p,max_p
            min_p=min(curr,min_p*curr)
            max_p=max(curr,max_p*curr)
            ans=max(max_p,ans)
        return ans
        
        

        
        