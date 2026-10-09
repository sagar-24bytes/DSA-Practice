from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req=Counter(t)
        req_len=len(req)
        left=0
        ans=""
        freq={}
        valid=0
        for right in range(len(s)):
            ch=s[right]
            freq[ch]=freq.get(ch,0)+1
            if ch in req and freq[ch]==req[ch]:
                valid+=1
            while valid==req_len:
                if ans=="" or len(ans)>(right-left+1):
                    ans=s[left:right+1]
                if s[left] in req and freq[s[left]]==req[s[left]]:
                    valid-=1
                freq[s[left]]-=1
                left+=1
        return ans