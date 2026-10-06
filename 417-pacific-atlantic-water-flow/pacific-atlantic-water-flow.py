from collections import deque
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific=set()
        atlantic=set()
        p=deque()
        a=deque()
        
        for r in range(rows):
            for c in range(cols):
                if r==0 or c==0:
                    p.append((r,c))
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        while p:
            r,c=p.popleft()
            pacific.add((r,c))
            for x,y in d:
                nr=r+x
                nc=c+y
                if 0<=nr<rows and 0<=nc<cols:
                    if heights[r][c]<=heights[nr][nc] and (nr,nc) not in pacific:
                        p.append((nr,nc))
        

        for r in range(rows):
            for c in range(cols):
                if r==rows-1 or c==cols-1:
                    a.append((r,c))
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        while a:
            r,c=a.popleft()
            atlantic.add((r,c))
            for x,y in d:
                nr=r+x
                nc=c+y
                if 0<=nr<rows and 0<=nc<cols:
                    if heights[r][c]<=heights[nr][nc] and (nr,nc) not in atlantic:
                        a.append((nr,nc))
        res=(pacific & atlantic)
        return [list(x) for x in res]
                    

        