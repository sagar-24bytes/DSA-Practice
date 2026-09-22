from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq=Counter(nums)
        temp=freq.most_common()
        ans=[]
        for x,y in temp:
            ans.append(x)
            if len(ans)==k:
                break
        return ans
        