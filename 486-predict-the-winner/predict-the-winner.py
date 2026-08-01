class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
    
        left=right=0
        def dfs(l,r):
            
            if l==r:
                return nums[l]
            left=nums[l]-dfs(l+1,r)
            right=nums[r]-dfs(l,r-1)

            return max(left,right)
        a=dfs(0,len(nums)-1)
        return a>=0


        