from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache(None)
        def dfs(i):
            if i==len(stoneValue):
                return 0
            curr=0
            best=float('-inf')
            for j in range(i,min(i+3,len(stoneValue))):
                curr+=stoneValue[j]
                best=max(best,curr-dfs(j+1))
            return best
        ans=dfs(0)
        if ans>0:
            return "Alice"
        elif ans<0:
            return "Bob"
        else:
            return "Tie"


        