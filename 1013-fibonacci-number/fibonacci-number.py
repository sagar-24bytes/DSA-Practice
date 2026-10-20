class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        def func(n):
            if n<=1:
                return n
            if dp[n]!=-1:
                return dp[n]
            dp[n]=func(n-1)+func(n-2)
            return dp[n]
        return func(n)


        