class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        path=[]
        def func(open_b,close_b):
            if len(path)==2*n:
                ans.append("".join(path[:]))
                return
            if open_b<n:
                path.append('(')
                func(open_b+1,close_b)
                path.pop()
            if close_b<open_b:
                path.append(')')
                func(open_b,close_b+1)
                path.pop()
        func(0,0)
        return ans
        