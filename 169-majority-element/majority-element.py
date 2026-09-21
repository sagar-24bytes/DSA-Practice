class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate=None
        votes=0
        for n in nums:
            if candidate==None or votes==0:
                candidate=n
            if candidate==n:
                votes+=1
            else:
                votes-=1
        return candidate
        