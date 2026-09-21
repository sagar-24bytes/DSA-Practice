from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq=Counter(nums)
        n=len(nums)
        for x,y in freq.items():
            if y>(n//2):
                return x


        