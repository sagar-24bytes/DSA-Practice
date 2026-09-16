from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        ans=[[-1]*cols for _ in range(rows)]
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    ans[r][c]=0
                    q.append((r,c))
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            r,c=q.popleft()

            for x,y in d:
                nr=r+x
                nc=c+y
                if 0<=nr<rows and 0<=nc<cols:
                    if ans[nr][nc]==-1:
                        q.append((nr,nc))
                        ans[nr][nc]=ans[r][c]+1
                        
        return ans 
            

        