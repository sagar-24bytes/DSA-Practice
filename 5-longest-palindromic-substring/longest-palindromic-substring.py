class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        def palindrome(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        for i in range(len(s)):
            odd=palindrome(i,i)
            even=palindrome(i,i+1)
            print(odd)
            print(even)
            if len(odd)>len(ans):
                ans=odd
            
            if len(even)>len(ans):
                ans=even
        return ans
        