class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum,count=0,0
        seen={0:1}
        for n in nums:
            prefix_sum+=n
            if prefix_sum-k in seen:
                count+=seen[prefix_sum-k]
            seen[prefix_sum]=seen.get(prefix_sum,0)+1
        return count

        