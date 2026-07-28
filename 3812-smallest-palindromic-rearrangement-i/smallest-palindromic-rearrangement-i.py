class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        temp=""
        mid=""
        for a,b in sorted(count.items()):
            if b%2!=0:
                mid=a
            for i in range(b//2):
                temp+=a
        ans=temp+mid+temp[::-1]
        return ans 




        