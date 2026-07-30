class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        path=[]

        def dfs(idx):
            if idx==len(nums):
                ans.add(tuple(path[:]))
                return
            path.append(nums[idx])
            dfs(idx+1)
            path.pop()
            dfs(idx+1)
        dfs(0)
        return [list(v) for v in ans]
        
            
        