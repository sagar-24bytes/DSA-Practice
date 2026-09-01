from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fresh=0
        rows=len(grid)
        cols=len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        ans=0
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for a,b in direction:
                    R=r+a
                    C=c+b
                    if 0<=R<rows and 0<=C<cols and grid[R][C]==1:
                        grid[R][C]=2
                        q.append((R,C))
                        fresh-=1
            ans+=1
        return ans if fresh==0 else -1
            
            