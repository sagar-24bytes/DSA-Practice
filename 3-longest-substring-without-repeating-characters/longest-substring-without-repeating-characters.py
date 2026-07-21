class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        max_len=0
        freq={}
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
            
                

            

        