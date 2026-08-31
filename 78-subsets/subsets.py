class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def dfs(idx,path):
            if idx==n:
                ans.append(path[:])
                return
            # TAKE 
            path.append(nums[idx])   
            dfs(idx+1,path)

            path.pop()    #undo
            
            dfs(idx+1,path)    # DONT TAKE
        dfs(0,[])
        return ans 