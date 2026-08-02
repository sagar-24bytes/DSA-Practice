class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for curr in range(len(heights)):
            while stack and heights[stack[-1]]>heights[curr]:
                h=heights[stack.pop()]
                if stack:
                    w=curr-stack[-1]-1
                else:
                    w=curr
                max_area=max(max_area,h*w)
            stack.append(curr)
        n=len(heights)
        while stack:
            h=heights[stack.pop()]
            if stack:
                w= n-stack[-1]-1
            else:
                w=n
            max_area=max(max_area,h*w)
        return max_area
        
        