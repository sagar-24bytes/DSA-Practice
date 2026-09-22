from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]
        for num,fr in freq.items():
            buckets[fr].append(num)
        ans=[]
        for f in range(len(buckets)-1,-1,-1):
            for n in buckets[f]:
                ans.append(n)
                if len(ans)==k:
                    return ans
        return ans
        