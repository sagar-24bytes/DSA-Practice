class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]
        def func(i):
            if i==len(nums):
                ans.append(res[:])
                return
            res.append(nums[i])
            func(i+1)
            res.pop()
            func(i+1)
        func(0)
        return ans
        
        