class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits=[]
        for s in str(n):
            digits.append(int(s))
        digits.sort()
        return digits[-1]*digits[-2]
        