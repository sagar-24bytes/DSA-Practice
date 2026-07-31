from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        ans=0
        idx=0
        phone=Counter(word)
        freq=sorted(phone.values(),reverse=True)
        for x in freq:
            idx+=1
            if 1<=idx<=8:
                mul=1
            elif 9<=idx<=16:
                mul=2
            elif 17<=idx<=24:
                mul=3
            else:
                mul=4
            ans+=(mul*x)
        return ans
            
        