class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        res=[]
        def func(i):
            if i==len(nums):
                ans.add(tuple(res))
                return
            res.append(nums[i])
            func(i+1)
            res.pop()
            func(i+1)
        func(0)
        return [list(x) for x in ans] 
        