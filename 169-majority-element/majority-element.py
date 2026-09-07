class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote=0
        candidate=None
        for n in nums:
            if vote==0:
                candidate=n
            if n==candidate:
                vote+=1
            else:
                vote-=1
        return candidate