class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        rows=len(board)
        cols=len(board[0])
        visited=[[False]*cols for _ in range(rows)]

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or visited[r][c]:
                return
            # if r==0 or r==rows-1 or c==0 or c==cols-1:
            visited[r][c]=True
            if board[r][c]=='O':
                # visited[r][c]=True
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        for r in range(rows):
            for c in range(cols):
                if (r==0 or r==rows-1 or c==0 or c==cols-1) and board[r][c]=='O' and not visited[r][c]:
                    # visited[r][c]=True
                    dfs(r,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and not visited[r][c]:
                    board[r][c]='X'

        
            
    
        
        

        