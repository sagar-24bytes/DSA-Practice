class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        seen={}
        ans=[]
        for w in s1.split():
            seen[w]=seen.get(w,0)+1
        for w in s2.split():
            seen[w]=seen.get(w,0)+1
        for x,y in seen.items():
            if y==1:
                ans.append(x)
        return ans
        