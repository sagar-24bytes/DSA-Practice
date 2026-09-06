class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxv=float('-inf')
        curr=0
        for n in nums:
            curr=max(n,n+curr)
            maxv=max(maxv,curr)
  
        return maxv

        