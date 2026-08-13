class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        vowel={'a','e','i','o','u'}
        ans=0
        count=0
        for right in range(len(s)):
            if s[right] in vowel:
                count+=1
            if right-left+1==k:
                ans=max(ans,count)
                if s[left] in vowel:
                    count-=1
                left+=1
        return ans

                
        