class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        path=[]
        ans=[0]
        
        def func(i):
            if i==len(nums):
                res=0
                for x in path:
                    res^=x
                ans[0]+=res
                return
            path.append(nums[i])
            func(i+1)
            path.pop()
            func(i+1)
        func(0)
        return ans[0] 
        