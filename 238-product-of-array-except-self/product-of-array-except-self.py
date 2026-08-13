class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod=post_prod=1
        ans=[]
        for i in range(len(nums)):
            ans.append(pre_prod)
            pre_prod*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            ans[j]*=post_prod
            post_prod*=nums[j]
        return ans


        