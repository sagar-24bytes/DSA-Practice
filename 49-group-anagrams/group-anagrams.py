class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen={}
        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            key=tuple(count)
            seen.setdefault(key,[]).append(s)
        return list(seen.values())

        