class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans=float('-inf')
        curr=0
        for n in nums:
            curr=max(n,curr+n)
            ans=max(ans,curr)
        return ans 
        