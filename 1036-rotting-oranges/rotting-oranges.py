from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        if fresh==0:
            return 0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        minutes=0
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for a,b in directions:
                    R=r+a
                    C=c+b
                    if 0<=R<rows and 0<=C<cols and grid[R][C]==1:
                        grid[R][C]=2
                        fresh-=1
                        q.append((R,C))
            minutes+=1
        return minutes if fresh==0 else -1

        