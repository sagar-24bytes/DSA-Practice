class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        visited=[False]*(len(nums))

        def dfs():
            if len(path)==len(nums):
                ans.append(list(path))
                print(path)
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i]=True
                path.append(nums[i])
                dfs()
                path.pop()
                visited[i]=False
            print(path)
        dfs()
        return ans 
        