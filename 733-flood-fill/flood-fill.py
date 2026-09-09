class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        original=image[sr][sc]
        visited=[[False]*cols for i in range(rows)]
        if original==color:
            return image
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            image[r][c]=color
            visited[r][c]=True
            for x,y in d:
                nr=r+x
                nc=c+y
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==original and not visited[nr][nc]:
                    dfs(nr,nc)
                
        dfs(sr,sc)
        return image

            
        