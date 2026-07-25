class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        ans=""
        for i in range(len(s)):
            even=expand(i,i+1)
            odd=expand(i,i)
            if len(even)>len(ans):
                ans=even
            if len(odd)>len(ans):
                ans=odd
        return ans 


        