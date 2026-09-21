class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        ans=prefix_sum=0
        for n in nums:
            prefix_sum+=n
            if prefix_sum-k in seen:
                ans+=seen[prefix_sum-k]
            seen[prefix_sum]=seen.get(prefix_sum,0)+1
        return ans


        