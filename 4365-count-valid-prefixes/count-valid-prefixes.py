class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zero,one=0,0
        ans=0
        for ch in s:
            if ch=='1':
                one+=1
            else:
                zero+=1
            if abs(zero-one)<=1:
                ans+=1
        return ans