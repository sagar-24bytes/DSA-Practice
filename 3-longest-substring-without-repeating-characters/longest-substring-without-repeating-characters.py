class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        ans=0

        for right in range(len(s)):
            seen[s[right]]=seen.get(s[right],0)+1
            while seen[s[right]]>1:
                seen[s[left]]-=1
                if seen[s[left]]==0:
                    del seen[s[left]]
                left+=1
            ans=max(ans,right-left+1)
           
        return ans 
        