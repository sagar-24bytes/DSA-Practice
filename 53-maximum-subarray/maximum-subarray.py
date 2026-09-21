class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum=float('-inf')
        curr_sum=0
        for n in nums:
            curr_sum=max(curr_sum+n,n)
            maxsum=max(curr_sum,maxsum)
        return maxsum