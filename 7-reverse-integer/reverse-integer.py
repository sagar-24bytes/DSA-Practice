class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x<0:
            pre=-1
        else:
            pre=1
        x=abs(x)
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x//=10
        ans=pre*rev
        if ans<(-2**31) or ans>(2**31-1):
            return 0
        return ans
        