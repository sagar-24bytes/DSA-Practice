class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        path=[]
        def func(i):
            if i==len(nums):
                ans.add(tuple(path))
                return
            path.append(nums[i])
            func(i+1)
            path.pop()
            func(i+1)
        func(0)
        return [list(x) for x in ans]
        