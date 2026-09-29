class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        temp=sorted(freq.items(),key=lambda x:x[1],reverse=True)

        ans=[temp[i][0] for i in range(k)]
        return ans

        