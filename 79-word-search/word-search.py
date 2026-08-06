class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n=len(board)
        rows=n
        cols=len(board[0])

        visited=[[False]*cols for _ in range(rows)]

        def dfs(r,c,w):
            if w==len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            if visited[r][c]:
                return False
            if not visited[r][c] and board[r][c]!=word[w]:
                return False
            visited[r][c]=True
            a=(dfs(r-1,c,w+1) or dfs(r+1,c,w+1) or dfs(r,c-1,w+1) or dfs(r,c+1,w+1))
            visited[r][c]=False
            return a
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False


                
        