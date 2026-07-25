class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n=int(str(abs(x))[::-1])
        if x<0:
            neg=-1
        else:
            neg=1
        n=neg*n
        if n<(-2**31) or n>(2**31)-1:
            return 0
        return n
        