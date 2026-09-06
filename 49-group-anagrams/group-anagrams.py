class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}

        for s in strs:
            st="".join(sorted(s))
            res.setdefault(st,[]).append(s)
        return list(res.values())
        