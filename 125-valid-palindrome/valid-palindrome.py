class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=""
        for x in s:
            if x.isalnum():
                st+=x.lower()
        return st==st[::-1]
        