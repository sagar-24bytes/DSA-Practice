class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        buckets=[[]for _ in range(len(nums)+1)]
        for n,count in freq.items():
            buckets[count].append(n)
        ans=[]
        for i in range(len(buckets)-1,-1,-1):
            for x in buckets[i]:
                ans.append(x)
                if len(ans)==k:
                    return ans
            
        

        