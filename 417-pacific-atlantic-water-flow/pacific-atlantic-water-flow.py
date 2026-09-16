class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific=set()
        atlantic=set()
        ans=[]
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r,c,temp):
            
            for x,y in d:
                nr=r+x
                nc=c+y
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue
                if heights[nr][nc]>=heights[r][c] and (nr,nc) not in temp:
                    temp.add((nr,nc))
                    dfs(nr,nc,temp)
            
        for r in range(rows):
            for c in range(cols):
                if r==0 or c==0:
                    pacific.add((r,c))
                    dfs(r,c,pacific)

        for r in range(rows):
            for c in range(cols):
                if r==rows-1 or c==cols-1:
                    atlantic.add((r,c))
                    dfs(r,c,atlantic)

        res=atlantic & pacific
        return list(res)

                
                
            

        