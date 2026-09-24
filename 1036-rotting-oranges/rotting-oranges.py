from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        ans=0
        if fresh==0:
            return 0
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        while q and fresh>0:
            n=len(q)
            for i in range(n):
                r,c=q.popleft()
                for x,y in d:
                    nr=r+x
                    nc=c+y
                    if nr<0 or nr>=rows or 0>nc or nc>=cols:
                        continue
                    if grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))
            ans+=1
        return ans if fresh==0 else -1

                