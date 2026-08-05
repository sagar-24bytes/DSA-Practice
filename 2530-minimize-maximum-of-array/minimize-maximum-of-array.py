class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans=0
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            x=i+1
            curr=(total+x-1)//x   # in place of math.ceil we used 
            ans=max(ans,curr)
        return ans