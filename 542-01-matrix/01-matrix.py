from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows=len(mat)
        cols=len(mat[0])
        ans=[[float('inf')]*cols for _ in range(rows)]
        q=deque()
        dist=[(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    ans[r][c]=0
                    q.append((r,c,0))
        while q:
            r,c,d=q.popleft()
            for x,y in dist:
                nr=r+x
                nc=c+y
                if 0<=nr<rows and 0<=nc<cols:
                    if mat[nr][nc]==1:
                        ans[nr][nc]=min(ans[nr][nc],d+1)
                        q.append((nr,nc,ans[nr][nc]))
                        mat[nr][nc]=0
        return ans

