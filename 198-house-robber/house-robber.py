class Solution:
    def rob(self, nums: list[int]) -> int:
        first=sec=0
        for n in nums:
            curr=max(sec,first+n)
            first=sec
            sec=curr
        return sec
        