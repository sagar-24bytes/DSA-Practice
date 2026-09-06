class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        left=0
        ans=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while len(freq)<right-left+1:
                if s[left] in freq:
                    freq[s[left]]-=1
                    if freq[s[left]]==0:
                        del freq[s[left]]
                left+=1
            if right-left+1==len(freq):
                ans=max(ans,right-left+1)
        return ans 

        