class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m=len(triangle)
        prev=[float('inf')]*m
        for r in range(m):
            curr=[float('inf')]*m
            for c in range(len(triangle[r])):
                if r==0 and c==0:
                    curr[0]=triangle[0][0]
                    continue
                f=prev[c] if r>0 else float('inf')
                s=prev[c-1] if r>0 and c>0 else float('inf')
                curr[c]=triangle[r][c]+min(f,s)
            prev=curr
        return min(prev)



        