class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
        memo={}
        def dfs(r,c,steps):
            if r<0 or r>=n or c<0 or c>=n:
                return 0
            if (r,c,steps) in memo:
                return memo[(r,c,steps)]
            if steps==k:
                return 1
            
            
            count=0
            for a,b in moves:
                R=r+a
                C=c+b
                count+=dfs(R,C,steps+1)
            memo[(r,c,steps)]=count
            return memo[(r,c,steps)]
        p=dfs(row,column,0)
        ans=p/(8**k)
        return ans
        