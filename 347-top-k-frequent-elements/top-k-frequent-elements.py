from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        x=count.most_common()
        ans=[]
        i=0
        for n in range(len(x)):
            i+=1
            if i<=k:
                ans.append(x[n][0])

        return ans





        