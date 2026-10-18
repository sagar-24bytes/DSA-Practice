class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path=[]
        ans=[]
        def func(open,close):
            if len(path)==2*n:
                ans.append("".join(path[:]))
                return
            if open<n:
                path.append('(')
                func(open+1,close)
                path.pop()
            if close<open:
                path.append(")")
                func(open,close+1)
                path.pop()
        func(0,0)
        return ans
        