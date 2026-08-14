class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        res={}
        for s in strs:
            x="".join(sorted(s))
            res.setdefault(x,[]).append(s)
        for y in res.values():
            ans.append(y)
        return ans
        