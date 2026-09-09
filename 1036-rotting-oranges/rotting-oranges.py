from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        ans=0
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        visited=[[False]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for x,y in d:
                    nr=r+x
                    nc=c+y
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))
            ans+=1
        return ans if fresh==0 else -1
            
            
            

        