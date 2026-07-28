class Solution(object):
    def countPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res={}

        for w in words:
            pattern=[]
            base=ord(w[0])
            for i in w:
                diff=(ord(i)-base)%26
                pattern.append(diff)
            p=tuple(pattern)
            res[p]=res.get(p,0)+1
        ans=0
        for x in res.values():
            ans+=x*(x-1)//2    # example 1 pattern -> 4 same as that pattern ,then no. of pairs=4C2=4*3/2 
        return ans
        