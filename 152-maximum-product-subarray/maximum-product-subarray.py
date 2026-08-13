class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min=curr_max=nums[0]
        ans=nums[0]

        for n in range(1,len(nums)):
            if nums[n]<0:
                curr_min,curr_max=curr_max,curr_min
            curr_max=max(curr_max*nums[n],nums[n])
            curr_min=min(curr_min*nums[n],nums[n])
            ans=max(curr_max,ans)
        return ans

        