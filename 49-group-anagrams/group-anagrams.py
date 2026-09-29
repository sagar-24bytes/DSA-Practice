class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen={}
        for s in strs:
            sor="".join(sorted(s))
            seen.setdefault(sor,[]).append(s)
        return list(seen.values())
        