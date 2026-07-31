class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=float('-inf')
        left=0
        right=len(height)-1
        while left<=right:
            area=(right-left)*(min(height[right],height[left]))
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
            max_area=max(max_area,area)
        return max_area
        