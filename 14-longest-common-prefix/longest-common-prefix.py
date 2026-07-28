class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        for i in range(len(strs[0])):
            ch=strs[0][i]
            for word in strs:
                if i>=len(word) or ch!=word[i]:
                    return result
            result+=ch
        return result
        