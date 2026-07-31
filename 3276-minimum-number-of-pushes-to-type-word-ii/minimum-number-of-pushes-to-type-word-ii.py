from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        ans=0
        idx=0
        phone=Counter(word)
        freq=sorted(phone.values(),reverse=True)
        for x in freq:
            mul=(idx//8)+1
            ans+=(mul*x)
            idx+=1
        return ans
            
        