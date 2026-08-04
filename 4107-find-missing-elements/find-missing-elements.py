class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start=min(nums)
        end=max(nums)
        ans=[]
        for i in range(start,end+1):
            if i not in nums:
                ans.append(i)
        return ans
        