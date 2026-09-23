class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        path=[]
        def dfs(open_p,close_p):
            if len(path)==2*n:
                ans.append("".join(path[:]))
                return
            if open_p<n:
                path.append('(')
                dfs(open_p+1,close_p)
                path.pop()
            if close_p<open_p:
                path.append(')')
                dfs(open_p,close_p+1)
                path.pop()
        dfs(0,0)
        return ans