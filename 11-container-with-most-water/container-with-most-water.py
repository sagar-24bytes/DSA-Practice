class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        ans=float('-inf')
        while left<=right:
            l=(right-left)
            if height[left]<=height[right]:
                h=height[left]
                left+=1
            else:
                h=height[right]
                right-=1
            ans=max(ans,(l)*(h))
        return ans

       


        