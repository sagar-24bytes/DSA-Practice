class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        if n<=8:
            return n
        x=n//8
        r=n%8
        add=0
        for i in range(1,x+1):
            add+=i
        ans=(add*8)+((x+1)*(r))
        return ans 
        