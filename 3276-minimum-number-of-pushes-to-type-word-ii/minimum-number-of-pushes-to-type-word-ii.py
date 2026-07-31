from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        if n<=8:
            return n
        phone=Counter(word)
        freq=sorted(phone.values(),reverse=True)
        ans=0
        for i,x in enumerate(freq):
            ans+=((i//8)+1)*x
        return ans
        