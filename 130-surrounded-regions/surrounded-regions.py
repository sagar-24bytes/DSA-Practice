from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q=deque()
        rows=len(board)
        cols=len(board[0])
        visited=[[False]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and (r==0 or r==rows-1 or c==0 or c==cols-1):
                    visited[r][c]=True
                    q.append((r,c))
        
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            r,c=q.popleft()
            for x,y in d:
                nr=r+x
                nc=c+y
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc]=='O' and  not visited[nr][nc]:
                    visited[nr][nc]=True
                    q.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and not visited[r][c]:
                    
                    board[r][c]='X'
        





       
        


                    


        