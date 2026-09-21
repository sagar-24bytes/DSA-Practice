class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return []
        res={}
        for s in strs:
            x="".join(sorted(s))
            res.setdefault(x,[]).append(s)
        return list(res.values())

        