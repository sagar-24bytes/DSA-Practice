class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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
                else:
                    continue
        for i in range(rows):
            for j in range(cols):
                if i==0 or j==0:
                    pacific.add((i,j))
                    dfs(i,j,pacific)
        for i in range(rows):
            for j in range(cols):
                if i==rows-1 or j==cols-1:
                    atlantic.add((i,j))
                    dfs(i,j,atlantic)
        final=pacific & atlantic
        # print(final)
        ans=[list(x) for x in final]
        # print(ans)
        return ans
        
                  

        